---
type: process
module: surveyor
surfaces: [tooling]
date: 2026-10-21T06:34
source_commits: {}
---

# lens-log 0.1.4: a module-map change needs an evaluation entry

## What was done
Built the automatic decomposition-evaluation trigger the operator approved on 2026-10-20,
in the form set by the approved roadmap method (lens-core
`docs/plans/2026-10-21-roadmap-method-proposal.md`, section 4, item 3).
- `definition.py`: `Definition.module_map` = `modules` + `proposed` from `decomposition.json`;
  rejects non-string names.
- `entries.py`: `last_evaluated_map()` returns the `modules:` list of the latest entry that
  also names an `evaluation:`.
- `stop_check.py`: when a turn writes `decomposition.json` and the map differs from that
  baseline, the turn is blocked with what was added or removed. A second stop records the
  problem under "module map" in `docs/log/missed/`. Fixed a KeyError in the command builder
  for surfaces that were covered but still named.
- DESIGN.md D11; the log-entry skill explains the two header lines.
- 11 new tests in `tests/test_module_map.py`; the suite has 88 passing. Version 0.1.4.

## What was found / decided
The check is stateless: the log is the baseline, so it survives commits and long sessions. It
only runs when `decomposition.json` was written in the turn, so it costs nothing otherwise.
Shell edits to the file are still not detected (known limit; the index Action is the backstop).

## Lessons
Using the log itself as the baseline avoids snapshot state that would be captured after the
edit (PostToolUse fires after the change).
