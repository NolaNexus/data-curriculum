---
type: troubleshooting
status: active
created: 2026-01-19T00:00:00.000Z
tags:
  - course/troubleshooting
id: doc_common_failures_and_what_to_check
title: Common failures (and what to check)
---

# Common failures (and what to check)

## Ingestion
- Rate limits → retry/backoff + caching
- Schema drift → keep raw + version parsers
- Duplicates → idempotency key + upsert/overwrite strategy

## dbt/modeling
- Wrong grain → fix before adding logic
- Exploding joins → validate uniqueness + join keys
- Freshness failures → scheduling or source changes

## Dashboards
- Undefined metrics → write metric definition notes
- Time zones → standardize UTC in storage
