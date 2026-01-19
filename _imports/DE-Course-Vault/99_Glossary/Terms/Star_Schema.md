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

    # Star Schema

    ## Definition
    A modeling pattern with **fact tables** (events/measurements) connected to **dimension tables** (descriptive attributes).

    ## Why it matters
    It keeps analytics fast and understandable: you can slice facts by dimensions without reinventing joins every time.

    ## Examples
    - `fact_sales` joined to `dim_customer`, `dim_product`, `dim_date`.
- Facts are usually numeric; dims are descriptive and relatively stable.

    ## Practical tips
    - Ensure dimension keys are unique (or SCD2 if historized).
- Document relationships in dbt docs.
