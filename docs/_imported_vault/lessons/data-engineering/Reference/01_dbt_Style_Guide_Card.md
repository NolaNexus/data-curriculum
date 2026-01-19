---
type: reference
status: active
created: 2026-01-19T00:00:00.000Z
tags:
  - course/reference
id: doc_dbt_style_guide_card_practical_defaults
title: dbt style guide card (practical defaults)
---

# dbt style guide card (practical defaults)

Use this as your project’s “house rules” until you choose something else.

## Naming
- Models plural (`customers`, `orders`)
- Primary key named `<object>_id`
- Booleans: `is_` / `has_`
- Timestamps: `<event>_at` (UTC)

## Layering
- `stg_<source>__<table>` for staging models
- marts are facts/dims at explicit grain

## Workflow
- Codify naming + conventions early
- Prefer readability over clever abbreviations
