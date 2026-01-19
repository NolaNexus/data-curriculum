---
type: lab
created: 2026-01-18
timebox_minutes: 120
tags: [course/cloud, course/lab]
---

# Lab A — Cloud Mirror (object storage)

## Outcome
Mirror `data/raw/` + `data/metadata/` to cloud object storage.

## Options
- AWS S3 citeturn0search1
- Google Cloud Storage citeturn0search2turn0search10
- Cloudflare R2 citeturn0search19

## Steps (generic)
1. Create a bucket
2. Create minimal credentials (least privilege)
3. Write a sync script (uploads new immutable objects only)
4. Store the object key/URL in your metadata table

## Pass criteria
- [ ] Upload works
- [ ] Re-run does not overwrite raw
- [ ] Metadata points to the object key

## Maps to gates
- G1, G2
