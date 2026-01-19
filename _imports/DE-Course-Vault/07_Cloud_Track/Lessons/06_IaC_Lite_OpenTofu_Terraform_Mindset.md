---
type: lesson
created: 2026-01-18
tags: [course/cloud, topic/iac]
---

# IaC Lite (OpenTofu/Terraform mindset)

IaC (Infrastructure as Code) means your cloud resources are created from code, not clicking around in a UI.
For personal projects, “lite” means:
- small number of resources
- one environment first
- reproducible apply/destroy

## Why it belongs in this course
- Reproducibility: you can rebuild after mistakes
- Reviewability: changes are visible in git
- Portability: move providers or regions more easily

## Minimal workflow
1) Define resources in code
2) `plan` (see what will change)
3) `apply` (create/update)
4) `destroy` (tear down to stop costs)

## Safety rule
Always keep a “destroy path” documented. Bills are sneaky.

## Practice
Lab: [[07_Cloud_Track/Labs/Lab_E_IaC_Lite_Minimal_Stack]]
