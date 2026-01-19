---
type: standards
status: active
updated: 2026-01-19T00:00:00.000Z
tags:
  - course/standards
id: doc_vault_standards_best_practice_protocol
title: Vault standards (best-practice protocol)
---

# Vault standards (best-practice protocol)

These standards exist to reduce decision fatigue and make the vault queryable.

## 1) Naming conventions
- Files: `NN_Title_With_Underscores.md` (NN only when order matters)
- Avoid renaming files after you’ve linked them widely.
- Prefer descriptive names over clever ones.

## 2) Note properties (Obsidian “Properties”)
Keep properties **flat** (no nested YAML) for maximum compatibility.

### Required for lessons
- `type: lesson`
- `module: Foundations | DE Core | Analytics | Shipping | Optional ML`
- `timebox_minutes: 45` (or 90 etc.)
- `status: draft | active | done`
- `prereqs: []`
- `tags: [...]`

### Required for labs
- `type: lab`
- `module: ...`
- `timebox_minutes: ...`
- `status: planned | active | done`
- `tags: [...]`

### Required for resources
- `type: resource`
- `format: docs|video|course|paper|repo`
- `topic: ...`
- `level: intro|intermediate|advanced`
- `status: unread|reading|done`
- `source_url: ...` (paste URL)
- `tags: [...]`

## 3) Tags taxonomy (keep it small)
- `course/lesson`, `course/lab`, `course/resource`
- `topic/sql`, `topic/python`, `topic/dbt`, `topic/docker`, `topic/metrics`, `topic/orchestration`

## 4) Maps of Content (MOCs)
- Each module index is a MOC.
- Prefer **links + short annotations** over huge paragraphs.
- Optional: use Dataview blocks to auto-list notes.

## 5) Backward design (course design protocol)
- Start with outcome (North Star)
- Define evidence (tests, rubrics, demo)
- Plan activities (lessons + labs)
