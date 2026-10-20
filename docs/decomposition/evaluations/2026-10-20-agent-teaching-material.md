# Decomposition evaluation — agent-teaching material was never inventoried (2026-10-20)

**Trigger:** the operator stated that the running records of decomposition are "not just
the script, it's the ontology and training agents and anything that has to do with
teaching agents how to think or not think and lessons learned". A read-only listing of
`PROVES_LIBRARY` at **02ab37e** then showed a body of material that no inventory (9/26,
A1, A2, A3) treated as a module:

- `canon/` (tracked): `CANON.md`, `KNOWLEDGE_FRAMEWORK.md`, `KNOWLEDGE_CAPTURE_CHECKLIST.md`,
  `FRAMES A Structural Diagnostic for.txt`; plus local (untracked or ignored) `ONTOLOGY.md`,
  `frames_ontology_canon_shaping_data_logic_and_agent_training.md` and the `IAKM_*` papers.
- `.deepagents/`: `AGENT_CONTRACTS.md`, `DECISION_TREE.md`, `PIPELINE_VALIDATION_CHECKLIST.md`,
  `standards/` (`PROVES_CANONICAL_NAMING`, `SYSML_V2_VOCABULARY`, `XTCE_VOCABULARY`,
  `PYTORCH_GEOMETRIC_VOCABULARY`), `agents/extraction_agent.yaml`, session summaries and
  analyses (lessons in practice), `workflows/` examples.
- In code: the agent specifications and prompts (`production/Version 3/subagent_specs_v3.py`),
  the prompt builder (`extraction-api/task_builder.py`), the ontology lookup in
  `extractor_v3.py` (`get_ontology`), and the live-schema tables `training_examples`,
  `training_interactions`, `learning_log`.

Per the operator's rule this is a **new module** (or a recategorization of material
previously dismissed), so the method is evaluated.

## 1. Were the core tenets right?

| Tenet | Verdict | Evidence |
|---|---|---|
| Find modules by bond strength | **Right** | The material is tightly bound inside (vocabularies, canon and agent specs reference each other) and binds to the pipeline at one place: what agents are told and allowed to produce. |
| A module's interface is what it touches | **Incomplete** | The tenet only looks at *runtime* touches (tables, RPCs, imports). Teaching material touches the system through **agents' behavior**, not through calls: a prompt or ontology changes what extraction produces without any table or import showing it. The tenet has no slot for a knowledge-and-instruction interface. |
| The database is the bus | **Right, but not the only bus** | Agents also meet the system through instructions. In PROVES that path is mostly files read at run time or text pasted into prompts. |
| Precedent ≠ identity; don't coin names | **Right** | Followed; this report uses descriptive labels only. FRAMES and IAKM are the operator's proprietary work and are not copied. |

**Overall:** the tenets held for code, but one was too narrow. "What a module touches"
must include what it **teaches or instructs** (ontology, prompts, standards, lessons), not
only what it calls.

## 2. Correct but more granular?

No. This is not a split of an existing module. It is a **category the inventories never
looked at**: A3 listed `.deepagents/` as "not running code" and `task_builder` as a prompt
builder whose output is discarded, and did not read `canon/` at all. The material was
judged by whether it *runs*, not by whether it *shapes* the agents.

## 3. Recategorization and new interface

- **Recategorization:** from "documentation / not runtime" to **the instruction layer of
  decomposition** (the operator's "running records"), owned by Surveyor.
- **New interface:** between Surveyor (which holds the teaching material) and whichever
  repo runs extraction (today lens-ingest): extraction agents get their ontology, prompts,
  standards and lessons from Surveyor's records rather than from text embedded in the
  extraction code. In PROVES this link is implicit and partly broken (the prompt builder's
  output is discarded, `agent_v3.py:331`; the ontology path points outside the repo and
  always falls back, `extractor_v3.py:61`).

## 4. Why the method missed it

1. Step 2 inventoried **code and screens**; it had no instruction to inventory the
   material that trains or instructs agents.
2. Step 3 defined interfaces only as runtime touches.
3. The status axes (working / superseded) were applied to code; docs and specs were
   filtered out as "not runtime" without asking what they teach.

## 5. Method adjustments

- **Step 2, inventory the instruction layer:** list ontology, canon/framework documents,
  agent definitions and contracts, prompts and prompt builders, vocabularies/standards,
  training data, and lessons/session summaries, as candidate modules in their own right.
- **Step 3, instruction interfaces:** record what each module *teaches or instructs*
  (which agents read it, where it is injected) alongside what it calls.
- **Step 4, proprietary check:** mark material that is the operator's proprietary work
  (here FRAMES, IAKM) and never copy it into a public repo without the operator's say.

## 6. Open for the operator

1. Which of this material comes into Surveyor's running records, and in what form
   (copied, summarized, or pointed to)?
2. Whether proprietary FRAMES/IAKM material may live in Surveyor (public) or only be
   referenced.
3. Whether extraction itself stays in lens-ingest (using Surveyor's teaching material) or
   moves under Surveyor.
