---
type: lab
created: 2026-01-18
timebox_minutes: 180
tags: [course/cloud, course/lab, topic/iac]
---

# Lab E — IaC Lite: minimal stack

## Outcome
Provision a minimal cloud setup via IaC:
- a bucket (object storage) OR a simple static hosting target
- (optional) a scheduled job container target, depending on provider

## Constraints (keep it sane)
- 1 environment: `dev`
- 1 region
- destroyable in one command

## Steps (provider-agnostic)
1) Create an `infra/` folder in your capstone repo
2) Write IaC config for:
   - object storage bucket
   - outputs: bucket name, region, endpoint
3) Store state safely (for personal projects: local state is fine, but treat it as sensitive)
4) Run:
   - plan
   - apply
   - destroy (to prove teardown works)

## Evidence
- Paste plan output snippet (what resources)
- Paste apply output (created resources)
- Paste destroy output (removed resources)
- Commit hash

## Maps to gates
- Supports G7 (fresh bootstrap), and de-risks cloud costs.
