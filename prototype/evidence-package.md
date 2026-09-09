# PROTOTYPE — Candidate Evidence Package

**Throwaway prototype.** Not a final CV, not a polished LinkedIn profile. A concrete draft to react to, iterate on, and discard once validated decisions fold into real assets.

Branch: `prototype/evidence-package`
Date: 2026-09-09
Ticket: 07-prototype-evidence-package

---

## 1. CV — Restructured outline

### Header

```
Vincent Loupmon
Site Reliability Engineer — moving into AI Infrastructure
Aix-en-Provence, France | Open to Zurich, Berlin, EU-remote
github.com/alchimestre | vincentloupmon+pro@protonmail.com | +33 6 84 82 86 03
```

**Change from current:** Title line says "moving into AI infrastructure" instead of "GPU workloads" claim. Location line signals relocation readiness. No more "GPU workloads" in the profile sentence.

### Profile (2–3 lines)

> Production SRE with 4 years operating high-availability distributed infrastructure across regulated healthcare, crypto, and multi-protocol systems. Specializing toward AI infrastructure — bringing Kubernetes reliability, observability, and cost-aware platform operations to AI compute and serving platforms.

**Change from current:** Removes "compute-intensive and GPU workloads" claim. Adds transition framing. Leads with cross-domain transfer differentiator.

### Experience — Kiln (Jun 2024 – Jan 2026)

**Title:** Site Reliability Engineer

**Bullets (rewritten to surface architecture + cross-stakeholder evidence):**
- Operated high-availability distributed infrastructure securing $8B+ in digital assets across 40+ production networks
- Integrated 10+ distributed protocols into hybrid-cloud environments with reliability and security guarantees
- Designed and maintained Terraform IaC across multi-environment Kubernetes clusters
- Built CI/CD pipelines improving deployment safety and reproducibility
- Translated infrastructure constraints into scalable architectural decisions across engineering and product teams
- Led production hardening and cross-team risk mitigation

**Change:** Removed "GPU workloads" from this section. Added emphasis on the architecture-translation bullet (already on CV, now more prominent). No fabricated claims.

### Experience — Cometh (Feb 2023 – Oct 2023)

**Title:** Site Reliability Engineer

**Bullets:**
- Managed multi-zone Kubernetes clusters on GCP in production
- Reduced CI build times by 60% through pipeline optimization and container standardization
- Improved observability (Prometheus, Grafana, OpenTelemetry, ELK) and reduced MTTR
- Optimized infrastructure architecture, reducing cloud costs by 25%
- Led ISO 27001 security implementation and incident response processes

**Change:** Filled in the truncated "25%" cost reduction (was "2…%" in PDF extraction — **verify actual figure**). No other changes; this section is already strong.

### Experience — Docaposte (Jun 2022 – Feb 2023)

**Title:** DevOps Engineer

**Bullets:**
- Recovered and stabilized critical Kubernetes clusters in a regulated healthcare environment
- Standardized and hardened infrastructure deployed via Ansible
- Improved CI/CD reliability and deployment safety in HDS-certified systems
- Managed Linux systems and distributed storage in production

**Change:** None. This section supports the regulated-environments differentiator.

### Experience — Bitgen (Dec 2021 – Apr 2022)

**Title:** Junior DevOps Engineer

**Bullets:**
- Containerized and deployed Ethereum services on Kubernetes
- Improved security and availability of blockchain infrastructure
- Contributed to technical documentation and developer content

**Change:** None. Keep as entry-level evidence of Kubernetes + distributed systems.

### Skills section (rewritten)

**Removed:** "GPU Workloads" (evidence gap — keyword only). "Ethereum" (crypto-specific, not relevant to AI positioning).

**Current defensible skills:**
```
Kubernetes · Terraform · GCP · Linux · Docker · CI/CD · GitOps
Prometheus · Grafana · OpenTelemetry · ELK · PostgreSQL
Distributed Systems · High Availability · Scalability
Performance Tuning · Capacity Planning · Cost Optimization
SecOps · ISO 27001 · HDS
```

**Added (after training plan produces evidence, week 6+):**
```
Python (in progress) · Go (in progress, from week 7)
SLO / Error Budgets · GPU Fleet Operations (in progress)
```

Mark these as "in progress" until the GitHub artifact is live, then remove the qualifier.

### Education

Keep as-is. Epitech (2011–2012) and AFPA (2021–2022). Not a differentiator but not harmful.

---

## 2. LinkedIn — Narrative outline

### Headline

```
Site Reliability Engineer → AI Infrastructure | Kubernetes · Observability · Cost-Aware Platform Operations
```

**Rationale:** The arrow signals transition without claiming current AI expertise. Keywords match the title aliases from the positioning thesis.

### About section (3 paragraphs)

**Paragraph 1 — Identity and wedge:**
> I'm a production SRE specializing toward AI infrastructure. Over the past four years I've operated high-availability distributed systems in regulated healthcare (HDS), crypto infrastructure ($8B+ in digital assets), and multi-protocol environments — always making platforms more observable, resilient, and cost-aware. My next step is bringing that reliability discipline to AI compute and serving platforms.

**Paragraph 2 — Differentiator (cross-domain transfer):**
> I move fast across domains. From stabilizing Kubernetes in a certified healthcare environment to securing $8B+ in digital assets at Kiln, I've repeatedly entered unfamiliar infrastructure domains and reached production-grade reliability within months. I'm now applying that same pattern to AI workloads.

**Paragraph 3 — What I'm building:**
> Currently building a GPU fleet Kubernetes operator — scheduling, fleet health monitoring, and SLO/error-budget practices for AI workloads. Open to SRE and platform roles at AI-native companies in Zurich, Berlin, or EU-remote. Particularly interested in roles with architectural scope, not just operational runbooks.

**Rationale:** Paragraph 3 mentions the project as "currently building" — honest, not overstated. It signals initiative without claiming completed expertise.

### Experience entries

Mirror the CV bullets. No additional claims.

### Skills

Same as CV skills section. Add "Kubernetes," "Terraform," "Prometheus," "Grafana," "Site Reliability Engineering," "Distributed Systems" as LinkedIn skill tags (these are endorsement-generating and search-discoverable).

---

## 3. GitHub — README outline for the GPU fleet operator project

### Repo name (suggestion)

`gpu-fleet-operator` or `gpu-node-guardian`

### README structure

```markdown
# GPU Fleet Operator

A Kubernetes operator that schedules GPU workloads, monitors fleet health,
and enforces SLO/error-budget policies for AI infrastructure.

## Why

AI infrastructure teams need reliable GPU fleet operations — scheduling,
health monitoring, and automated recovery. This project demonstrates
production SRE practices applied to GPU workloads on Kubernetes.

## What it does

- Schedules GPU workloads based on resource availability and health
- Monitors GPU fleet health via DCGM metrics (NVIDIA Data Center GPU Manager)
- Cordons nodes with unhealthy GPUs and drains workloads to healthy nodes
- Defines and enforces SLOs: scheduling latency, GPU utilization, fleet-health check success rate
- Alerts on error-budget burn via Prometheus

## Architecture

[diagram placeholder — operator watches GPU node CRD, reads DCGM metrics,
makes scheduling/cordoning decisions, emits Prometheus metrics]

## Tech stack

- Phase 1: Python (Kopf framework) + Kubernetes + DCGM exporter + Prometheus
- Phase 2: Go (controller-runtime) port

## Tested against

- Cloud GPU instances (Lambda / Vast.ai / RunPod spot)
- Local kind/k3d cluster for development

## SLO definitions

| SLI | Target | Error budget |
|-----|--------|-------------|
| Scheduling latency (P99) | < 30s | 5% monthly |
| GPU utilization (fleet avg) | > 70% | 10% monthly |
| Fleet health check success rate | > 99% | 1% monthly |

## Runbook

[placeholder — alert response, node recovery, manual override procedures]

## Status

Phase 1 (Python) — in progress
Phase 2 (Go port) — planned
```

**Rationale:** The README is the single most important evidence artifact. It demonstrates: Kubernetes operator pattern, GPU fleet operations, SLO methodology, Python/Go code, observability, and the systems-thinking differentiator. It is linked from the CV and LinkedIn.

---

## 4. Outreach message templates

### 4a. Cold message to hiring manager / founder at AI-native company

```
Subject: SRE moving into AI infrastructure — [company name]

Hi [name],

I'm a production SRE with 4 years operating high-availability
distributed infrastructure (Kubernetes, Terraform, observability)
in crypto ($8B+ assets secured) and regulated healthcare.

I'm transitioning into AI infrastructure and building a GPU fleet
Kubernetes operator to close the practical gap — scheduling, DCGM-based
fleet health monitoring, and SLO/error-budget practices.

I saw [role title] at [company] and it looks like a strong fit for my
reliability background. Would you be open to a short conversation?

I'm based in France, available for remote start, and relocating to
[Zurich/Berlin] with employer support or after a remote-start period.

Best,
Vincent
```

**Rationale:** Leads with proven evidence, not aspiration. Mentions the project concretely. Addresses the relocation constraint upfront (from the pipeline diagnosis: pre-qualify before investing time). Short enough to read on mobile.

### 4b. Recruiter response (when a recruiter reaches out)

```
Hi [name],

Thanks for reaching out. Before we go further, a few quick questions
so we don't waste each other's time:

1. What's the seniority band and years-of-experience expectation?
2. What's the total compensation range for this role and location?
3. Does the role require direct GPU, training-framework, or serving-engine
   expertise on day one?
4. Is remote start from France for 8–12 weeks possible, or is relocation
   assistance provided?
5. What's the team's current AI workload stack and infrastructure maturity?

Happy to dig in if the fit is right.

Best,
Vincent
```

**Rationale:** These are the five mandatory recruiter-screen questions from ticket 05. Sending them proactively filters out mismatches before the screen, directly addressing the pipeline diagnosis failure mode.

### 4c. LinkedIn connection request (practitioner networking)

```
Hi [name],

I'm an SRE transitioning into AI infrastructure — currently building a
GPU fleet Kubernetes operator. I saw your work at [company] and would
love to connect and learn from your experience.

Vincent
```

**Rationale:** Short, honest, references the project. Does not ask for a job. Opens a channel for future referral or information.

---

## 5. What this prototype does NOT include

- A polished, formatted CV file (this is an outline, not a design)
- A completed LinkedIn profile (this is a narrative outline)
- The actual GPU fleet operator code (that's the training plan, ticket 06)
- Distributed training or serving framework claims (positioned away)
- Datacenter fabric or HPC performance claims (positioned away)
- Interview preparation materials (out of scope per map)
- Salary negotiation scripts (out of scope per map)

## 6. Open questions for Vincent to react to

1. **The transition framing ("moving into AI infrastructure")** — does this feel honest and strong, or does it undersell you?
2. **Cost reduction figure at Cometh** — the PDF extraction showed "2…%" truncated. Was it 25%? The prototype assumes 25%.
3. **The GitHub project README** — does the scope feel achievable in 6 weeks for the Python phase, or is it too ambitious?
4. **The outreach message tone** — too direct? Too cautious? Right balance?
5. **"GPU Workloads" removal from skills** — comfortable dropping this, or does it feel like losing a keyword that was generating responses?
6. **LinkedIn "About" paragraph 3** — comfortable publicly stating "currently building" a project that hasn't started yet?
