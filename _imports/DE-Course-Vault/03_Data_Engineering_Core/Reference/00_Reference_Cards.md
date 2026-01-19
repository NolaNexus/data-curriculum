---
type: reference
status: active
created: 2026-01-19
tags: [course/reference]
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
