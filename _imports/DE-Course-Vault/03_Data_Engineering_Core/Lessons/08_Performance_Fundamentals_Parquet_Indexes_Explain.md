---
type: lesson
module: DE Core
timebox_minutes: 75
status: active
prereqs: []
tags: [course/lesson, topic/performance]
updated: 2026-01-18
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
Lab: [[03_Data_Engineering_Core/Labs/06_Lab_Query_Plans_and_Partitioning]]
