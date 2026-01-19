---
type: lesson
module: DE Core
timebox_minutes: 60
status: active
prereqs: []
tags:
  - course/lesson
  - topic/contracts
updated: 2026-01-18T00:00:00.000Z
estimated_time_minutes: 60
id: les_schema_contracts_evolution_stop_drift_from_wrecking_you
title: Schema contracts + evolution (stop drift from wrecking you)
---

# Schema contracts + evolution (stop drift from wrecking you)

Tests detect problems **after** they land. Contracts prevent bad changes from landing.

## Contract types you’ll use in personal projects
- **Source schema contract** (expected columns + types)
- **Parser contract** (what your extractor emits)
- **Model contract** (what downstream tables guarantee)

## Evolution rules (simple but strict)
- Additive changes are usually safe (new nullable columns)
- Renames and type changes are breaking unless versioned
- Always keep raw immutable so you can reparse

## Your “adult” strategy
- Version your parser (`parser_version`)
- Store schema hash/version with metadata
- Maintain golden raw fixtures for regression tests

## Practice
Lab: 05_Lab_Golden_Files_and_Schema_Drift
