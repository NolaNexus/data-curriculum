---
type: lesson
module: DE Core
timebox_minutes: 120
status: planned
tags:
  - course/lab
  - topic/contracts
  - topic/testing
created: 2026-01-18T00:00:00.000Z
kind: lab
estimated_time_minutes: 120
id: les_lab_golden_files_schema_drift_defense
title: Lab — Golden files + schema drift defense
---

# Lab — Golden files + schema drift defense

## Goal
Make your extractor/transformer **regression-testable**.

## Steps
1. Save 2–3 raw payloads into `tests/fixtures/raw/`
2. Parse them into normalized records
3. Assert the parsed output matches a saved “golden” JSON/CSV result
4. Introduce a schema change (simulate drift) and prove tests fail
5. Version your parser and update golden files intentionally

## Evidence
- Test output for pass and intentional fail
- Commit hash

## Bonus
- Emit `schema_hash` and `parser_version` in metadata


# Success criteria
- [ ] (define a testable outcome)
- [ ] (define a reproducible run command)


# Reflection
- What was the sharp edge?
- What would you do differently next time?
