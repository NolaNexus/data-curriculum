---
type: debug-pattern
tags:
  - course/troubleshooting
  - topic/sql
id: doc_row_explosion_from_non_unique_join_keys
title: Row explosion from non-unique join keys
---

# Row explosion from non-unique join keys

## Symptom
Row counts increase unexpectedly after a join.

## Quick tests
- Count distinct join keys on each side
- Check for duplicates on the “one” side

## Fix
- Deduplicate dimension / enforce uniqueness
- Aggregate before joining
- Add dbt uniqueness test on keys

## Prevention
- Write grain at top of each model
