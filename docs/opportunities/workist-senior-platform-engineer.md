# Workist — Senior Platform Engineer (f/m/x)

**Posting:** https://www.linkedin.com/jobs/view/4471439954/ · Berlin (remote-flexible; 4 weeks/year abroad)
**Org:** Workist — Berlin-based AI scale-up, founded 2019; AI Agents for inside-sales teams in manufacturing/wholesale; 200+ business customers
**Market:** DE (Berlin) · **Tier:** **A** — first Tier A role in the pipeline · **Channel:** ATS (LinkedIn)
**Applied:** ✅ 2026-09-26 (LinkedIn) · **Comp band (employer-disclosed): €80,000–100,000 base**
**Stage:** **Closed** 2026-10-06 (refused, no reason given, pre-screen)
**Follow-ups:** **none sent, none owed** — the refusal arrived the day after the first window opened (2026-10-05)

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

- Stage reached: **closed at Contacted, never screened** (LinkedIn ATS application 2026-09-26 → refusal
  reported 2026-10-06; **exact refusal date not captured**)
- Board Stage: **Closed** (set 2026-10-06)
- Rejection reason: **`unknown`** — no reason given
- Duration: ~7 business days application → refusal, pre-screen. Slower than the n8n triage refusals (≤2 days)
  and in the same range as Langdock (~7 days): a role that was actually looked at
- Follow-ups: **none sent, none owed** — the first follow-up was due 2026-10-05 and the refusal arrived the
  next day
- **Outreach was never sent, and this was the one draft that could have been sent as written.**
  `docs/outreach/workist-senior-platform-engineer.md` — the only draft addressed to a **named recipient**
  (Fabian Brosig, CTO, the person this role reports to) — stayed marked NOT SENT, and `docs/outreach/sent/`
  remains empty. The refusal therefore rests on the cold LinkedIn ATS application alone
- Feedback request: **not sent** — §3 gates it on a recruiter screen, which this never reached
- **What was lost, recorded in full:** the strongest application in the pipeline on every axis — **Tier A**
  (the JD named the platform AI workloads run on: Kubernetes for ML workloads, LLM gateway with region
  failover, GPU capacity planning), **employer-disclosed band €80,000–100,000 clearing the floor**, the
  closest seniority match, and the closest role shape (quarterly-theme ownership, reports to the CTO).
  It is the pipeline's **last remaining Tier A** role
- **What the refusal does and does not say.** A pre-screen silence with no reason tells us nothing about the
  fit; it cannot be attributed to the two honest gaps (GCP-first cloud depth, Python read-and-debug rather
  than author). Recording either as the cause would be a prediction, not a fact
- **What would have changed the outcome:** an outreach message reaching the CTO before the ATS queue. The
  material to do it existed since 2026-09-29 and was never used
- Next action: **closed.** No further contact, no re-application

## Funnel delta

Applications sent +1 (2026-09-26, DE lane). **Primary-lane (Tier A) — exits as a pre-screen refusal with
`reason:unknown`.** With this closure the pipeline holds **no open Tier A role**; #9 SAP Fioneer (Tier B) is
the last open primary-lane application, and #13 Bubblemaps (Tier C, recruiter lane) the only live process.
