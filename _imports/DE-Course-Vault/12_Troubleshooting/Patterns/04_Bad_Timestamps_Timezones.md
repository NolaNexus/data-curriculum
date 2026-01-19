---
type: debug-pattern
tags: [course/troubleshooting, topic/time]
created: 2026-01-18
---

# Bad timestamps / timezones

## Symptom
Freshness tests fail or data appears “in the future/past.”

## Fix pattern
- Store timestamps in UTC (`*_utc`)
- Convert for display at the edge (dashboard/UI)
- Record both `fetched_at_utc` and `source_event_time_utc` if applicable

## Prevention
- Add a test: no timestamps > now()+grace
