---
type: lesson
module: Shipping
timebox_minutes: 60
status: active
prereqs: []
tags: [course/lesson, topic/ci]
updated: 2026-01-18
---

# CI + pre-commit + release hygiene (keep the project from rotting)

## Minimum automation (v1)
- pre-commit runs: format/lint/tests quickly before commits
- CI runs on every push:
  - python tests
  - `dbt parse` or `dbt build` (as feasible)
  - basic “smoke” run (optional)

## Release hygiene
- Semantic versioning (even for you)
- Changelog entries per meaningful change
- “How to rollback” note in runbook

## Practice
Lab: [[06_Data_Product_Shipping/Labs/03_Lab_Add_Precommit_and_CI]]
