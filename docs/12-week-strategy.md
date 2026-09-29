# Integrated 12-Week AI Infrastructure Job Search Strategy

**Status:** Approved 2026-09-09 by Vincent. This is the operating plan for execution. Source: branch `prototype/integrated-strategy` at commit `d2fd804` (wayfinder ticket 10). It integrates decision tickets 01–09; it plans execution and does not itself execute applications, outreach, coursework, or profile changes.

**Amendment 2026-09-11 (grilling session):** the search is re-aimed by a newly quantified income cliff and by Vincent's confirmed weights on location vs purpose. Changes: lane allocation replaces the CH 60 / Berlin 40 market split; physical relocation is deferred to a signed offer; the Go port becomes conditional; compensation floors, AI definition, and role admission gain a late-cliff widening mode; deadlines are back-computed from ARE exhaustion. Full detail in §10.

**Amendment 2026-09-13:** Australia becomes **remote-only** (no visa-sponsorship or on-site relocation route); `Solutions Engineer` / forward-deployed infrastructure added to the target titles as a credible secondary option, admitted only where engineering and product dogfooding remain the foundation of the work.

**Amendment 2026-09-14 (pause):** Vincent is unavailable 2026-09-14 → 2026-09-23 inclusive. The search is **paused**, not abandoned: no outreach, no applications, no follow-ups, no project work in that window. The whole 12-week plan shifts **+10 days**, so Week 2 begins **2026-09-24** and the week numbering stays aligned to calendar dates (every `Week N` reference in §5 moves 10 days later). The mode timeline in §10 does **not** shift — late-cliff (~Feb 2027) and last-resort (~Apr 2027) are anchored to ARE exhaustion, not to week numbers, so the 12 weeks simply compress slightly against the cliff. Rules 1–3 in §7 count **active** weeks only; the pause does not count toward their denominators. Live follow-ups originally due 2026-09-18 / 2026-09-25 (issues #1, #3, #4) move to the week of 2026-09-24.

**Amendment 2026-09-29 (scope widening):** Vincent's instruction — Web3 companies are in scope, ML/LLM work stays preferred but **non-blocking**, and the return to work should be **as early as possible** rather than as late as the cliff allows. Changes: §2 admits a **Web3 infrastructure track** and deletes the crypto-continuity rejection; the ML requirement becomes a *preference* rather than a gate; §1 gains an earliest-start objective that ranks the fastest-to-income lanes first. No compensation floor, seniority filter, or cliff deadline changes.

## 1. Objective and constraints

**Objective:** Generate qualified interviews for mid-to-senior **ML Platform / MLOps engineering**, **AI platform engineering**, **SRE-on-ML-platform**, and **Web3 infrastructure** roles while producing credible evidence for the largest hiring gaps. **Return to work as early as achievable** — the 2027-06-01 target and the 2027-06-15 absolute are deadlines, not goals; any accepted offer that passes the filters is taken earlier, and where two opportunities are otherwise comparable the faster-to-income one wins.

**Lanes (amended 2026-09-11):** EU-remote / France-compatible **50%** · Berlin **35%** · Switzerland **15%** (relationships and selective applications only). Switzerland is a 12–36 month objective, not a job-#1 market. Job #1 is optimised for income continuity and AI transition; physical relocation happens only on a signed offer, and may be deferred to a second move. See §10.

**Destination hierarchy:** EU-remote/France-compatible (income + AI, no move) → Berlin (preferred first physical move; densest AI-funnel, no visa friction) → Switzerland (money + mountains/lakes + proximity to France; medium-term, rail-accessible cities; not Zurich-specific) → **Australia (added 2026-09-11; desired destination, employer-sponsored only — see below)**. A French-border (frontalier) arrangement is opportunistic only, not a lane. No hard anchors: fully mobile within the EU, income-constrained only.

**Australia:** Vincent's stated preference is to move there, but his own assessment is that his profile does not clear the Australian points-based system, so an employer-sponsored role is the only realistic route — no immigration policy was researched this session; treat the visa detail as [INFERENCE] until verified. Australia therefore adds no search-lane allocation now: job #1 remains EU-remote/France-compatible because of the income cliff. The actionable move is to **target remote-first employers whose hiring footprint already includes Australia** (or who will sponsor), rather than to open an Australian lane. First concrete example: vCluster Labs, issue #5.

**Available time:** 35 hours per week baseline, plus two push modes at ~45 h/week — weeks 1–4 (ramp) and the late-cliff window from ~Feb 2027. Sustained 45–50 h for the whole campaign is rejected: burnout over 10 months costs more than the extra hours buy.

**Positioning (amended 2026-09-11, second amendment):** Production SRE moving into **ML platform / MLOps engineering**. Lead with Kubernetes, production reliability, distributed systems, observability, cost optimization, security-hardened environments, and infrastructure-to-architecture translation. Use `AI infrastructure` as the umbrella keyword and `ML platform` / `MLOps` as the specific lane. Do not claim direct production ownership of ML platforms, GPU fleets, training systems, serving systems, Python/Go software, SLO/error-budget programs, or datacenter fabrics before evidence exists.

**Why ML platform rather than GPU fleet operations (amended 2026-09-11):** the earlier GPU-fleet emphasis came from ticket 06's single-artifact choice (a GPU Kubernetes operator) leaking into the identity, and from a 28-JD benchmark sampled entirely from GPU-vendor and lab postings. Ticket 02's market map concluded the opposite: Berlin's demand "is mostly *in-house ML platform / MLOps* inside product companies and AI scale-ups", it "is not a GPU-cloud-vendor market", and platform/reliability work is where "an SRE profile converts best". The vendor/lab tier also demands hardware depth (CUDA, NCCL, RDMA, HPC fabric) the candidate has no evidence for, and hires at staff/senior bars. ML platform / MLOps reuses the proven strengths, has a far larger and more remote-friendly funnel, and matches the candidate's own preference and 2026 independent work. GPU/AI-infra vendor roles remain a secondary lane.

**Relocation constraint:** No relocation savings. Any on-site Switzerland or Berlin role must support an 8–12 week remote start from France or provide relocation assistance. Relocation is never undertaken before a signed offer.

**Income cliff (harness of the whole plan):** ARE (French unemployment) pays €92.38 net/day; **318 days remaining as of 2026-08-31 → exhaustion 2027-07-15**; remaining runway value ≈ €29,377 (~€2,812/month). Zero tolerance for a month without income; no other savings. Consequences: the employment **start** date, not the exhaustion date, is the deadline (salary lands ~30 days after start); target start ≤ 2027-06-01, absolute ≤ 2027-06-15; sign by ~2027-04-20 (EU-remote) or ~2027-03-20 (Berlin/CH on-site, permit + relocation lead). Reserve ~€2,900 (one ARE month) untouched as a transition buffer. Keep France Travail obligations (actualité, convocations, offer-acceptance rules) satisfied, so the cliff date cannot move against the plan.

**Hardware constraint:** MacBook Air M4; no local NVIDIA GPU. Develop locally on OrbStack Kubernetes (single node), CPU-only — the ML-platform artifact requires no GPU. One optional bounded cloud-GPU run (≤ $20) may keep `GPU exposure` honest; it is not required and must not become an ongoing cost.

## 2. Role admission and ranking

### Admit

1. **Tier A:** Direct ownership of the ML platform / MLOps surface — ML pipelines, model registry, serving/inference platform, training platform, ML observability, or the Kubernetes platform those run on.
2. **Tier B:** SRE/platform role supporting ML teams — at an AI-native company, or in an in-house ML platform organisation at a product company with real AI workloads (the Berlin lane).
3. **Tier B-secondary — forward-deployed infrastructure (added 2026-09-11):** customer-facing deployment/operations roles at AI-native companies (FDE, deployment/solutions infrastructure), admitted at **≤ ~¼ of the EU-remote/France-compatible lane**, and only where the role stays **infrastructure-heavy** — planning, Kubernetes/Helm, private/on-prem deployment, troubleshooting — not pre-sales or support-ticket work. Blocked from scaling up until real customer-facing evidence exists on the CV (`docs/resume-edits.md`).
4. **Web3 infrastructure track (added 2026-09-29):** production infrastructure roles at blockchain / crypto / digital-asset employers — protocol and node operations, validator and staking infrastructure, RPC/indexing/data infrastructure, exchange and custody platform engineering, on-chain tooling. Admitted in **every** lane, and treated as the **fastest-to-income** track because it sits directly on Vincent's strongest evidence (Kiln: distributed infrastructure securing $8B+ across 40+ protocol networks; Cometh: multi-zone Kubernetes for Web3 delivery tooling). No AI/ML exposure is required for these roles.
5. **Tier C:** Non-AI, non-Web3 SRE/platform bridge role only when it offers architectural scope, strong compensation, and a credible path to AI exposure or relocation — **and only in the last-resort window from ~Apr 2027** (see §10).

### ML preference (amended 2026-09-29: preference, not a gate)

ML/AI-platform exposure is **preferred, not required**. A role is admissible without it when it passes the other filters — Web3 infrastructure roles (§2 Admit 4) are admitted by default, and any other platform/SRE role with architectural scope is admissible if it clears compensation, seniority, and start-date filters. Where two roles are otherwise comparable, the one with ML/AI-platform surface wins.

When ML/AI work is present it **qualifies** as before: the role must **own or materially operate the platform ML/AI workloads run on** — ML platform / MLOps, ML pipelines, model registry, serving/inference platform, training infrastructure, ML observability — at an AI-native company or in a product company's in-house ML platform organisation. GPU ownership is *not* required; running the platform that hosts models is sufficient. The umbrella term `AI infrastructure` still covers vendor-tier roles, which are admitted as a **secondary** lane.

Sub-filter within MLOps: prefer the **platform/infrastructure side** (Kubernetes for ML workloads, serving, reliability, capacity/economics, observability) over **data-pipeline authoring** (Airflow/Spark/dbt ownership with no platform scope). The latter does not use the candidate's differentiators.

### Reject before investing in a process

- Generic SRE/DevOps runbook roles **with no architectural scope and no Web3 infrastructure surface** (until the last-resort window). A runbook role at a Web3 infrastructure employer is admitted on the Web3 track.
- Roles based **outside the EU/EMEA** — US, Canada, LatAm, and APAC-only locations are rejected outright (added 2026-09-29), including "Remote - USA" postings. Australia/New Zealand travels on its own lane (§1) rather than as part of EMEA. A posting that offers both a US and a European location stays admissible.
- Roles whose **job description is not written in English or French** (added 2026-09-29). German-language JDs are excluded; an English-language JD at a German employer is **not**. Public-sector or SME postings written in German are the bulk of this group.
- Staff/Principal roles or roles asking 8+ years.
- Total compensation below **CHF 110k (CH) / €80k (Berlin) / €80k (EU-remote and France-compatible)**. In late-cliff mode (from ~Feb 2027) the floor may flex to €70k, but only for an offer passing every other filter.
- On-site roles without relocation assistance or an 8–12 week remote start.
- Roles requiring direct GPU, distributed-training, or serving-engine expertise on day one.
- Any role whose **start date** would leave an income gap at the cliff: start ≤ 2027-06-01 (target) / 2027-06-15 (absolute).

### Rank admitted roles

AI/ML-platform depth; architectural scope; 3–6 year seniority match; relocation feasibility; compensation; **time-to-income**; English-first environment; strategic bridge value. Company stage is not a filter. Within MLOps-titled roles, rank the **platform/infrastructure side** above the data-pipeline-authoring side. Between tracks, rank ML/AI-platform roles above Web3 infrastructure roles **only when time-to-income is equal** — the fastest credible route to a signed offer wins.

### Search titles

`ML Platform Engineer`, `MLOps Engineer`, `Machine Learning Platform Engineer`, `ML Infrastructure Engineer`, `AI Platform Engineer`, `AI Infrastructure Engineer`, `SRE — ML/AI Platform`, `Reliability Engineer — ML`, `Training Platform Engineer`, `Inference Platform Engineer`, and (secondary, vendor tier) `GPU Platform Engineer`, `HPC/AI Platform Engineer`; (credible secondary lane) `Solutions Engineer`, `Forward Deployed Engineer`, `Deployment/Solutions Infrastructure Engineer`.

Web3 infrastructure (added 2026-09-29): `Blockchain Infrastructure Engineer`, `Protocol Engineer`, `Node / Validator Operations Engineer`, `Staking Infrastructure Engineer`, `Platform Engineer — Web3`, `DevOps Engineer — Blockchain`, `Infrastructure Engineer (Remote) — Crypto`, `Exchange Platform Engineer`, `Custody Platform Engineer`, `Indexer / RPC Infrastructure Engineer`, `Site Reliability Engineer — Web3`.

Responsibilities override title: admit customer-facing roles only when engineering and product dogfooding remain the foundation of the work, not quota-first account sales or support.

## 3. Search channels and baseline throughput

Channel percentages apply to active search time. Target lists split by lane: **EU-remote/France-compatible 50%, Berlin 35%, Switzerland 15%** (CH = relationships + selective applications only).

- **60% hiring-manager/founder outreach:** EU-remote and France-compatible LinkedIn-first; Berlin LinkedIn-first; Swiss contacts email-first. Use the validated transition message from the evidence-package prototype.
- **25% targeted ATS applications:** Only roles passing every hard filter. From late-cliff mode (~Feb 2027) the weekly cap is **removed** — apply to every role that clears the filters, never to roles that fail them.
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

**Amended 2026-09-11 (second amendment):** one repository, `ml-platform-on-k8s`, replaces `gpu-fleet-operator`. The GPU operator was chosen to close three gaps in a single artifact, but it also dragged the identity toward GPU-fleet operations — a narrow tier with staff/senior bars and hardware depth (CUDA, NCCL, RDMA, HPC fabric) the candidate cannot evidence. The replacement closes the same gaps (Python, SLO methodology) while producing the ML-lifecycle evidence MLOps JDs screen on, and it reuses the proven Kubernetes / Helm / observability / cost strengths.

Build spec: `docs/ml-platform-project.md`.

### Phase 1 evidence — Python (weeks 1–6)

- Training/retraining pipeline running on Kubernetes: Python, containerised steps, scheduled and on-demand runs.
- Model registry with versions, stage transitions, and reproducible training artifacts (MLflow or equivalent).
- Model serving on Kubernetes with a defined scaling and rollout path.
- Prometheus metrics for both service and pipeline; Grafana dashboard; alert rules.
- Drift/quality monitoring on inputs and predictions.
- SLIs and error budgets for serving availability, serving latency, and pipeline success rate; operational runbook.
- CI/CD (tests, image build) plus GitOps deployment; architecture and design-decision documentation.

### Phase 2 — Go (conditional, deprioritised)

Go stays conditional and is now **lower priority**: MLOps/ML-platform roles are Python-first, while the benchmark's Go demand concentrates in vendor control-plane roles that are not the primary lane. If the Python artifact is complete and the search is on track, port the serving control path or a controller to Go/controller-runtime to evidence the stretch band; otherwise those hours belong to search and Go waits until after an offer.

### Positioned-away gaps

Spend approximately four hours each across the 12 weeks on conceptual study only:

- Distributed training: data/model parallelism, FSDP, Ray/Slurm basics.
- GPU/HPC hardware: CUDA, NCCL, InfiniBand/RDMA at a conceptual level.

Do not add these as CV claims or create separate portfolio artifacts. One optional bounded cloud-GPU run (≤ $20) may keep `GPU exposure` honest; it is not required and must not become an ongoing cost.

## 5. Weekly operating plan

**Capacity modes (amended 2026-09-11):** 35 h/week baseline; push to ~45 h/week in weeks 1–4 and again from the late-cliff trigger (~Feb 2027) if no offer is signed.

**Go is conditional (amended 2026-09-11):** the Python artifact (week 6) is a fixed milestone and the admissibility gate. The Go port is started after week 6 **only if** the search is on track and no offer is imminent; otherwise those hours move to search, outreach, and applications. Go is now **lower priority than before** — the ML platform / MLOps lane is Python-first, and Go's market weight sits in vendor control-plane roles, which are the secondary lane. If paused, it resumes after an offer. Weeks 7–12 below still describe the full path for when the condition holds.

### Week 1 — Make the search legible; establish the project

**Allocation:** 7h search/assets, 24.5h training, 3.5h pipeline management.

- Apply the approved CV restructure: ML-platform transition title, defensible profile, 25% Cometh cost reduction, Helm bullets, and `GPU exposure` rather than `GPU Workloads`.
- Apply the approved LinkedIn headline and About narrative (ML platform / MLOps; the 2026 independent work is the gap answer). Make **no project claim** until the artifact exists.
- Create the pipeline tracker and the initial target list on the lane split (EU-remote/FR 50 / Berlin 35 / CH 15).
- Create the `ml-platform-on-k8s` repository, README, architecture skeleton, and local OrbStack Kubernetes environment; scaffold the Python training pipeline.
- Define the pipeline → registry → serving contract and the SLIs it will expose.

**Exit check:** Search assets tell one consistent story; tracker exists; a containerised training step runs on the local cluster and writes a model artifact.

### Week 2 — Start outreach; stand up registry and serving

**Allocation:** 7h search, 24.5h training, 3.5h management.

- Begin outreach on the primary lanes first (EU-remote/FR and Berlin, LinkedIn-first); Swiss contacts email-first at low volume.
- Submit only high-confidence ATS applications; contact relevant in-house recruiters.
- Publish the first meaningful project commit and link it from the search assets.
- Stand up the model registry (MLflow or equivalent) and register a first trained version from the pipeline.
- Deploy the model-serving path end to end on the local cluster.
- Define the three SLIs and how each is measured.

**Exit check:** First outreach cohort sent; project link is public; a trained model is registered, served, and answering requests locally.

### Week 3 — Reach steady-state search; prove the local platform path

**Allocation:** 15.75h search, 15.75h training, 3.5h management.

- Reach the steady-state throughput targets while preserving the lane split.
- Send first due follow-ups.
- Complete the local end-to-end path: scheduled retrain → registry version → rollout to serving.
- Export Prometheus metrics for both the pipeline and the serving service.

**Exit check:** The retrain → register → serve path runs end to end on the local cluster; every pipeline entry has source, tier, market, status, next action, and due date.

### Week 4 — Harden serving; establish error-budget mechanics

**Allocation:** 15.75h search, 15.75h training, 3.5h management.

- Continue steady-state outreach, applications, recruiter work, and follow-ups.
- Add the Grafana dashboard and Prometheus alert rules covering pipeline and serving.
- Implement SLI measurement and error-budget burn for serving availability and latency.
- Add drift/quality monitoring on inputs and predictions.
- Begin distributed-training conceptual study.

**Checkpoint:** Calculate outreach response rate over weeks 2–4. If below 10%, change either targeting or messaging—not both—and label the changed cohort.

### Week 5 — Exercise failure recovery; diagnose qualification

**Allocation:** 15.75h search, 15.75h training, 3.5h management.

- Continue search at steady state with the selected week-4 adjustment, if any.
- Exercise failure recovery: a failing pipeline step, rollback of a bad model version, an unhealthy serving replica, and an idempotent retrain.
- Draft the operational runbook and record the evidence honestly as a learning artifact — never implying production-scale platform ownership.
- Begin GPU/HPC conceptual study.

**Checkpoint:** If screen-to-rejection remains above 75% after four active weeks, classify every rejection as relevance, readiness, compensation, location, or unknown. Narrow the responsible role band or strengthen the relevant pre-qualification question.

### Week 6 — Ship the complete ML-platform evidence package

**Allocation:** 15.75h search, 15.75h training, 3.5h management.

- Complete the artifact: pipeline, registry, serving, metrics, dashboard, alert rules, SLI definitions, error-budget policy, drift monitoring, runbook, architecture diagram, and reproducible setup instructions.
- Replace `in progress` with completed Python/SLO/ML-platform evidence in search assets only where the repository proves the claim.
- Use the completed artifact in new outreach and appropriate follow-ups.

**Checkpoint:** If no technical interview has been reached, pause new ATS applications for week 7. Audit the full funnel and compare pre-artifact versus post-artifact cohorts. Do not pause direct conversations already in progress.

**Exit check:** A reviewer can clone the repository, understand the architecture, run the local platform path, and see pipeline, registry, serving, monitoring, and error-budget evidence.

### Week 7 — Go port (conditional); perform the midpoint funnel audit

**Allocation:** 17.5h search, 14h training, 3.5h management.

- If the zero-interview trigger fired, use ATS time for the funnel audit; keep qualified outreach and active conversations moving.
- Scaffold a Go/controller-runtime component and reproduce the pipeline → registry → serving contract.
- Review market conversion separately by lane (EU-remote/FR, Berlin, Switzerland); do not pool the results.
- Finish any remaining distributed-training conceptual study.

**Exit check:** Root qualification cause is named if the trigger fired; the Go component builds and handles a minimal control path.

### Week 8 — Port the core control path

**Allocation:** 17.5h search, 14h training, 3.5h management.

- Resume or continue filtered ATS applications based on the week-7 audit.
- Port the serving/rollout control path, health-state evaluation, and idempotent reconciliation to Go.
- Continue full follow-up sequence and recruiter cultivation.
- Finish any remaining GPU/HPC conceptual study.

**Exit check:** The Go implementation reproduces the serving and rollout control decisions of the Python implementation.

### Week 9 — Run the Go component end to end

**Allocation:** 17.5h search, 14h training, 3.5h management.

- Run the Go component locally end to end with metrics and simulated failure states.
- Document differences between the Python prototype and the Go implementation.
- Refresh outreach links to point at the clearest evidence entry point.

**Exit check:** The Go component compiles and runs; architecture documentation explains both phases.

### Week 10 — Deepen Go behavior; increase search emphasis

**Allocation:** 19.25h search, 12.25h training, 3.5h management.

- Increase search emphasis without weakening filters.
- Port or improve the rollback/recovery path and Prometheus instrumentation.
- Review compensation mismatches by market. If they exceed 50% of rejections in one market, research that market's band before changing its floor.

**Exit check:** Go recovery behaviour is observable; compensation decisions remain market-specific.

### Week 11 — Revalidate; use mature evidence

**Allocation:** 19.25h search, 12.25h training, 3.5h management.

- If a GPU-inference line is wanted on the CV, conduct a single bounded cloud-GPU validation; otherwise skip it. No ongoing GPU bill either way.
- Finish the runbook, architecture decisions, and reproducibility instructions.
- Use mature evidence in new outreach and in active interview conversations.
- Compare Swiss and Berlin response and screen rates using equal definitions and minimum cohort notes.

**Market checkpoint:** If Switzerland has underperformed Berlin consistently across at least four active weeks, shift 10 percentage points of search effort from Switzerland to Berlin for the remaining period; record the change and review after three weeks if the strategy continues beyond week 12.

### Week 12 — Complete the evidence package; make the next-cycle decision

**Allocation:** 19.25h search, 12.25h training, 3.5h management.

- Complete the Go component if the conditional held, and present one clear repository landing page covering the pipeline, registry, serving, monitoring, SLOs, alerts, and runbook.
- Complete all due follow-ups; do not begin low-fit processes merely to increase activity.
- Review the complete 12-week funnel by market, tier, channel, and rejection reason.
- Decide the next cycle: continue the winning market/channel combination, revise positioning, pursue an admissible bridge role, or deepen a remaining evidence gap.

**Exit check:** Go port complete *if the conditional held*; otherwise search hours were spent and the evidence package stands on Python + real-GPU validation. All claims are evidence-backed; the next-cycle decision follows recorded funnel data rather than intuition.

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
8. **Late-cliff trigger (~Feb 2027, if no offer is signed):** enter late-cliff mode once, as a labelled cohort — comp floor flexes to €70k, the AI requirement widens to AI-adjacent infrastructure (§2), the ATS weekly cap is removed (volume only inside the filters), and weekly capacity pushes to ~45 h. Change nothing else.
9. **Last-resort window (~Apr 2027, if still no offer):** non-AI platform/SRE roles become admissible when they pass the comp floor and the architectural-scope filter. Income continuity outranks every non-hard filter. This is the final rung; it exists so the cliff is never hit at zero income.
10. **Relocation fund and trigger:** once employed, set aside a relocation fund (target ≈ €8–10k) and keep a standing CH/Berlin application stream (~2–3 h/week). Relocate when an acceptable on-site offer with support or a remote-start ramp arrives, or when the fund is ready and a suitable role is in reach. Hard review: **2028-01** — decide whether to keep deferring, change destinations, or commit. Review confirmed 2026-09-11.

## 8. Internal consistency and protected trade-offs

- **The search starts before the project is complete.** Existing SRE evidence already qualifies for Band 1; waiting six weeks would waste viable market time.
- **Claims lag evidence.** `Currently building` is allowed from week 1; completed Python/SLO/ML-platform claims appear only after week 6 proof. `GPU exposure` stays `exposure` unless the optional bounded GPU run happens. Go becomes a completed claim only after week 12 proof.
- **One project closes three gaps** (Python, ML-platform lifecycle, SLO methodology). No second portfolio project competes for time.
- **Go is a deliberate stretch and now conditional and deprioritised.** If the Python milestone slips by more than one week, recover Python first. From week 7, Go proceeds only while the search is on track; under cliff pressure the hours belong to the funnel. Never trade incomplete core evidence for the port.
- **The market decides the identity, not the artifact.** The GPU-fleet framing came from one project choice and outran the market evidence. Any future project that would change the positioning must first clear the market check (ticket 02 class), or the assets stay put.
- **Market and channel results stay separable.** EU-remote/FR, Berlin, and Switzerland, applications/outreach, and evidence versions are tracked independently.
- **Compensation and relocation filters are hard constraints.** Funnel pressure does not override them.
- **The plan optimizes qualified interviews, not activity.** Throughput targets never justify low-fit applications.

## 9. Approval decision

Approve only if all are acceptable:

- Approximately 35 hours per week is sustainable for 12 weeks, with ~45 h push modes in weeks 1–4 and the late-cliff window.
- The week-6 ML-platform (Python) milestone is fixed; the week-12 Go milestone is conditional and deprioritised.
- Search begins in week 2 rather than waiting for the completed project.
- Lane allocation is EU-remote/France-compatible 50% / Berlin 35% / Switzerland 15% (amended 2026-09-11, replacing CH 60 / Berlin 40).
- The income cliff drives the deadlines: start ≤ 2027-06-01 (target), sign ≤ ~2027-04-20 (EU-remote) / ~2027-03-20 (Berlin/CH).
- Compensation and relocation constraints remain hard filters, with the defined late-cliff and last-resort widenings.
- The public narrative says `moving into ML platform / MLOps engineering` (umbrella: `AI infrastructure`) and `GPU exposure`, until stronger evidence exists.

## 10. Income cliff, continuum beyond week 12, fallback ladder

*Added 2026-09-11 from Vincent's actual France Travail figures.*

### The cliff, quantified

| Item | Value |
|---|---|
| ARE daily rate | €92.38 net/day |
| Days remaining (as of 2026-08-31) | 318 |
| Monthly equivalent | ≈ €2,812 |
| Total remaining runway value | ≈ €29,377 |
| **Exhaustion date** | **2027-07-15** |
| Savings | none |
| Tolerance for a month without income | **zero** |

### Back-computed deadlines

| Milestone | By | Basis |
|---|---|---|
| Sign EU-remote offer | ~2027-04-20 | ~6-week offer→start lead |
| Sign Berlin/CH on-site offer | ~2027-03-20 | ~10-week lead (permit, relocation, notice) |
| Employment **start** (target) | 2027-06-01 | first salary ~2027-07-01, inside the cliff |
| Employment start (absolute) | 2027-06-15 | salary lands on exhaustion day |
| Reserve held untouched | ~€2,900 | one ARE month, covers the payment lag |

The start date, not the exhaustion date, is the deadline: salary arrives ~30 days after starting. Starting 2027-07-01 would leave 16 days at literally zero income — outside tolerance.

### Mode timeline

1. **Normal mode (now → ~Jan 2027):** full filters, personalised outreach, 2–4 filtered ATS/week, Python evidence gate at week 6.
2. **Late-cliff mode (from ~Feb 2027, if no offer):** one labelled cohort — comp floor → €70k; AI requirement → AI-adjacent; ATS cap removed (volume inside filters only); ~45 h/week.
3. **Last-resort mode (from ~Apr 2027, if still no offer):** non-AI platform/SRE roles admitted on comp + architectural scope. Income continuity wins.

### Post-week-12 continuum

After week 12 (≈Dec 2026), run the same machinery in four-week cycles until an offer: steady-state search at the lane split, evidence maintenance (the ML-platform artifact polished, Go only if the condition held), pipeline review each Friday, and the relocation fund started as soon as income resumes. The next-cycle decision at week 12 is only about *which channel/market combination to double down on*, not about whether to keep searching.

### Open inputs (not decisions)

- **Customer-facing evidence** — required before any FDE/forward-deployed application is scaled up; see `docs/resume-edits.md`. Unanswered as of 2026-09-11.
- **France Travail obligations** — confirm actualité/convocations/offer-acceptance rules on the France Travail account so no suspension can move the cliff. `[INFERENCE]` on the general rules; not verified against primary sources.
- **France-role compensation bands** — the €80k remote/FR floor is an estimate; no primary-source salary benchmarking was done in the research. Recalibrate on the first real offer or recruiter screen.
- **Helm** — confirmed used (2026-09-11); must appear on the CV before further applications.
