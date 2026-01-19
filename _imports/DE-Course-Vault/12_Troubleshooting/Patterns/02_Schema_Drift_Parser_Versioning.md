---
type: debug-pattern
tags: [course/troubleshooting, topic/ingestion]
---

# Schema drift: parser versioning

## Symptom
Ingestion suddenly fails or columns shift.

## Fix pattern
- Keep raw payload immutable
- Version your parser
- Emit metadata: parser_version + schema_hash

## Prevention
- Add schema validation step (pydantic/jsonschema)
