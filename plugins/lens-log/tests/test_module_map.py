"""The module map: a change to decomposition.json's modules needs an evaluation entry."""
import json
import sys
from datetime import datetime
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import record_touch  # noqa: E402
import stop_check  # noqa: E402
from conftest import SAMPLE  # noqa: E402
from lenslog import definition, entries  # noqa: E402

NOW = datetime(2026, 10, 21, 7, 0, 0)

EVAL_ENTRY = """---
type: decision
module: lens-core
surfaces: [definition]
date: 2026-10-21T07:00
evaluation: {evaluation}
modules: [{modules}]
---

# t

## Lessons
x
"""


def write_definition(root, modules, proposed=()):
    data = dict(SAMPLE, modules=list(modules), proposed=list(proposed))
    data["surfaces"] = SAMPLE["surfaces"] + [
        {"name": "definition", "paths": ["decomposition.json"], "on": "write", "entry": "decision"}]
    (root / "decomposition.json").write_text(json.dumps(data), encoding="utf-8")


def write_eval_entry(root, name, modules, evaluation="surveyor/docs/decomposition/evaluations/x.md"):
    d = root.joinpath(*entries.ENTRIES_DIR)
    d.mkdir(parents=True, exist_ok=True)
    (d / name).write_text(EVAL_ENTRY.format(evaluation=evaluation, modules=", ".join(modules)),
                          encoding="utf-8")


def touch_definition(root):
    record_touch.handle({"session_id": "s1", "cwd": str(root), "tool_name": "Edit",
                         "tool_input": {"file_path": str(root / "decomposition.json")}})


def stop(root):
    return {"session_id": "s1", "cwd": str(root), "hook_event_name": "Stop",
            "stop_hook_active": False, "last_assistant_message": "done"}


def test_definition_reads_modules_and_proposed(repo):
    write_definition(repo, ["a", "b"], ["new thing"])
    assert definition.load(repo).module_map == frozenset({"a", "b", "new thing"})


def test_definition_without_modules_has_empty_map(repo):
    assert definition.load(repo).module_map == frozenset()


def test_definition_rejects_non_string_modules(repo):
    write_definition(repo, ["a", 3])
    with pytest.raises(definition.DefinitionError):
        definition.load(repo)


def test_last_evaluated_map_takes_latest_entry_with_evaluation(repo):
    write_eval_entry(repo, "2026-10-01-a.md", ["a"])
    write_eval_entry(repo, "2026-10-02-b.md", ["a", "b"])
    write_eval_entry(repo, "2026-10-03-c.md", ["a", "b", "c"], evaluation="")
    assert entries.last_evaluated_map(repo) == {"a", "b"}


def test_last_evaluated_map_none_without_entries(repo):
    assert entries.last_evaluated_map(repo) is None


def test_unchanged_map_needs_only_the_normal_entry(repo):
    write_definition(repo, ["a", "b"])
    write_eval_entry(repo, "2026-10-01-a.md", ["a", "b"])
    touch_definition(repo)
    write_eval_entry(repo, "2026-10-21-edit.md", ["a", "b"], evaluation="")
    assert stop_check.decide(stop(repo), NOW) is None


def test_changed_map_without_evaluation_blocks(repo):
    write_definition(repo, ["a", "b"])
    write_eval_entry(repo, "2026-10-01-a.md", ["a"])
    touch_definition(repo)
    write_eval_entry(repo, "2026-10-21-edit.md", ["a", "b"], evaluation="")
    out = stop_check.decide(stop(repo), NOW)
    assert out["decision"] == "block"
    assert "module map" in out["reason"] and "evaluation:" in out["reason"]
    assert "added: b" in out["reason"]


def test_changed_map_with_evaluation_entry_allows(repo):
    write_definition(repo, ["a", "b"])
    write_eval_entry(repo, "2026-10-01-a.md", ["a"])
    touch_definition(repo)
    write_eval_entry(repo, "2026-10-21-eval.md", ["a", "b"])
    assert stop_check.decide(stop(repo), NOW) is None


def test_map_without_any_baseline_blocks(repo):
    write_definition(repo, ["a"])
    touch_definition(repo)
    write_eval_entry(repo, "2026-10-21-edit.md", ["a"], evaluation="")
    out = stop_check.decide(stop(repo), NOW)
    assert out["decision"] == "block" and "module map" in out["reason"]


def test_map_problem_recorded_as_miss_on_second_stop(repo):
    write_definition(repo, ["a", "b"])
    write_eval_entry(repo, "2026-10-01-a.md", ["a"])
    touch_definition(repo)
    write_eval_entry(repo, "2026-10-21-edit.md", ["a", "b"], evaluation="")
    assert stop_check.decide(stop(repo), NOW)["decision"] == "block"
    out = stop_check.decide(stop(repo), NOW)
    assert "systemMessage" in out
    missed = list(repo.joinpath(*entries.MISSED_DIR).glob("*.json"))
    assert missed and "module map" in json.loads(missed[0].read_text(encoding="utf-8"))["surfaces"]


def test_no_map_no_check(repo):
    # A definition without modules (e.g. a sibling piece) never triggers the check.
    write_definition(repo, [])
    touch_definition(repo)
    write_eval_entry(repo, "2026-10-21-edit.md", [], evaluation="")
    assert stop_check.decide(stop(repo), NOW) is None
