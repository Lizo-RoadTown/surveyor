---
type: decision
module: surveyor
surfaces: [evaluations, method, source]
date: 2026-10-20T14:15
source_commits:
  PROVES_LIBRARY: 02ab37e
---

# Evaluation: agent-teaching material was never inventoried; method adjusted

## What was done
- Listed PROVES teaching material read-only (`canon/`, `.deepagents/`, agent specs and
  prompts, training tables) after the operator defined the running records.
- Wrote `docs/decomposition/evaluations/2026-10-20-agent-teaching-material.md`.
- Applied its method changes to `skills/decomposition/SKILL.md` (instruction-layer
  inventory, proprietary check, instruction interfaces).

## What was found / decided
Tenets held for code, but "a module's interface is what it touches" was too narrow:
it must include what a module teaches or instructs. The material was dismissed as "not
runtime". Recategorized as the instruction layer of decomposition (Surveyor's running
records), with a new interface to whichever repo runs extraction. Open for the operator:
what comes in and in what form, proprietary FRAMES/IAKM handling, where extraction lives.

## Lessons
Judging material by whether it runs hides the part that shapes how agents think.
