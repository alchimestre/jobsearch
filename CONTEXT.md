# Job Search Domain

## Terms

### AI Infrastructure (umbrella term)

The umbrella term for the target family, kept because it is the keyword employers use. It covers both the **ML platform / MLOps lane (primary)** and the **GPU/vendor tier (secondary)**.

### ML Platform / MLOps Engineer (primary target role)

The canonical target role as of 2026-09-11. A platform engineer responsible for the ML lifecycle surface — pipelines, model registry, serving/inference platform, training platform, ML observability — and for the Kubernetes platform those run on, including its reliability and economics.

Title aliases: **ML Platform Engineer**, **MLOps Engineer**, **Machine Learning Platform Engineer**, **ML Infrastructure Engineer**, **AI Platform Engineer**, **SRE — ML/AI Platform**, **AI Infrastructure Engineer**. Secondary (vendor tier): **GPU Platform Engineer**, **HPC/AI Platform Engineer**. Responsibilities override title.

Ranking rule: within MLOps-titled roles, prefer the **platform/infrastructure side** over **data-pipeline authoring** (Airflow/Spark/dbt ownership without platform scope).

### Search Strategy

A decision-complete system for generating qualified interviews. It includes target employers and markets, candidate positioning, application assets, outreach channels, pipeline measures, and adaptation rules.

### Self-Training Plan

A prioritized capability-development plan tied to the evidence expected for the target role. It is not a general AI curriculum. Amended 2026-09-11: Python first, then ML lifecycle tooling (pipeline orchestration, model registry, serving, drift monitoring), plus the SLO/error-budget layer — all evidenced by `docs/ml-platform-project.md`. Go is conditional and deprioritised: the primary lane is Python-first.

### ML Platform Evidence Artifact

The single portfolio project that closes the programming and SLO gaps and adds the ML-lifecycle evidence the primary lane screens on: a lab-scale ML platform on Kubernetes (pipeline → registry → serving → monitoring → SLOs). Spec: `docs/ml-platform-project.md`. It replaced `gpu-fleet-operator` on 2026-09-11. Non-goals: distributed training, GPU fleet management, HPC.

### Search Lanes

Effort split across active search (amended **2026-10-09**): **France-anchored 70%** — France-based roles and
France-compatible remote roles (EU-remote that can employ in France, or Web3 roles that are remote-first) —
**Web3 infrastructure 20%**, **Berlin/Germany 10%**. Switzerland moves to opportunistic only.

The change is a speed decision. Vincent needs income as soon as possible and needs to stay in France: a French
contract needs no permit, no move, and no relocation funding, so it clears every location filter at once. Web3
infrastructure is the fastest lane to income because it sits directly on the strongest evidence (Kiln: $8B+
secured across 40+ networks) and needs no AI-platform proof.

**Web3 is now a priority lane, not a fallback.** It ranks with the ML/MLOps lane for active effort, and it wins
ties against any role that needs a relocation Vincent has no funding for.

The earlier split (EU-remote/FR 50%, Berlin 35%, Switzerland 15%, amended 2026-09-11) is retired.

### Destination Hierarchy

The order in which destinations are pursued, given that job #1 need not relocate:

1. **EU-remote / France-compatible** — fastest to income, no relocation, no move.
2. **Berlin** — preferred first *physical* move: dense AI-infra/ML-platform demand, no visa or permit friction for EU citizens, lower cost than Switzerland.
3. **Switzerland** — the long-term destination: money, mountains and lakes, proximity to France. Target as an employed engineer with AI/ML-platform evidence (12–36 months), in rail-accessible cities (not Zurich-specific). A French-border (frontalier) arrangement is opportunistic only, not a lane.
4. **Australia** — added 2026-09-11 on Vincent's request. Desired destination, but **employer-sponsored only**: Vincent's assessment is that his profile does not clear the Australian points-based system, so a job offer is the required path (recorded as Vincent's own read; no Australian immigration policy was researched this session). Does not change job #1, which stays EU-remote/France-compatible for income reasons. Feasible route: remote-first employers whose hiring footprint already includes Australia.

Physical relocation happens only on a signed offer, funded by relocation assistance or an 8–12 week remote-start ramp.

### Target Countries

Added 2026-09-30. The places a role may require physical presence: **France, Germany, Switzerland, the Netherlands**. A hybrid or on-site posting outside those four is out of scope however good the title is — London, Warsaw, Madrid, Tel Aviv and US sites included. A remote posting is in scope when it names one of the four or is open to a broad region that contains them (EU, EMEA, Europe, worldwide, anywhere), and out when it names only some other country (`Remote - US`, `Remote, United Kingdom`). A remote posting that says nothing about geography is kept, flagged `-geo-unverified`, and reviewed by hand rather than dropped.

Enforced by jobradar's geography gate: `target_countries` in `tools/jobradar/config.yaml`. Work mode (`remote`/`hybrid`/`onsite`) and country are stored per row and visible in the TUI and `jobradar list --mode/--country`.

### Income Cliff

The binding constraint of the search: French ARE unemployment income ends **2027-07-15** (318 days remaining as of 2026-08-31), at €92.38 net/day ≈ €2,812/month ≈ €29,377 total remaining, with no savings and **zero tolerance for a month without income**. Because salary arrives ~30 days after a start date, the employment *start* is the deadline: target 2027-06-01, absolute 2027-06-15. A ~€2,900 reserve is held untouched to cover the payment lag.

### Late-Cliff Mode

The single widening triggered ~Feb 2027 if no offer is signed: compensation floor flexes to €70,000, the AI requirement widens to AI-adjacent infrastructure, the weekly ATS cap is removed (volume only inside the filters), and weekly capacity rises to ~45 h. Entered once as a labelled cohort so funnel data stays interpretable.

### Last-Resort Window

From ~Apr 2027, if still no offer: **non-AI** platform/SRE roles become admissible when they pass the compensation floor and the architectural-scope filter. Income continuity outranks every non-hard filter. This exists so the cliff is never reached at zero income.

### Solutions Engineer / Forward-Deployed Infrastructure Role

A **credible secondary option**: a customer-facing technical role at an AI-native company (Solutions Engineer, FDE, deployment or solutions infrastructure). Admit it only when engineering and product dogfooding remain the foundation of customer work — Kubernetes/Helm, private/on-prem deployment, solution design, and troubleshooting — rather than quota-first account sales or support. Keep it at ≤ ~¼ of the EU-remote/France-compatible effort until real customer-facing evidence is on the CV.

### Bridge Opportunity

A France-based or EU-remote role considered only when it materially strengthens AI-infrastructure positioning or enables later relocation. It is not part of the primary geographic pipeline.

### Candidate Positioning Thesis

Professional identity (amended 2026-09-11): Production SRE moving into **ML platform / MLOps engineering** (umbrella: `AI infrastructure`). The candidate leads with proven reliability, Kubernetes, distributed systems, observability, and cost work from high-stakes production environments, and states ML-platform specialisation as the deliberate next step.

Entry wedge: reliable ML platform operations. The immediate value proposition is making the platform that hosts models — pipelines, registry, serving — observable, resilient, reproducible, and cost-aware.

Why not GPU fleet operations (amended 2026-09-11): the GPU-fleet framing came from ticket 06's artifact choice plus a benchmark sampled entirely from GPU-vendor and lab JDs. Ticket 02's market map found Berlin demand is "mostly *in-house ML platform / MLOps* inside product companies and AI scale-ups" and "is not a GPU-cloud-vendor market". The vendor tier also demands hardware depth (CUDA/NCCL/RDMA/HPC) with no candidate evidence, at staff/senior bars. GPU/vendor roles remain a secondary lane.

### Differentiators

1. Rapid cross-domain reliability transfer: moved from regulated healthcare (HDS) to crypto infrastructure ($8B+ assets) to multi-protocol distributed systems, each time applying production reliability to a new domain within months.
2. Infrastructure-to-architecture translation: demonstrated ability to translate infrastructure constraints into architectural decisions and align cross-functional stakeholders.

### Web3 Infrastructure Track

Added 2026-09-29. Production infrastructure roles at blockchain / crypto / digital-asset employers: protocol and node operations, validator and staking infrastructure, RPC, indexing and on-chain data infrastructure, exchange and custody platform engineering. Admitted in **every** lane, with **no AI/ML requirement**, and treated as the fastest route to income because it sits directly on the candidate's strongest evidence (Kiln: distributed infrastructure securing $8B+ across 40+ protocol networks; Cometh: multi-zone Kubernetes for Web3 delivery tooling). It is a *track*, not a fallback: it does not weaken the positioning thesis, it is the same platform/SRE work applied to a domain where the candidate already has production receipts.

### ML Preference (not a gate)

Amended 2026-09-29. ML/AI-platform exposure is preferred and wins ties, but it does not gate admission. A role with no ML surface is admissible when it clears the compensation floor, the seniority band, the start-date constraint, and offers architectural scope — Web3 infrastructure roles by default, other platform/SRE roles case by case. The earlier formulation (a role only qualified if it owned or operated the platform ML workloads run on) is retired; the ML-platform definition itself still describes what the primary lane looks like.

### Earliest-Start Rule

Added 2026-09-29. The 2027-06-01 target start and the 2027-06-15 absolute are **deadlines, not goals**. When two opportunities are otherwise comparable, the faster-to-income one is pursued first, even where the slower one has more ML/AI surface. The income cliff still binds: no accepted offer may start later than 2027-06-15, and the ~€2,900 reserve stays untouched.

### Role-Selection Criterion

Prefer roles with architectural scope and cross-stakeholder communication over pure operational runbooks. The long-term career direction is toward creative and architectural infrastructure work; the positioning thesis serves the immediate transition but role selection should preserve room for that trajectory.

### Deferred to Evidence Package

Unconventional problem-solving and cross-field curiosity are real differentiators but are not claims to lead with. They must be demonstrated through a concrete portfolio artifact (e.g., a technical write-up or project showing a problem solved that others missed). This belongs in ticket 07, not in the positioning thesis.

### Evidence Boundaries

Claims the candidate can defend today:
- Production Kubernetes operations at multi-environment/multi-zone scale
- SRE reliability, incident response, and security-hardened environments (ISO 27001, HDS)
- Observability stack (Prometheus, Grafana, Loki, OpenTelemetry, ELK) with MTTR reduction
- Kubernetes platform tooling deployed/operated at Kiln: Velero (backup/restore), Teleport (access management), cert-manager (TLS automation), Flux (GitOps delivery), nginx (ingress)
- Tools used (not deployed) at Kiln: Loki (log aggregation), Argo CD (GitOps delivery), Vault (secrets)
- On-premise Kubernetes tooling deployed at Docaposte: MetalLB (bare-metal load balancing), Cilium (networking / network policy), HAProxy
- Ingress / API gateway tooling deployed at Cometh: Traefik, Kong, HAProxy
- Broader deployed tooling — middleware, data stores, Kubernetes add-ons: `docs/tooling-inventory.md` (employer attribution pending for part of the list)
- Terraform/Ansible IaC and CI/CD delivery
- Cost-reduction track record
- Hybrid-cloud operations
- Independent 2026 work: AI assistance/orchestration proofs of concept, and AI-assisted history/linguistics research (application layer — never presented as platform or infrastructure ownership)

Claims excluded from current positioning (evidence gaps to close):
- GPU fleet operations (experience is GPU-adjacent, not direct ownership)
- Production programming in Python or Go (operational scripting only)
- ML lifecycle tooling — pipelines, model registry, serving platforms, drift monitoring (targeted by the `ml-platform-on-k8s` artifact)
- Explicit SLO/error-budget/canary-rollout methodology (targeted by the `ml-platform-on-k8s` artifact)
- Distributed training or model-serving frameworks
- Datacenter fabric, AI storage, or HPC performance engineering

### Compensation Floors

Minimum total annual compensation below which an opportunity is not pursued (amended 2026-09-11):
- Switzerland: CHF 110,000
- Berlin: €80,000
- EU-remote / France-compatible: €80,000 (raised from €70,000 — a role that does not relocate must pay for the missing half of the goal)
- Late-cliff flex (from ~Feb 2027): €70,000, only for an offer passing every other filter
- Last-resort window (from ~Apr 2027): the floor still applies; scope and AI filters are what yield

France-role bands are `[INFERENCE]` estimates — no primary-source salary benchmarking was performed. Recalibrate on the first real offer or recruiter screen.
