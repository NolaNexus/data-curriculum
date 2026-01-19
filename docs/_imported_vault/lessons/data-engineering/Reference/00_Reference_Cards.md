---
type: reference
status: active
created: 2026-01-19T00:00:00.000Z
tags:
  - course/reference
id: doc_de_core_reference_cards
title: DE Core reference cards
---

# DE Core reference cards

## Idempotency quick check
- Natural key defined?
- Upsert/overwrite strategy chosen?
- Rerun yields same outputs?

## Modeling quick check
- Grain written at top of model?
- Keys unique on dimension tables?
- Facts reference dims by stable IDs?

## Quality gates minimum
- uniqueness + not-null + freshness
