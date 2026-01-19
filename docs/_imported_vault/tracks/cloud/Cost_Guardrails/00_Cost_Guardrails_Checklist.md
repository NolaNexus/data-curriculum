---
type: checklist
created: 2026-01-18T00:00:00.000Z
tags:
  - course/cloud
  - topic/cost
id: doc_cost_guardrails_checklist_personal_projects
title: Cost guardrails checklist (personal projects)
---

# Cost guardrails checklist (personal projects)

## Hard rules
- [ ] Set a monthly cap: $____ (even if it’s $0)
- [ ] Prefer scheduled jobs over always-on services
- [ ] Tear down resources you aren’t actively using
- [ ] Store big artifacts in object storage, not attached disks

## Daily / Weekly cadence
- [ ] Do a quick “cost check” 2–3x/week (log it)
- [ ] Weekly cleanup: delete unused images/artifacts, stop services
- [ ] Monthly review: what was worth it?

## Lifecycle / retention (reduce storage creep)
- [ ] Raw data retention policy exists
- [ ] Artifact retention policy exists
- [ ] Logs retention policy exists

## Incident readiness
- [ ] If a bill spikes, I have a plan:
  - disable schedules
  - destroy non-essential resources
  - rotate keys if leaked
