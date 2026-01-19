---
type: lesson
created: 2026-01-18
tags: [course/cloud]
---

# Object storage and artifacts

## What to store
- Immutable raw payloads
- Metadata/provenance JSON
- Parquet exports (silver/gold)
- Static report outputs (HTML)

## Options
- AWS S3 (industry standard). citeturn0search1
- Google Cloud Storage (pairs nicely with Cloud Run). citeturn0search2turn0search10
- Cloudflare R2 (S3-compatible, published free tier for some usage). citeturn0search19
- MinIO for local S3-compat (great for learning; cloud later). citeturn0search0
