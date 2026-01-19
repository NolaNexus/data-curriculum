---
type: lesson
created: 2026-01-18T00:00:00.000Z
tags:
  - course/cloud
id: les_serverless_jobs_and_scheduling
title: Serverless jobs and scheduling
---

# Serverless jobs and scheduling

## Why
- Runs your pipeline in a clean environment (like a fresh machine every time)
- Easy scheduling
- Pay-per-use

## Path A (recommended for personal projects)
- Google Cloud Run Jobs / Cloud Run services + schedule externally
  - Cloud Run has documented free-tier compute seconds. citeturn0search6turn0search14

## Path B
- AWS Lambda for small tasks; container-based runs may use other AWS services
  - Lambda free tier details are documented. citeturn0search9

Start with a containerized pipeline that can run headless with env vars.
