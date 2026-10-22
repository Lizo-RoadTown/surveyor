#!/usr/bin/env python3
"""Stop hook: a turn that touched declared decomposition surfaces must leave a log entry.

Blocks once with exact instructions. If the next stop still has no entry, it allows
the stop and writes a docs/log/missed/ marker instead of looping.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lenslog import definition, entries, state  # noqa: E402

HELPER = Path(__file__).resolve().parent / "new_entry.py"


def _warn(text: str) -> dict:
    # systemMessage is shown to the operator and lets the turn end; additionalContext
    # on Stop would continue the conversation (hooks.md:2614).
    return {"systemMessage": text}


MAP_KEY = "module map"


def module_map_problem(defn, root: Path, pending: dict[str, list[str]]) -> tuple[str, str] | None:
    """(surface, problem) when this turn wrote decomposition.json and its module map
    differs from the map recorded by the latest evaluation entry (DESIGN.md D11)."""
    if not defn.module_map:
        return None
    touched = [n for n in pending if definition.DEFINITION_FILE in defn.surface(n).patterns]
    if not touched:
        return None
    recorded = entries.last_evaluated_map(root)
    current = set(defn.module_map)
    if recorded == current:
        return None
    if recorded is None:
        return touched[0], "has no evaluated baseline: no entry records 'evaluation:' and 'modules:'"
    parts = []
    if added := sorted(current - recorded):
        parts.append("added: " + ", ".join(added))
    if removed := sorted(recorded - current):
        parts.append("removed: " + ", ".join(removed))
    return touched[0], "changed since the last evaluation (" + "; ".join(parts) + ")"


def block_message(defn, missing: dict[str, list[str]], rejected: list[str],
                  map_problem: tuple[str, str] | None = None) -> str:
    lines = ["[lens-log] This turn touched parts of the decomposition that need a log entry before you finish:"]
    by_type: dict[str, list[str]] = {}
    for name, evidence in sorted(missing.items()):
        surface = defn.surface(name)
        more = f" (+{len(evidence) - 1} more)" if len(evidence) > 1 else ""
        lines.append(f"  - {name} (needs a {surface.entry} entry): {evidence[0]}{more}")
        by_type.setdefault(surface.entry, []).append(name)
    if map_problem:
        name, problem = map_problem
        lines.append(f"  - {MAP_KEY} {problem}. Changing the modules needs a Surveyor evaluation "
                     "(skills/decomposition, 'When the decomposition changes') and a decision entry "
                     "whose header adds 'evaluation: <path to that evaluation>' and "
                     f"'modules: [<the full new list>]'.")
        names = by_type.setdefault("decision", [])
        if name not in names:
            names.append(name)
    if rejected:
        lines.append("Not counted, because the '## Lessons' section is empty (write what was learned, or 'none'): "
                     + ", ".join(rejected))
    lines.append("Create the entry with:")
    for entry_type, names in sorted(by_type.items()):
        roots = sorted({r for n in names for e in missing.get(n, [])
                        if (r := definition.source_root(defn, e)) and "*" not in r})
        sources = "".join(f' --source "{r}"' for r in roots)
        reads_source = any(set(defn.surface(n).patterns) & set(defn.sources) for n in names)
        if reads_source and not roots:
            sources = ' --source "<local folder of each source repo read>"'

        # The interpreter running this hook, not whatever 'python' is on PATH (M1).
        lines.append(f'  "{sys.executable}" "{HELPER}" --type {entry_type} --surfaces {",".join(names)} '
                     f'--slug <short-slug> --title "<what this was>"{sources}')
    lines.append("Then fill in 'What was done', 'What was found / decided' and 'Lessons'. "
                 "See the lens-log:log-entry skill.")
    return "\n".join(lines)


def _changed_since(root: Path, name: str, since: float | None) -> bool:
    if since is None:
        return False
    try:
        return Path(root).joinpath(*entries.ENTRIES_DIR, name).stat().st_mtime > since
    except OSError:
        return False


def decide(data: dict, now: datetime | None = None) -> dict | None:
    # Stop input carries stop_hook_active, last_assistant_message, background_tasks and
    # session_crons; it has no tool_calls (hooks.md:2535). Touches come from PostToolUse.
    root = definition.find_root(Path(data.get("cwd") or "."))
    if root is None:
        return None
    try:
        defn = definition.load(root)
    except definition.DefinitionError as e:
        return _warn(f"[lens-log] decomposition.json is invalid, so logging is not enforced: {e}")

    session = data.get("session_id", "")
    sid = state.key(session, root)
    known = {s.name for s in defn.surfaces}
    pending = {k: v for k, v in state.pending(sid).items() if k in known}
    if not pending:
        state.clear(sid)
        return None
    meta = state.meta(sid) or {}
    before = set(meta.get("entries_before") or [])
    since = meta.get("since")
    new = {n for n in entries.list_entries(root) if n not in before or _changed_since(root, n, since)}
    covered, rejected = entries.coverage(root, new)
    missing = {k: v for k, v in pending.items() if k not in covered}
    map_problem = module_map_problem(defn, root, pending)
    if not missing and not map_problem:
        state.clear(sid)
        return None
    # Our own flag is the guard: stop_hook_active is also true when another plugin's
    # Stop hook continued the turn, and our first block must not be skipped then.
    if meta.get("blocked"):
        recorded = dict(missing, **({MAP_KEY: [map_problem[1]]} if map_problem else {}))
        path = entries.write_missed(root, recorded, session, now or datetime.now())
        state.clear(sid)
        rel = path.relative_to(root).as_posix()
        return _warn(f"[lens-log] No log entry was written; recorded a miss at {rel}. The index will list it.")
    state.set_blocked(sid)
    return {"decision": "block", "reason": block_message(defn, missing, rejected, map_problem)}


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        return 0
    try:
        out = decide(data)
    except Exception as e:  # noqa: BLE001 — a hook must never break the session
        print(f"[lens-log] stop_check error: {e!r}", file=sys.stderr)
        return 0
    if out:
        print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
