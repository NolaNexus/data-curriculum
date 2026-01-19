---
type: debug-pattern
tags: [course/troubleshooting, topic/ingestion]
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
