# Surveyor — orientation

Not a spec. It says what Surveyor holds, where things are, and what is known to be open.
Progress is recorded as log entries in [`log/entries/`](log/entries/), not here.

## 1. What is here

| Path | What |
|---|---|
| `skills/decomposition/` | The method: steps, scan categories, the evaluate-on-change rule |
| `skills/decomposition-launch/` | How decomposed repos are launched (orientation, never an outside spec) |
| `plugins/lens-log/` | The enforced decomposition log (design in `DESIGN.md`, plan in `PLAN.md`) |
| `docs/decomposition/evaluations/` | Evaluations of the method, one per change event |
| `docs/decomposition/proves/` | The PROVES case: run log, inventories, database map, module map |
| `docs/decomposition/tapestry-docs-precedent.md` | How Tapestry does docs (for the doc agents) |

These came from `lens-core` on 2026-10-20 with their git history.

## 2. Known open work (operator decisions recorded in loom memory)

- **Automatic evaluation trigger** (approved for design): adding, splitting or moving a
  module in a machine-readable module map requires an evaluation entry.
- **Agent-teaching material** from PROVES (ontology, canon, standards, agent specs and
  prompts, lessons): the operator places it in Surveyor's running records; which parts
  come here, and whether proprietary FRAMES/IAKM material may, is the operator's call.
- **Core teachings** of the decomposition component: not written yet.
- **Docs site + documentation agent**: every Lens repo, and Surveyor, gets one.
- **Two new Lens module repos** proposed (access + tenancy; agent oversight + trust),
  names pending.

## 3. Constraints that hold

- Sources are read-only. Never write to PROVES.
- No secrets, keys or source data in this repo.
- Precedent (PROVES, Tapestry) is guidance, not identity.
