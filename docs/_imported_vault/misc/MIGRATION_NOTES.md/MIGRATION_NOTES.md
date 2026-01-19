---
type: notes
status: active
created: 2026-01-19T00:00:00.000Z
tags:
  - course/migration
id: doc_migration_notes_what_we_salvaged_what_needs_work
title: Migration notes (what we salvaged + what needs work)
---

# Migration notes (what we salvaged + what needs work)

This rebuild is intentionally conservative: it keeps your content, but makes the **shape** of the vault easier to navigate.

## Salvaged (high confidence)

These parts are already strong and worth keeping as “foundation infrastructure”:
- `00_START_HERE/` study method, retention system, gates system, standards
- `01_Syllabus/` backward-design structure + pacing guidance
- Module layouts: each track uses `00_Index.md` + `Lessons/` + `Labs/` + `Reference/`
- `08_Capstone/` spec → milestones → runbook → demo checklist
- `10_Templates/` (excellent—this is your “scaffolding engine”)
- `12_Troubleshooting/` and `13_Assessments/` (keeps momentum when stuck)

## Key problems fixed
- **Folder numbering collision**: both Cloud + Capstone were `07_...` in the previous layout.
- **Maintenance files mixed with learning files**: scripts + patches are now under `_meta/`.

## What still needs work (highest leverage)

1) **Single “Curriculum Map” note**
   - A one-page view that answers: *what should I do next, and why?*
   - Add explicit prerequisites between lessons/labs (even if rough).

2) **Frontmatter consistency**
   - Audit flagged multiple notes without YAML frontmatter.
   - Fixing this enables Dataview queries and filtering.

3) **Outcomes + evidence tightened per lab**
   - Some labs are great already; the rest need sharper “success criteria” and “evidence to capture”.

4) **Unify the meaning of “Gates” vs “Assessments”**
   - Suggested split:
     - *Assessments* = knowledge checks (can be done without a working pipeline)
     - *Gates* = working-system proof (repo runs, logs, artifacts)

## Quick audit results (from `vault_audit.sh`)
- Several notes missing frontmatter (dashboard, some reference cards, troubleshooting notes).
- This is a solvable “one afternoon” cleanup, not a redesign.

