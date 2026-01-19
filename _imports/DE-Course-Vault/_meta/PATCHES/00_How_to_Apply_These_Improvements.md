---
type: patch-instructions
created: 2026-01-18
tags: [course/maintenance]
---

# Improvements Pack v1 — how to apply

This add-on **adds** new lessons/labs/templates. It does not rewrite your existing indexes to avoid merge conflicts.

## After merging
1. Open each module index and add the new links:
   - `02_Foundations/00_Index.md`
   - `03_Data_Engineering_Core/00_Index.md`
   - `06_Data_Product_Shipping/00_Index.md`
2. Optional: add Dataview blocks (already included where useful).

## What this pack adds
- Linux/shell for pipeline operators
- CI + pre-commit + “don’t rot” automation
- Schema contracts + evolution + golden-file extractor tests
- Performance fundamentals (Parquet, partitioning, Postgres indexes, EXPLAIN)
- Security/privacy basics for personal data projects
