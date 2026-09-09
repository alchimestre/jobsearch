# Integrated 12-Week AI Infrastructure Job Search Strategy

**Status:** Approved 2026-09-09 by Vincent. This is the operating plan for execution. Source: branch `prototype/integrated-strategy` at commit `d2fd804` (wayfinder ticket 10). It integrates decision tickets 01–09; it plans execution and does not itself execute applications, outreach, coursework, or profile changes.

## 1. Objective and constraints

**Objective:** Generate qualified interviews for mid-to-senior AI Infrastructure Engineer, AI/ML Platform, and SRE-on-AI-platform roles while producing credible evidence for the largest hiring gaps.

**Primary markets:** Switzerland 60% / Berlin 40% of active search effort.

**Available time:** Approximately 35 hours per week for 12 weeks.

**Positioning:** Production SRE moving into AI infrastructure. Lead with Kubernetes, production reliability, distributed systems, observability, cost optimization, security-hardened environments, and infrastructure-to-architecture translation. Do not claim direct production ownership of GPU fleets, training systems, serving systems, Python/Go software, SLO/error-budget programs, or datacenter fabrics before evidence exists.

**Relocation constraint:** No relocation savings. Any on-site Switzerland or Berlin role must support an 8–12 week remote start from France or provide relocation assistance.

**Hardware constraint:** MacBook Air M4; no local NVIDIA GPU. Use local kind/k3d for development and approximately $5–20 of cloud GPU time for real DCGM and workload validation.

## 2. Role admission and ranking

### Admit

1. **Tier A:** Direct ownership of AI workload infrastructure: compute, scheduling, serving, training platform, or AI observability.
2. **Tier B:** SRE/platform role at an AI-native company, even without direct AI-infrastructure ownership.
3. **Tier C:** Non-AI SRE/platform bridge role only when it offers architectural scope, strong compensation, and a credible path to AI exposure or relocation.

### Reject before investing in a process

- Generic SRE/DevOps runbook roles without AI exposure or architectural scope.
- Crypto-continuity roles that do not strengthen AI-infrastructure positioning.
- Staff/Principal roles or roles asking 8+ years.
- Total compensation below CHF 110k in Switzerland, €80k in Berlin, or €70k for a France/EU-remote bridge.
- On-site Switzerland/Berlin roles without relocation assistance or an 8–12 week remote start.
- Roles requiring direct GPU, distributed-training, or serving-engine expertise on day one.

### Rank admitted roles

AI-infrastructure depth; architectural scope; 3–6 year seniority match; relocation feasibility; compensation; English-first environment; strategic bridge value. Company stage is not a filter.

### Search titles

`AI Infrastructure Engineer`, `AI/ML Platform Engineer`, `GPU Platform Engineer`, `SRE — ML/Inference`, `Reliability Engineer — AI/ML`, `Training Platform Engineer`, `Inference Platform Engineer`, and `HPC/AI Platform Engineer`. Responsibilities override title.

## 3. Search channels and baseline throughput

Channel percentages apply to active search time. Switzerland receives 60% of each week's target list; Berlin receives 40%.

- **60% hiring-manager/founder outreach:** Switzerland email-first; Berlin LinkedIn-first. Use the validated transition message from the evidence-package prototype.
- **25% targeted ATS applications:** Only roles passing every hard filter.
- **10% recruiter relationships:** Pre-qualify inbound contacts; proactively cultivate 3–5 in-house AI-infrastructure recruiting or talent contacts across target employers in both markets. External agency recruiters remain inbound/opportunistic only.
- **5% public evidence and channel follow-up:** Link the project from CV, LinkedIn, and outreach as soon as the first meaningful commit exists.

**Steady-state weekly throughput target from week 3:**

- 6–10 personalized hiring-manager/founder messages.
- 2–4 filtered ATS applications.
- 1–2 new or maintained in-house recruiter relationships.
- All due follow-ups sent.

These are quality floors, not volume goals. Never lower the admission criteria to hit them. If too few admissible roles exist, spend the unused search time on target research or the evidence project.

### Mandatory questions before a recruiter screen

1. Does the role require direct GPU, training-framework, or serving-engine expertise on day one?
2. What is the seniority band and expected experience?
3. What is the total compensation range?
4. Is an 8–12 week remote start from France possible, or is relocation assistance provided?
5. What is the team's current AI workload stack and infrastructure maturity?

### Follow-up sequence

- First follow-up: 5–7 business days after initial outreach.
- Second and final follow-up: 10–14 business days after initial outreach.
- After a recruiter-screen rejection: one request for specific feedback on relevance, readiness, compensation, or location mismatch.

No mass job-board applications. Agency recruiters, networking events, and unrelated open-source work remain opportunistic rather than primary channels.

## 4. Evidence project

One repository: `gpu-fleet-operator`.

### Phase 1 evidence — Python

- Kubernetes operator built with Python/Kopf or equivalent.
- GPU workload scheduling based on resource and health state.
- DCGM metric ingestion against a real cloud NVIDIA GPU.
- Node cordoning and workload draining for unhealthy GPU state.
- Prometheus metrics and alerts.
- SLIs for scheduling latency, fleet-health check success, and GPU utilization.
- Error-budget policy and operational runbook.
- Architecture and design-decision documentation.

### Phase 2 evidence — Go

Port the operator to Go/controller-runtime. Preserve the observable contract, improve scheduling or reconciliation logic, and document why the production-oriented implementation differs from the Python prototype.

### Positioned-away gaps

Spend approximately four hours each across the 12 weeks on conceptual study only:

- Distributed training/serving: data and model parallelism, FSDP, Ray/Slurm basics.
- Datacenter fabric/HPC: InfiniBand, RDMA, NCCL basics.

Do not add these as CV claims or create separate portfolio artifacts.

## 5. Weekly operating plan

### Week 1 — Make the search legible; establish the project

**Allocation:** 7h search/assets, 24.5h training, 3.5h pipeline management.

- Apply the approved CV restructure: transition title, defensible profile, 25% Cometh cost reduction, and `GPU exposure` rather than `GPU Workloads`.
- Apply the approved LinkedIn headline and About narrative. State that the operator is currently being built.
- Create the pipeline tracker and initial Switzerland/Berlin target list using the 60/40 split.
- Create the `gpu-fleet-operator` repository, README, architecture skeleton, local kind/k3d environment, and Python/Kopf operator scaffold.
- Define the operator's custom resource and reconciliation contract.

**Exit check:** Search assets tell one consistent story; tracker exists; the operator reconciles a minimal custom resource locally.

### Week 2 — Start outreach; implement scheduling state

**Allocation:** 7h search, 24.5h training, 3.5h management.

- Begin email-first Swiss and LinkedIn-first Berlin outreach.
- Submit only high-confidence ATS applications; contact relevant in-house recruiters.
- Publish the first meaningful project commit and link it from the search assets.
- Implement GPU-node discovery using labels/resources, workload admission, desired scheduling state, and simulated health metrics locally.
- Define the three SLIs and how each is measured.

**Exit check:** First outreach cohort sent; project link is public; scheduling decisions are observable locally.

### Week 3 — Reach steady-state search; prove local control loop

**Allocation:** 15.75h search, 15.75h training, 3.5h management.

- Reach the steady-state throughput targets while preserving 60/40 market allocation.
- Send first due follow-ups.
- Complete a local end-to-end path: health input → reconciliation decision → cordon/drain action or safe simulated equivalent.
- Export Prometheus operator metrics.

**Exit check:** Basic Python operator runs on kind/k3d; every pipeline entry has source, tier, market, status, next action, and due date.

### Week 4 — Validate against a real GPU; establish error-budget mechanics

**Allocation:** 15.75h search, 15.75h training, 3.5h management.

- Continue steady-state outreach, applications, recruiter work, and follow-ups.
- Rent a cloud NVIDIA GPU only for a bounded validation session.
- Ingest real DCGM metrics and run a real GPU workload.
- Implement Prometheus alert rules and error-budget burn calculations.
- Begin distributed-training conceptual study.

**Checkpoint:** Calculate outreach response rate over weeks 2–4. If below 10%, change either targeting or messaging—not both—and label the changed cohort.

### Week 5 — Exercise failure recovery; diagnose qualification

**Allocation:** 15.75h search, 15.75h training, 3.5h management.

- Continue search at steady state with the selected week-4 adjustment, if any.
- Exercise unhealthy-GPU handling, idempotent reconciliation, cordoning, draining, and recovery.
- Draft the operational runbook and record cloud validation evidence without implying production-scale ownership.
- Begin datacenter-fabric conceptual study.

**Checkpoint:** If screen-to-rejection remains above 75% after four active weeks, classify every rejection as relevance, readiness, compensation, location, or unknown. Narrow the responsible role band or strengthen the relevant pre-qualification question.

### Week 6 — Ship the complete Python evidence package

**Allocation:** 15.75h search, 15.75h training, 3.5h management.

- Complete the Python operator, DCGM validation, metrics, alerts, SLI definitions, error-budget policy, runbook, architecture diagram, and reproducible setup instructions.
- Replace `in progress` with completed Python/GPU/SLO evidence in search assets only where the repository proves the claim.
- Use the completed artifact in new outreach and appropriate follow-ups.

**Checkpoint:** If no technical interview has been reached, pause new ATS applications for week 7. Audit the full funnel and compare pre-artifact versus post-artifact cohorts. Do not pause direct conversations already in progress.

**Exit check:** A reviewer can clone the repository, understand the architecture, run the local path, and see evidence from bounded real-GPU validation.

### Week 7 — Start Go port; perform the midpoint funnel audit

**Allocation:** 17.5h search, 14h training, 3.5h management.

- If the zero-interview trigger fired, use ATS time for the funnel audit; keep qualified outreach and active conversations moving.
- Scaffold Go/controller-runtime implementation and reproduce the custom-resource contract.
- Review market conversion separately for Switzerland and Berlin; do not pool the results.
- Finish any remaining distributed-training conceptual study.

**Exit check:** Root qualification cause is named if the trigger fired; Go controller builds and handles a minimal reconciliation path.

### Week 8 — Port the core control loop

**Allocation:** 17.5h search, 14h training, 3.5h management.

- Resume or continue filtered ATS applications based on the week-7 audit.
- Port scheduling, health-state evaluation, and idempotent reconciliation to Go.
- Continue full follow-up sequence and recruiter cultivation.
- Finish any remaining fabric/HPC conceptual study.

**Exit check:** Go implementation makes the same core scheduling and health decisions as the Python implementation.

### Week 9 — Run the Go operator end to end

**Allocation:** 17.5h search, 14h training, 3.5h management.

- Run the Go operator locally end to end with metrics and simulated failure states.
- Document differences between the Python prototype and Go implementation.
- Refresh outreach links to point at the clearest evidence entry point.

**Exit check:** Basic Go operator compiles and runs; architecture documentation explains both phases.

### Week 10 — Deepen Go behavior; increase search emphasis

**Allocation:** 19.25h search, 12.25h training, 3.5h management.

- Increase search emphasis without weakening filters.
- Port or improve cordon/drain recovery and Prometheus instrumentation.
- Review compensation mismatches by market. If they exceed 50% of rejections in one market, research that market's band before changing its floor.

**Exit check:** Go recovery behavior is observable; compensation decisions remain market-specific.

### Week 11 — Revalidate; use mature evidence

**Allocation:** 19.25h search, 12.25h training, 3.5h management.

- Conduct a final bounded cloud-GPU validation if needed to prove the Go integration; do not incur an ongoing GPU bill.
- Finish the runbook, architecture decisions, and reproducibility instructions.
- Use mature evidence in new outreach and in active interview conversations.
- Compare Swiss and Berlin response and screen rates using equal definitions and minimum cohort notes.

**Market checkpoint:** If Switzerland has underperformed Berlin consistently across at least four active weeks, shift 10 percentage points of search effort from Switzerland to Berlin for the remaining period; record the change and review after three weeks if the strategy continues beyond week 12.

### Week 12 — Complete the evidence package; make the next-cycle decision

**Allocation:** 19.25h search, 12.25h training, 3.5h management.

- Complete the Go port and present one clear repository landing page covering Python, Go, real-GPU validation, SLOs, alerts, and runbook.
- Complete all due follow-ups; do not begin low-fit processes merely to increase activity.
- Review the complete 12-week funnel by market, tier, channel, and rejection reason.
- Decide the next cycle: continue the winning market/channel combination, revise positioning, pursue an admissible bridge role, or deepen a remaining evidence gap.

**Exit check:** Go port is complete; all claims are evidence-backed; the next-cycle decision follows recorded funnel data rather than intuition.

## 6. Pipeline tracker

Each opportunity/contact records:

- Company, role, URL, market, employer tier, role band.
- Channel and contact name.
- Hard-filter results: direct-experience requirement, seniority, compensation, remote-start/relocation, language.
- Date contacted/applied; follow-up dates; current stage; next action.
- Outcome and normalized rejection reason: relevance, readiness, compensation, location, process, unknown.
- Evidence version used: pre-project, early Python, completed Python, or Go.

Weekly dashboard:

- Applications sent and application-to-screen rate.
- Outreach sent and outreach response rate.
- Recruiter conversations.
- Recruiter screens and screen-to-rejection rate.
- Technical interviews reached.
- Compensation mismatches by market.
- Conversion by Switzerland/Berlin, employer tier, channel, and evidence version.
- Project milestone status and hours spent.

Rates use eligible cohorts whose response window has elapsed; unanswered messages younger than seven business days do not count as failures.

## 7. Friday review and adaptation rules

Reserve one hour every Friday inside pipeline-management time:

1. Update every pipeline record and project milestone.
2. Calculate the weekly dashboard and note cohort sizes.
3. Apply any triggered rule below.
4. Change one search variable at a time so the next cohort remains interpretable.
5. Set exactly three priorities for the next week: one search, one training, one follow-up.

Rules:

1. Outreach response below 10% after three active weeks: change targeting or messaging, one at a time.
2. Screen-to-rejection above 75% after four active weeks: identify the dominant qualification filter and adjust pre-qualification or role band.
3. Zero technical interviews by week 6: pause new ATS applications for week 7 and perform a funnel audit; keep qualified conversations active.
4. Compensation mismatch above 50% of rejections in one market: research that market's band before changing its floor.
5. Project milestone more than one week late: transfer 10% of total weekly time from search to training until recovered.
6. Switzerland consistently below Berlin after four comparable active weeks: shift 10 percentage points from Switzerland to Berlin; never abandon Switzerland solely on a small cohort.
7. An admissible Tier C bridge above €70k with AI exposure and architectural scope: pursue it as a strategic bridge.

## 8. Internal consistency and protected trade-offs

- **The search starts before the project is complete.** Existing SRE evidence already qualifies for Band 1; waiting six weeks would waste viable market time.
- **Claims lag evidence.** `Currently building` is allowed from week 1; completed Python/GPU/SLO claims appear only after week 6 proof. Go becomes a completed claim only after week 12 proof.
- **One project closes three gaps.** No second portfolio project competes for time.
- **Go is a deliberate stretch.** If the Python milestone slips by more than one week, recover Python first; do not start or preserve the Go port at the cost of incomplete core evidence.
- **Market and channel results stay separable.** Switzerland/Berlin, applications/outreach, and evidence versions are tracked independently.
- **Compensation and relocation filters are hard constraints.** Funnel pressure does not override them.
- **The plan optimizes qualified interviews, not activity.** Throughput targets never justify low-fit applications.

## 9. Approval decision

Approve only if all are acceptable:

- Approximately 35 hours per week is sustainable for 12 weeks.
- The week-6 Python and week-12 Go milestones are credible.
- Search begins in week 2 rather than waiting for the completed project.
- Switzerland remains the primary market at 60%, subject to the defined rebalancing rule.
- Compensation and relocation constraints remain hard filters.
- The public narrative honestly says `moving into AI infrastructure` and `GPU exposure` until stronger evidence exists.
