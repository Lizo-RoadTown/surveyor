---
type: decision
module: surveyor
surfaces: [identity, definition]
date: 2026-10-20T14:10
source_commits: {}
---

# Surveyor founded: the decomposition component gets its own repo

## What was done
- Created from `lens-core` with `git filter-repo`, keeping the history (21 commits) of
  `skills/decomposition/`, `skills/decomposition-launch/`, `plugins/lens-log/` and
  `docs/decomposition/` (PROVES case records, evaluations, Tapestry docs precedent).
- Added `CHARTER.md`, `CLAUDE.md`, `docs/BUILD.md`, `README.md`, `decomposition.json`
  (surfaces: source, identity, definition, method, evaluations, cases, tooling),
  `.claude/settings.json` (Tapestry plugins + `lens-log@lizo-skills`), `.env`
  (`LOOM_PROJECT_ID=surveyor`), `.gitignore`, `LICENSE`.
- Onboarded with `tapestry onboard --slug surveyor` against
  `https://loom-project-registry.onrender.com`: project id
  `d9ce5a6d-b8b9-41d5-8785-f2e9b7bb0f14` (local `project-context.json` matches the registry).
- Retargeted `plugins/lens-log/tests/test_real_definition.py` at Surveyor's definition;
  lens-log version 0.1.2. Suite 74/74.

## What was found / decided
Operator decisions, 2026-10-20: the decomposition component (one of five layers of the
individual system, each with its own core teachings) gets its own repo, named **Surveyor**.
It holds the method, the launch rules, lens-log, the evaluations of the method, the case
records (first: PROVES), and the decomposition teachings, and it operates in other repos.
lens-core keeps its own `decomposition.json`, its own log, and its charter job (the lab's
database standard, composition, launcher). The running records include the ontology,
agent training material and lessons learned, not only scripts; which PROVES teaching
material comes here (and whether proprietary FRAMES/IAKM may) is still the operator's call.

## Lessons
A component that operates across many repos was lodged in one of them; giving it a home
of its own makes its boundary match what it does. `tapestry onboard` needs
`--registry-url` on this machine; the default is a placeholder.
