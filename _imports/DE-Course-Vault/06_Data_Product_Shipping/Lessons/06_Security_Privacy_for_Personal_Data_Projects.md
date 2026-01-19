---
type: lesson
module: Shipping
timebox_minutes: 60
status: active
prereqs: []
tags: [course/lesson, topic/security]
updated: 2026-01-18
---

# Security + privacy for personal data projects (minimum viable adulthood)

## Non-negotiables
- Keep secrets out of git (use env vars + `.env` excluded)
- Least privilege credentials (DB + object storage)
- Define retention rules (what raw data you keep, for how long)
- Avoid storing sensitive identifiers unless required

## Practical patterns
- Separate “dev” and “prod” configs
- Rotate keys when you publish a repo
- Sanitize logs (don’t log tokens/personal identifiers)

## Practice
- Add a `SECURITY.md` note (even simple)
- Add a “data retention” section in the runbook
