---
type: lesson
module: DE Core
timebox_minutes: 75
status: active
prereqs: []
tags:
  - course/lesson
  - topic/performance
updated: 2026-01-18T00:00:00.000Z
estimated_time_minutes: 75
id: les_performance_fundamentals_so_your_project_scales_past_toy_data
title: Performance fundamentals (so your project scales past toy data)
---

# Performance fundamentals (so your project scales past toy data)

## Parquet basics (practical)
- Columnar storage = only read columns you need
- Partitioning = avoid scanning everything
- File sizing matters (too many tiny files is pain)

## Postgres basics
- Indexes speed reads but cost writes
- Use `EXPLAIN`/`EXPLAIN ANALYZE` to see plans
- Keep grain clear to avoid join explosions

## DuckDB basics
- Great for local analytics; loves Parquet
- Avoid reading CSV repeatedly; convert once to Parquet

## Practice
Lab: 06_Lab_Query_Plans_and_Partitioning
