# Redcare Pharmacy — Platform Engineer (m/f/d), Köln — Data & AI department

**Posting:** https://www.linkedin.com/jobs/view/4449523926/ (LinkedIn job id `4449523926`, posted ~3 weeks
before reading, "be among the first 25 applicants")
**Org:** **Redcare Pharmacy** — *"Europe's No.1 e-pharmacy"* (the Shop Apotheke Europe group; NL-listed). Large,
established, regulated healthcare e-commerce. **Köln** office.
**Market:** **DE** · **Tier:** **B** (lower end — see the note) · **Channel:** ATS (LinkedIn) · **Track:** `ai`
**Team:** platform team **inside the Data & AI department**, building the *"next-generation AI Platform"* —
the foundations that let teams *"develop, deploy, govern, monitor, and scale AI systems safely and reliably"*.
**Applied:** ✅ **2026-10-09** · **Stage:** Contacted · **Issue:** #37
**Compensation:** **not published.** DE floor **€80,000** (§2). ⚠️ The JD's seniority language reads **mid-level**
(*"implementing agreed solutions with support from more experienced engineers when needed"*, *"resolve standard
support cases"*), which is the profile that can sit **below the floor** `[INFERENCE — no band data]`.
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**
**jobradar:** no store row; Redcare is **not** a tracked board.

## Hard-filter checklist (§2)

- [ ] Not Staff/Principal / seniority — ⚠️ **passes the letter, fails the spirit.** It is not Staff/Principal, but
      the role is written **mid-level**: component ownership under more experienced engineers, standard support
      cases, escalation paths. Applying ~4 years of production ownership to a role framed one step below it
- [ ] Compensation ≥ €80k (DE) — ⚠️ **unverified**, not published, and the mid-level framing makes a sub-€80k
      band plausible. A large listed employer should pay properly, but that is not evidence
- [ ] On-site DE with 8–12 week remote start / relocation — ⚠️ **likely fails, and this is the second
      residency-gated role today.** The benefits state *"work from home … individually — even for **up to 20
      days a year anywhere in the EU**"*. A 20-day annual EU allowance **implies German residency** for the rest
      of the calendar, i.e. relocation, and **no relocation assistance is mentioned**. Unverified but the
      inference is strong
- [x] No day-one GPU / training / serving requirement — ✅ no GPU or serving ownership in the JD
- [x] AI workload exposure AND architectural scope — ✅ genuine: the Kubernetes and Databricks platform the
      Data/AI/MLOps teams run on, plus self-service capabilities and design discussions

**Verdict: admissible but the weakest fit of the eight logged today — the AI-platform *surface* is right and the
*platform* is wrong.** Azure and Databricks are the core of the job and neither is in the evidence base, the
seniority is a step down, and the location is probably gated to German residency.

## Tier note

**Tier B, lower end.** The surface is genuinely the primary lane — a platform team inside a **Data & AI
department**, building AI-platform foundations for Data/AI/MLOps teams, on Kubernetes and Databricks. But
ownership is **component-level** (*"take ownership of platform components and improvements"*, *"with support
from more experienced engineers when needed"*) rather than platform-level, and the employer is not AI-native.
Recorded so the label stays auditable.

## Craft read

| JD requirement | Candidate evidence |
|---|---|
| **Hands-on Microsoft Azure** — compute, networking, storage, identity, security | ❌ **the core gap.** **No Azure row exists anywhere in `docs/tooling-inventory.md`.** Cloud depth is GCP (multi-zone Cometh) plus hybrid/on-prem. Cloud-native concepts transfer, but Azure is the platform this team runs on, not a bonus |
| **Azure Databricks** platform: configuration, automation, monitoring, access management, troubleshooting | ❌ not evidenced ❌. The JD accepts *"or a strong motivation to develop hands-on expertise"* — the honest answer is motivation plus the ML-platform project (`docs/ml-platform-project.md`), which is designed for exactly this surface |
| **Azure Kubernetes** platform, deployments via **GitOps and CI/CD** | ✅✅ Kubernetes at multi-zone and bare-metal scale, GitOps with **Flux** (`deployed`) and Argo CD, Drone CI `deployed`, GitHub Actions — strong, with ⚠️ AKS specifically unproven |
| **Terraform** IaC; Helm an advantage | ✅✅ Terraform/Terragrunt multi-environment; Helm on the skills inventory |
| Containers and how containerised workloads are deployed and operated | ✅✅ Docker, Kubernetes, GitOps delivery |
| Logging, monitoring, troubleshooting production/platform environments; resolve common operational issues independently | ✅✅ Prometheus/Thanos, Grafana, Loki, ELK, Jaeger, Alertmanager, Datadog; production incident response |
| **Programming/scripting language (Python, Go, or Shell) for infrastructure automation and platform tooling** | ✅ **this is the permitted form of the scripting claim.** The evidence boundary excludes *production software authorship*, not automation tooling — and "for infrastructure automation and platform tooling" is precisely what is evidenced. Shell, CI/CD glue, operational scripting |
| **Basic understanding of Data, ML, or AI workloads and how infrastructure supports them** | ✅✅ **the strongest single requirement match**: the entire positioning thesis is ML-platform/MLOps, plus the in-progress `ml-platform-on-k8s` project |
| Self-service and reusable automation for engineering/Data/AI teams | ✅ platform tooling, GitOps self-service patterns, cross-team platform work |
| Regulated environment (implied: pharmacy, health data) | ✅ Docaposte **HDS-certified health-data infrastructure**, ISO 27001 lead — an e-pharmacy handling health data is adjacent to this |
| English fluent; German a plus | ✅ |
| Collaborate across Platform, Data, AI, MLOps, Security | ✅ cross-team architecture translation |

## Risks, stated plainly

1. **Azure is the platform, not a bonus.** Everything in the first bullet requires hands-on Azure, and the
   Databricks platform work sits on top of it. This is the least-bridgeable gap in the JD — it will decide the
   screen on its own.
2. **Seniority is a step down.** *"Implementing agreed solutions with support from more experienced engineers
   when needed"* is not the role the CV is built for, and taking it would trade ownership for surface.
3. **Location is probably gated.** The *"up to 20 days a year anywhere in the EU"* benefit reads as a cap on
   the existing remote policy rather than a remote-first setup, and no relocation support is mentioned.
4. **Compensation unpublished**, with a mid-level frame that could put the band under the floor.
5. **Second residency-gated role in a row** (after #36 MAIA) — see the pattern note below.

## What is genuinely attractive

- **The surface is the primary lane**: a platform team inside a Data & AI department, building the foundations
  that let AI teams *"develop, deploy, govern, monitor, and scale"*. Of the eight roles logged today, this and
  #32 Runware are the two whose subject is AI-platform operation rather than AI-adjacent platform work.
- **"Programming/scripting … for infrastructure automation and platform tooling"** is the one form of the
  programming requirement that the evidence supports cleanly — worth noting for future applications, where
  "software engineering" is usually the gate.
- **The ML-workload understanding requirement is the CV's thesis verbatim**, and the JD accepts motivation
  instead of depth on Databricks.
- Large, established, regulated employer — stable income, and health-data compliance experience transfers.

## Questions to put in writing (first follow-up)

1. **Salary band** for the role?
2. **Is German residency required**, or could the role be performed from France — and is relocation support
   available if not?
3. How much of the work is Azure platform generalism versus Databricks/ML-platform specifics?
4. Is the role scoped as mid-level, and is there a senior variant in the same team?
5. What is the on-call arrangement for the Data & AI platform?

## ⚠️ Pattern note — the German lane is producing residency-gated roles

Two consecutive applications (#36 MAIA, #37 Redcare) fail or probably fail on **residency in Germany**, not on
capability. Combined with the earlier rows (#29 idnow: Berlin on-site, no relocation mentioned; #30 Atlantic:
Berlin on-site five days a week, no relocation mentioned), the **DE lane is structurally harder to convert from
France than the FR/EU-remote lane**, because a large share of German postings assume residency without funding a
move. The lane allocation (Berlin 35%) was set on demand density, not on convertibility. **This is a Friday
review item**: either the DE lane needs a relocation-funding filter applied *before* applying, or the allocation
should shift toward EU-remote/FR until relocation funding is secured.

## Timeline

- Contacted / applied: **2026-10-09** (LinkedIn)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Salary: not stated in the application
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** with no band published and a probable residency gate, this is a row where **silence carries no
  information** — it joins the `unknown` pile. The lesson is upstream: both unknowns were answerable **before
  applying** (ask for the band; ask whether France is eligible), which is exactly what the 2026-10-09 rule now
  requires.
- What would have changed the outcome: a published band clearing €80k; a France-eligible contract; a
  senior-scoped variant

## Funnel delta

Applications sent +1 (2026-10-09) · **DE lane** · `tier:b` · `track:ai`. Eighth application logged today and the
second consecutive one whose binding constraint is German residency.
