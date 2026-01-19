---
type: glossary
status: active
created: 2026-01-19
tags: [course/glossary]
---

    ---
    type: glossary
    updated: 2026-01-18
    tags: [course/glossary]
    ---

    # Freshness Check

    ## Definition
    A test that verifies data is **recent enough** for its intended use (e.g., updated daily).

    ## Why it matters
    Freshness catches silent pipeline failures where the system ‘runs’ but outputs stop updating.

    ## Examples
    - `events` table must have data in the last 24 hours.
- API ingest must have a successful run today.

    ## Practical tips
    - Record `fetched_at_utc` and use it for freshness assertions.
- Add alerting for failed schedules or freshness failures.
