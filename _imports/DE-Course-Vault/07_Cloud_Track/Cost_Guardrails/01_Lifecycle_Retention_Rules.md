---
type: guide
created: 2026-01-18
tags: [course/cloud, topic/cost]
---

# Lifecycle + retention rules (simple defaults)

## Suggested defaults
- Raw payloads: keep 30–90 days (unless you need full history)
- Processed artifacts (Parquet): keep “latest + last 7 versions”
- Reports: keep latest only (regenerate anytime)
- Logs: keep 14–30 days

## Why
Storage grows silently. Retention is the antidote.

## Action
Add retention rules to your runbook and enforce them via scripts when possible.
