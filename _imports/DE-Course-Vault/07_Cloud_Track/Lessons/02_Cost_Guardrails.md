---
type: lesson
created: 2026-01-18
tags: [course/cloud]
---

# Cost guardrails (avoid surprise bills)

## Default rules
- Prefer **object storage + static sites** over always-on servers.
- Put a hard cap on your project: “I will not spend more than $X/month.”
- Delete unused resources weekly (artifacts/old containers).

## Concrete guardrails
- Use provider billing dashboards and set alerts/limits when available.
- Keep compute scheduled (daily) rather than continuous.
- Keep datasets small while learning; scale later.

## Practical note
Some platforms do not provide a permanent free tier; treat any “trial credit” as finite. citeturn1search6turn1search1
