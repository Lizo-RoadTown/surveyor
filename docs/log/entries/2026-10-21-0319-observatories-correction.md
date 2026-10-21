---
type: process
module: surveyor
surfaces: [cases, evaluations]
date: 2026-10-21T03:19
source_commits: {}
---

# Correction: the Lens as a whole is the project observatory

## What was done
- Rewrote `docs/decomposition/proves/module-map.md` section 7 after the operator's correction:
  the Lens with all its modules is the project observatory; lens-observe is its exchange-signals
  part; Tapestry and Loom memory will build personal observatories from Lens elements. The
  chart was revalidated.
- Appended §8 (the correction) to
  `docs/decomposition/evaluations/2026-10-21-observation-layers.md`.
- Drafted lens-core `docs/architecture/observatories.md` (two validated charts) for the
  operator's approval. Once approved, it becomes the roadmap everyone works from.

## What was found / decided
This is the same split as before, but the project layer maps to the whole Lens, not to one
repo. Personal reuse strengthens the existing reuse rules (neutral about scale, injected
connection, small interface).

## Lessons
When the operator names a layer, check whether it means one module or the whole before
assigning it to a repo.
