---
type: gate
gate_id: G5
status: not_started
last_run: null
evidence_links: []
tags:
  - course/gates
id: gate_g5_publish_metrics_dashboard
title: G5 — Publish + Metrics + Dashboard
---

# G5 — Publish + Metrics + Dashboard

## Why this gate exists
Proves you can produce a useful output and define meaning.

## Pass criteria (must all be true)
- [ ] At least one published output exists: dashboard or static report or API
- [ ] Each metric has a definition note (grain, filters, window)
- [ ] Dashboard tiles link back to metric definitions

## Evidence required
- [ ] Screenshot/URL of output
- [ ] Link to metric definition notes
- [ ] Query that matches the metric

## Common failure modes
- Metrics undefined (dashboard lies)
- Aggregations mismatch grain
- No documentation of filters

## Next step (smallest move)
- Publish one chart and one metric definition.
