---
type: decision
module: surveyor
surfaces: [evaluations, method, cases]
date: 2026-10-21T03:11
source_commits: {}
---

# Evaluation: observation is several layers; lens-observe split

## What was done
- Recorded the operator's 2026-10-21 decisions: extraction stays with the Lens (the curation
  dashboard and the agents that feed it); a separate, pluggable agentic team watches the
  health of the dashboard and the extraction workflow; personal observers (per contributor,
  private) and a shared project observer (knowledge exchanges, builds a knowledge map) are
  different layers.
- Wrote `docs/decomposition/evaluations/2026-10-21-observation-layers.md`. It works from the
  existing A1 to A4 records; PROVES was not re-read this turn.
- Updated `docs/decomposition/proves/module-map.md`: moved rows, widened the proposed
  "agent oversight + trust" repo into workflow oversight, re-scoped lens-observe as the project
  observer, and added section 7 with a validated layer chart.
- Added two scan steps to `skills/decomposition/SKILL.md`: observation layers (step 4) and
  layers the source lacks (step 1).

## What was found / decided
The tenets held. "Interface = what it touches" again needed a companion test: what a module
observes and for whom. Oversight and the project observer both read `validation_decisions`,
so grouping by tables merged them. The lens-observe category came from Tapestry precedent
before the source was sorted by subject. PROVES has no personal observer; that layer comes
from the operator's architecture. New contract: a project observer sees only what happens at
the project's shared interfaces.

## Lessons
Sort observation by its subject and reader, not by the tables it reads. A one-project source
cannot show the personal layer, so the method has to ask the operator which layers exist.
