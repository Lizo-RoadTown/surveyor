# Working in Surveyor

Loaded into every session in this repo. **Read [`CHARTER.md`](CHARTER.md) first — it is
your identity.** This file is how you operate here.

## Who this repo is
**Surveyor** is the decomposition component: it holds the decomposition method, the
launch rules, the lens-log plugin, the evaluations of the method, the running records of
each case (first: PROVES → The Lens), and the decomposition teachings. It operates in
other repos; it does not own their code or their logs.

## How to work here
1. **Recall memory first.** `LOOM_PROJECT_ID=surveyor` (in `.env`). Recall Surveyor and
   The Lens records at session start.
2. **[`docs/BUILD.md`](docs/BUILD.md) orients you**; it is not a spec.
3. **PROBE before asserting**; cite `file:line`.
4. **Record as you go.** Progress goes in a log entry under `docs/log/entries/` (lens-log
   enforces it). It is a **decision** entry if it changes what this repo is or how it
   connects; otherwise it is progress.
5. **When the decomposition changes, evaluate the method.** Any new module, further split,
   or recategorization gets a full report in `docs/decomposition/evaluations/` and a
   method change in `skills/decomposition/SKILL.md` (see that skill).
6. **Sources are read-only.** PROVES (`PROVES_LIBRARY`, `proves-curation-dashboard`) is
   never modified. Proprietary material (FRAMES, IAKM) is not copied here without the
   operator's say.

## Tapestry wiring
Depends on the Tapestry discipline + patterns plugins and on `lens-log@lizo-skills`
(enabled in `.claude/settings.json`).

## Commit discipline
Small commits, one concern. Never `--no-verify`, never `--amend` on pushed work.
Co-author tag: `Co-Authored-By: Claude <noreply@anthropic.com>`.
