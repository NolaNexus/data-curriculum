---
type: lesson
module: DE Core
timebox_minutes: 120
status: planned
tags:
  - course/lab
  - topic/performance
created: 2026-01-18T00:00:00.000Z
kind: lab
estimated_time_minutes: 120
id: les_lab_query_plans_partitioning
title: Lab — Query plans + partitioning
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


# Success criteria
- [ ] (define a testable outcome)
- [ ] (define a reproducible run command)


# Reflection
- What was the sharp edge?
- What would you do differently next time?
