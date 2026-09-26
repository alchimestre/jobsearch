# Workist — Senior Platform Engineer (f/m/x)

**Posting:** https://www.linkedin.com/jobs/view/4471439954/ · Berlin (remote-flexible; 4 weeks/year abroad)
**Org:** Workist — Berlin-based AI scale-up, founded 2019; AI Agents for inside-sales teams in manufacturing/wholesale; 200+ business customers
**Market:** DE (Berlin) · **Tier:** **A** — first Tier A role in the pipeline · **Channel:** ATS (LinkedIn)
**Applied:** ✅ 2026-09-26 (LinkedIn) · **Comp band (employer-disclosed): €80,000–100,000 base**
**Follow-up 1 due:** 2026-10-05 · **Follow-up 2 due:** 2026-10-14 (final)

## Why this is Tier A

The JD states the §2 ML requirement almost verbatim:

> "As Senior Platform Engineer, you own the platform that **Workist's AI agents run on**: two clouds, the
> **Kubernetes clusters for production, staging and ML workloads**, and the path from merge request to
> production for every service we ship."

And the entry wedge is named directly:

> "Most recently that meant an **LLM gateway with region failover** in front of our Azure OpenAI deployments,
> and performing **GPU capacity planning** for our own models."

That is ownership of the platform AI workloads run on — §2 Tier A, not Tier B. The MLOps sub-filter also
holds: this is the **platform/infrastructure side** (own the substrate), not data-pipeline authoring.

## Strongest hard-filter profile in the pipeline

| Filter | Result |
|---|---|
| Not Staff/Principal | ✅ Senior band, "run production infrastructure for years", no years figure |
| Comp ≥ €80k | ✅ **PASS, employer-disclosed €80–100k** — clears the floor at the bottom of the band |
| Remote-start / relocation | ⚠️ Berlin-based, remote-flexible, 4 weeks/year abroad. No relocation mention → **ask at screen** |
| No day-one GPU/training/serving | ⚠️ **partial** — "GPU capacity planning" and "LLM gateway" are named as the role's work, not as a prior-specialist gate |
| AI exposure AND architectural scope | ✅ **PASS — Tier A** |

## Stack overlap

`Kubernetes (AKS)` · `Helm` · `GitOps/Flux` · `Terraform via CI` · `GitLab CI` · `Azure + AWS` ·
`Postgres/OpenSearch/Redis` · `Python`.

Flux is in the **deployed-at-Kiln** evidence list (not merely used). Terraform, Helm, Prometheus/Grafana
observability, cost optimisation, patch management, pentest-finding remediation, DR testing and
least-privilege design all map directly onto stated responsibilities.

The three "what this looked like recently" anecdotes — a Redis instance silently dropping half its TCP
connections and taking Celery workers down; region failover and load balancing for Azure OpenAI; migrating
clusters from nginx ingress to the Kubernetes Gateway API — are all shapes the candidate can discuss from
production experience.

## The two honest gaps

1. **Azure.** Evidence is GCP-first, AWS-adjacent. The JD allows this explicitly: *"an AWS background works
   if you are willing to go deep on Azure."* State it plainly; do not overclaim.
2. **"Active Python skills: you read and debug a Python codebase and fix the application when the
   application is what is broken."** Python is operational scripting only today; `ml-platform-on-k8s` is
   closing this but is pre-week-6. It is "read and debug", not "author production services" — a screen
   question, not a hard gate.

## Role shape

> "You set your own roadmap. Infrastructure at Workist is run as quarterly themes that you propose, make
> the case for and deliver… You report to our **CTO** and are the voice of the platform in engineering
> decisions."

Senior-with-autonomy rather than senior-as-senior-IC — matches the role-selection criterion (architectural
scope, cross-stakeholder communication) better than any other role logged today.

## Recruiter-screen answers (ask before any screen)

1. Azure expectation — workable from an AWS/GCP background, and how much Azure ramp is expected?
2. Remote-start shape: could the first 8–12 weeks be worked from France, with relocation to Berlin after?
3. What do "ML workloads" mean on their clusters today — self-hosted models, GPU nodes, or managed endpoints?
4. Is Python debugging gated at interview, and at what depth?
5. On-call model and team size?

## Timeline

- Contacted / applied: **2026-09-26** (LinkedIn ATS)
- Follow-up 1 due (5–7 business days): **2026-10-05**
- Follow-up 2 due (10–14 business days): **2026-10-14** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- Watch: ~67 applicants within the first day of posting. Apply timing was good.
- What would have changed the outcome: —
- Note: this is the **strongest application in the pipeline** — Tier A, disclosed band clearing the floor,
  AI-exposure filter cleared on the strong side, and the closest seniority match. Prioritise any response
  from Workist above the Tier C cohort.
