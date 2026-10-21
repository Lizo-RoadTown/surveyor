# Context for the surveyor agent (2026-10-21)

This document is for an agent that has no prior context. It defines every term it uses.

## 1. The two layers

**Definition.** The system this method serves has two kinds of overseeing agent, with the same anatomy and different scope:

- The **program agent** oversees ONE project that MANY people work on. It observes knowledge exchanges at the project's shared surfaces and builds the project's shared knowledge map. It is the Lens (the lens-core repo and its siblings).
- The **personal agent** oversees ONE person who works on MANY projects. It observes that one person's own activity everywhere they work, keeps their private memory, and adapts their tools to them. It is being assembled in the tapestry repo.

**Example.** A CubeSat program with many students has one program agent (the program's own observatory). Each student separately has one personal agent across all their own projects. Both agents first need the system DECOMPOSED — its components and the connections between them made explicit — before observation of the flow across those connections means anything.

## 2. Where THIS repo sits

surveyor holds the **decomposition method — the shared spine of BOTH layers**. The operator's formulation (2026-10-21): the two agents' shape is the same "because they oversee knowledge flow with the same decomposition, just different telemetry for a different layer and domain." The method in this repo is that same decomposition. It is used by reference at both layers; it is not itself an observer and does not collect telemetry.

## 3. What was decided today

1. The operator adopted a build plan for the personal agent's working loop; decomposition supplies the structure that observations refer to. Plan: `tapestry/docs/plans/2026-10-21-master-plan-personal-loop.md`.
2. A cross-layer language standard is forming (same function, same base word, layer qualifier `project-` / `personal-`; final names only after the full decomposition is reconciled). The current provisional table does not rename anything in this repo.
3. The work is managed under the **prototype reconstruction procedure** at `tapestry/docs/prototype-reconstruction-procedure.md` (version 0.1). That procedure names the decomposition module as its intended eventual distributor and is shared by versioned reference, never copied divergently (its step 10). Its canonical home is pending; no action in this repo until the operator assigns it.

## 4. This repo's tasks

This repo has no new tasks from today's decisions; this document is context only. One forward note: the reconstruction procedure's relocation to the decomposition module is pending (its own header says so); when the operator assigns its canonical home, it may land here.

## 5. What NOT to do

- Do not build observation or collection machinery here; the method stays a method.
- Do not map the method onto one layer only; it serves both.
- Do not coin new names; the operator names things.

## 6. Pointers

- `tapestry/docs/architecture/2026-10-21-fleet-reality-map.md` — what actually runs today.
- `tapestry/docs/architecture/2026-10-21-task-division-study.md` — the task evidence across repos.
- `tapestry/docs/plans/2026-10-21-master-plan-personal-loop.md` — the master plan.
- `tapestry/docs/prototype-reconstruction-procedure.md` — the management method (versioned reference).
- Loom memory records: `two-level-agent-symmetry-2026-10-21`, `adopted-personal-loop-build-sequence-2026-10-21`.
