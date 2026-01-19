---
type: debug-pattern
tags:
  - course/troubleshooting
  - topic/ingestion
id: doc_rate_limits_retry_backoff_cache
title: 'Rate limits: retry/backoff/cache'
---

# Rate limits: retry/backoff/cache

## Symptom
429s, intermittent failures, blocked scrapes.

## Fix pattern
- Exponential backoff with jitter
- Cache responses
- Respect robots/policies where applicable

## Prevention
- Persist last successful cursor / watermark
