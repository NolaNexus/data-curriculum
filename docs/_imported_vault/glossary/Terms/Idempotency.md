---
type: glossary
status: active
created: 2026-01-19T00:00:00.000Z
tags:
  - course/glossary
id: doc_idempotency
title: Idempotency
---

    ---
    type: glossary
    updated: 2026-01-18
    tags: [course/glossary]
    ---

    # Idempotency

    ## Definition
    An idempotent pipeline can be run multiple times with the same inputs and produce the **same result**.

    ## Why it matters
    This is the difference between a pipeline you trust and a pipeline that duplicates data quietly.

    ## Examples
    - Using `MERGE`/upsert keyed by a natural key.
- Overwriting a partition for a specific date range.

    ## Practical tips
    - Prove idempotency with checksums/row counts across reruns.
- Make backfills explicit and test them.
