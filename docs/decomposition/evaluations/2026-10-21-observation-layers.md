# Decomposition evaluation: observation is several layers, not one module (2026-10-21)

**Trigger:** the operator decided on 2026-10-21:

- Extraction stays with the Lens, which is "really just the curation dashboard" (the agents
  that extract feed what humans verify).
- Two kinds of agent work are separate: (1) the **agentic orchestration that feeds the
  dashboard** (extraction), and (2) an **agentic team that keeps track of the dashboard and
  extraction workflow health**. The second "overlooks everything else". Its models may change
  at any time, so what matters is a module slot that plugs into the dashboard and feeds it.
- More than one layer is observed. Each **contributor** has a personal observer that supports
  their work across all their projects and keeps their context private. Each **project** has a
  shared observer, maintained and configured by someone, that observes the **knowledge
  exchanges between contributors** (contributions, reviews, explanations, handoffs) against
  the project's components and interfaces. Its telemetry builds a **project knowledge map**.
  Taking part in a project does not expose a contributor's other projects or private context.

The A4 module map had one observation module (lens-observe, "signals + metrics") plus a
proposed "agent oversight + trust" repo. The operator's layers **split** lens-observe and
**recategorize** its parts, so the method is evaluated.

## 1. What PROVES actually observes (read-only, 02ab37e / c484e52)

Each kept observation-type module, sorted by **what it observes** (the subject):

| PROVES module (A4 row) | What it observes | Who reads it | New layer |
|---|---|---|---|
| Agent capabilities, proposals, trust history + auto-approve triggers (DB area F, `database-bus.md:33`; dashboard R6) | whether the agents are doing good work | the maintainer | workflow oversight |
| Pipeline + activity instruments: pipeline stats (dashboard U3, R9 panels) | whether the pipeline is moving | the maintainer | workflow oversight |
| Queue API `/health`, `/queue/stats`, `/jobs/{id}` (`backend-inventory.md:28`) | whether intake is up and draining | the maintainer | workflow oversight |
| Error + suggestion logging, diagnostics (`curator/error_logger.py`, `curator_errors/reports`) | failures and fix ideas | the maintainer | workflow oversight |
| Peer-reflection metrics: calibration, rejection trends, reviewer patterns (dashboard U2 + `v_*` views) | how people's judgments meet the agents' and each other's | the project | project observer |
| Org activity heat map (same instruments row: dashboard U3, R9 panels) | who is active where in the project | the project | project observer |
| Review decisions + edits (`validation_decisions`, reviewer edits) | the exchange itself: an agent's candidate meets a human's judgment | the project | project observer's raw evidence |

**Nothing in PROVES is a personal observer.** PROVES is one project, so the personal layer is
not in the source at all. It comes from the operator's architecture (the personalization
module and adaptive engine), and it lies outside the Lens.

## 2. Were the core tenets right?

| Tenet | Verdict | Evidence |
|---|---|---|
| Find modules by bond strength | **Right** | The two groups in §1 bind tightly inside and loosely across. Workflow oversight binds to job, error and agent tables and answers to the maintainer. The project observer binds to decisions, reviewers and activity and answers to the project. |
| A module's interface is what it touches | **Not enough here** | Both groups read some of the same tables. `validation_decisions` feeds agent trust (oversight) and reviewer patterns (project observer). Grouping by tables touched merged them. What separates them is **what is observed** and **who the result is for**. |
| The database is the bus | **Right, but needs a scope contract** | The project observer must see exchanges at project interfaces and nothing from a contributor's private system. That is a rule on what crosses the bus, like row-level security (step 4, "modules that govern the bus"). |
| Precedent ≠ identity | **Right, but it was broken in practice** | lens-observe was defined from Tapestry's `services/project-observatory` ("the module both observatory types borrow", memory `the-lens-repos-created-2026-09-26`). That precedent shaped the category before the source was read by subject. |
| Don't coin names | **Right** | This report uses descriptive labels only. |

**Overall:** the tenets held, but "interface = what it touches" again needed a companion test.
Evaluation 2 added what a module teaches. This one adds **what a module observes, and for whom**.

## 3. Correct but more granular?

**Partly.** The proposed "agent oversight + trust" repo was correct. It now widens into
**workflow oversight** by absorbing pipeline instruments, health and queue stats, and error
logging from lens-observe. That part is more granular and a recategorization. lens-observe
narrows to the **project observer**. This is a real split, because its two halves answer
different questions for different readers.

The personal layer is not a finer cut of anything in PROVES. It is a layer the source never
had.

## 4. Recategorizations and new interfaces

1. **Workflow oversight** (replaces the proposed "agent oversight + trust"; name pending).
   - Watches the extraction pipeline and the dashboard.
   - Writes health, trust and proposals; the dashboard reads them.
   - **New interface:** a pluggable slot. The standard fixes the tables the team writes
     (health, agent trust, proposals) and names no model, so the team's models can change
     without touching the dashboard.
2. **Project observer** (lens-observe, re-scoped).
   - Reads the knowledge exchanges in the lab: decisions, edits, reviewer patterns, activity.
   - Writes **exchange telemetry** that builds the project knowledge map.
   - **New interface:** the exchange-telemetry output (the knowledge map). It is distinct from
     the verified library, which records *what* is known. The map records *where knowledge
     lives and how it moves* between contributors.
3. **Personal observer** (outside the Lens).
   - **New boundary contract:** a project observer receives only what happens at the
     project's shared interfaces. A contributor's personal system sends nothing else unless
     the contributor chooses to. This is a constraint on the bus, not a table.

## 5. Why the original pass missed it

1. Observation was found by the cross-cutting scan ("signals + metrics") and grouped as one
   concern. The scan asked *whether* something observes, not *what* it observes or *for whom*.
2. The category was named from precedent (Tapestry's project observatory) before the source
   was sorted by subject.
3. The personal layer cannot be found in a one-project source. The method has no step for
   layers the operator's architecture defines that the source lacks.

## 6. Method adjustments (applied to `skills/decomposition/SKILL.md`)

- **Step 4, observation layers:** for every signal, metric, log, health check or trust score,
  record what it observes (the machinery's health, the knowledge exchanges between people and
  agents, or one individual), who reads it, and how far its data may travel. Separate the
  layers even when they read the same tables. Give each layer's data scope a bus contract.
- **Step 1, layers the source lacks:** when orienting to the whole, list the layers the
  operator's architecture defines (for example personal versus project) and mark which ones
  the source contains. A layer missing from the source is recorded, not invented.

## 7. Where this leaves the module map

The A4 table rows move as follows (applied in `module-map.md`):

| Row | Was | Now |
|---|---|---|
| Pipeline + activity instruments | lens-observe | split: pipeline stats → workflow oversight; activity heat map → lens-observe (project observer) |
| Error + suggestion logging, diagnostics | lens-observe | workflow oversight |
| Agent oversight + trust | NEW (proposed) | workflow oversight (same proposed repo, wider) |
| Peer-reflection metrics | lens-observe | lens-observe (project observer) |

The operator's open items now include a name for the workflow oversight repo (it replaces
"agent oversight + trust" in the list of names to choose).

## 8. Correction from the operator (later the same day)

§4 and §7 placed the project observer in lens-observe alone. The operator corrected this:
**the Lens, with all its modules, is the project observer**, the larger observatory for one
project. lens-observe is one part of it (the exchange signals), alongside extraction, review,
the read side and workflow oversight. Tapestry and Loom memory plan to build the smaller
**personal observatories** from elements of the Lens.

What changes:
- `module-map.md` section 7 now shows the Lens as the project observatory, with its modules
  as parts, and a reuse link from the Lens modules to personal observatories.
- The tenet verdicts in §2 stand. One more lesson: the evaluation itself mapped a layer onto a
  single repo when the operator meant the whole. When the operator names a layer, check
  whether it means one module or the whole before assigning it.
- Reuse at personal scale is a new reason for an existing rule: Lens modules must stay neutral
  about scale (one project or one person), take their connection injected, and keep their
  interface to what they touch on the bus.

The architecture is written up for every repo in lens-core
`docs/architecture/observatories.md` (approved 2026-10-21).
