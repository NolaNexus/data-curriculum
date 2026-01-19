---
type: lesson
module: DE Core
timebox_minutes: 45
status: active
created: 2026-01-19
tags: [course/lesson, topic/quality]
---

# Goal
Put quality gates in place so bad data doesn’t silently ship.

# Minimum tests
- uniqueness on keys
- not-null on required fields
- freshness checks
- row-count anomaly check (simple)

# Checks
- I can interpret a failing dbt test and trace it to a root cause.
