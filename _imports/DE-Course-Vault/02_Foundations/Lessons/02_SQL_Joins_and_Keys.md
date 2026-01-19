---
type: lesson
module: Foundations
timebox_minutes: 45
status: active
created: 2026-01-19
tags: [course/lesson, topic/sql]
---

# Goal
Learn joins without accidentally duplicating the universe.

# Key ideas
- Primary keys are promises.
- Joins amplify mistakes if the “one” side isn’t unique.
- Validate grain before building models.

# Practice
- Write a LEFT JOIN and verify:
  - row counts before/after
  - uniqueness of the “one” side keys

# Checks
- I can explain why non-unique keys break star schemas.
