---
type: lab
module: DE Core
timebox_minutes: 120
status: planned
tags: [course/lab, topic/performance]
created: 2026-01-18
---

# Lab — Query plans + partitioning

## Goal
Learn to measure performance with evidence (not vibes).

## Tasks
- [ ] Take one slow-ish query and run `EXPLAIN` / `EXPLAIN ANALYZE`
- [ ] Add an index (Postgres) or adjust model (dbt) and compare
- [ ] Convert a CSV workflow to Parquet and compare runtime
- [ ] If using Parquet: partition by a date column and prove scan reduction

## Evidence
- Before/after plan snippets
- Before/after runtime (rough is fine)
