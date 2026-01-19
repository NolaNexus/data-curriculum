---
type: runbook
created: 2026-01-18
tags: [course/cloud, topic/cost]
---

# Cloud cleanup runbook (weekly)

## Checklist
- [ ] Remove unused container images
- [ ] Delete old build artifacts
- [ ] Verify schedules are only what you intend
- [ ] Confirm no stray databases/disks exist
- [ ] Confirm credentials are least-privilege

## Evidence
Log a weekly cost/cleanup note in `11_Logbook/Cloud_Cost_Checks/`.
