---
type: lesson
module: DE Core
timebox_minutes: 45
status: active
created: 2026-01-19
tags: [course/lesson, topic/ingestion]
---

# Goal
Make reruns safe and enable backfills.

# Patterns
- upsert by natural key
- partition overwrite by date
- temp → validate → swap

# Checks
- Same inputs twice → same final tables.
