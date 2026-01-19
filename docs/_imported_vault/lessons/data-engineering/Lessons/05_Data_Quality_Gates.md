---
type: lesson
module: DE Core
timebox_minutes: 45
status: active
created: 2026-01-19T00:00:00.000Z
tags:
  - course/lesson
  - topic/quality
estimated_time_minutes: 45
id: les_goal
title: Goal
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
