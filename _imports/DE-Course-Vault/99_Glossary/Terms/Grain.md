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

    # Grain

    ## Definition
    Grain is what **one row represents** in a dataset or model.

    ## Why it matters
    If you don’t state grain, joins and aggregations will lie to you.

    ## Examples
    - A `fact_orders` table with grain = **one row per order**.
- A `fact_order_items` table with grain = **one row per (order_id, item_id)**.

    ## Practical tips
    - Write grain at the top of dbt models and metric definitions.
- Test uniqueness on the grain keys.
