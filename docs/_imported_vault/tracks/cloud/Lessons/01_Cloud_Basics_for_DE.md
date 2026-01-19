---
type: lesson
created: 2026-01-18T00:00:00.000Z
tags:
  - course/cloud
id: les_cloud_basics_for_data_engineering_personal_projects
title: Cloud basics for data engineering (personal projects)
---

# Cloud basics for data engineering (personal projects)

**Mental model**
- Object storage = durable blob store (S3-like). Great for raw + artifacts.
- Managed Postgres = offload DB ops, good for “always available” projects.
- Serverless jobs = run containers on demand + schedule, pay per use.

**Free-tier reality (read the provider docs)**
- AWS has an AWS Free Tier / free plan model; watch billing and eligibility. citeturn0search1turn0search5
- Google Cloud offers a free trial and a free tier; Cloud Run has a documented free tier of CPU/RAM seconds. citeturn0search2turn0search6turn0search10
- Cloudflare R2 has a published free tier for storage/operations. citeturn0search19
- Supabase publishes a free plan with defined limits (DB size/storage and inactivity behavior). citeturn0search3
- Neon publishes a free plan and plan details in their docs. citeturn1search0turn1search17

**Project vibe (recommended)**
Start with “Cloud Mirror” first: cheapest and teaches the right habits.
