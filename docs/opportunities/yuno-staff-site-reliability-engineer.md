# Yuno — Staff Site Reliability Engineer

**Posting:** https://www.linkedin.com/jobs/view/4451375646/ (LinkedIn; fr.linkedin.com mirror)
**Org:** **Yuno** — "the AI-native operating system of global commerce": one API connecting pay-ins, payouts,
fraud prevention, KYC/KYB and stablecoins; 1,000+ payment methods, 460+ integrations, 190+ countries.
Customers: McDonald's, NetEase Games, GoFundMe, Rappi.
**Market:** **eu-remote** (Remote — "you can work from everywhere"; posting location Lacaussade, FR) ·
**Tier:** **B** (SRE at an AI-native company; the owned platform is Yuno's AI-agent infrastructure, so a Tier A
bump is arguable) · **Channel:** ATS (LinkedIn) · **Track:** `ai`
**Applied:** ✅ **2026-10-11** (LinkedIn) · **Stage:** Contacted
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**
**Posting age:** "il y a 2 mois" at application → stale; response odds lower.

## Hard-filter checklist (§2 + lane filters)

| Filter | Result |
|---|---|
| JD language — English or French | ✅ **PASS** — JD body is English |
| Location — FR-based / FR-employable remote / on-site w/ relocation | ✅ **PASS** — fully remote, "work from everywhere"; French posting location |
| Role type — no software-engineering roles | ✅ **PASS** — SRE / platform reliability, no application authorship |
| Not Staff/Principal | ❌ **FAIL — titled "Staff Site Reliability Engineer", "+7 Years of Experience", "most senior reliability voice in the room"** |
| Compensation ≥ €80k | ⚠️ **NOT STATED** — "Competitive Compensation"; unverified |
| AI workload exposure AND architectural scope | ✅ strong — owns the platform that provisions/deploys AI agents at scale; AI/MLOps a preferred qualification |

**Verdict: deliberate long-shot — fails the seniority filter (Staff / +7 yrs vs ~4 yrs evidenced).** Logged per
`AGENTS.md` so the funnel stays interpretable. Location and role-type gates pass cleanly; the only blocker is
the seniority band.

## Craft read — minimum qualifications vs evidence

| Requirement | Evidence |
|---|---|
| Event-driven architecture / messaging (Kafka, NATS, RabbitMQ); sync→async migration | ⚠️ **not directly evidenced** — steady-state needs a concrete migration story |
| Deep AWS (EC2, VPC, IAM, S3, RDS) + networking | ⚠️ standing gap — evidence is GCP-first, AWS-adjacent |
| IaC (Terraform/Pulumi) reviewed in PRs | ✅✅ Terraform multi-environment, Terragrunt, Ansible |
| Kubernetes + Docker in production at scale | ✅✅ multi-zone / bare-metal production clusters |
| Observability + SLOs (Datadog or equivalent, tracing) | ✅✅ Prometheus, Grafana, Loki, **OpenTelemetry**, Datadog, Jaeger; ⚠️ formal SLO/error-budget practice is an excluded claim (targeted by `ml-platform-on-k8s`) |
| Chaos engineering / fault injection (Gremlin, Chaos Mesh, AWS FIS) | ⚠️ **not evidenced** |
| Distributed-systems debugging; coding for automation (Go/Python) | ✅ debugging; ⚠️ Python operational-scripting only |
| Databases — PostgreSQL, MongoDB, Redis | ✅ in tooling inventory |
| Technical leadership, mentoring, cross-team influence | ⚠️ scope claimed via cross-team platform work; no formal mentoring |
| English advanced | ✅ |

## Risks

1. **Staff level, +7 years.** The single hard blocker. Yuno wants "the most senior reliability voice in the
   room"; the CV shows ~4 years of continuous infra roles. Do not inflate tenure.
2. **AWS depth** is a minimum qualification again (4th–5th consecutive AWS gap).
3. **Event-driven / messaging ownership** and **chaos engineering** are named must-haves with no direct
   evidence.
4. **Posting is ~2 months stale.**
5. **No compensation band** — "Competitive Compensation"; floor unverified.

## Questions to put in writing (first follow-up)

1. Seniority: is the Staff scope negotiable, or is the +7-years bar hard?
2. Total compensation band, and the France/EU contract shape (employment vs EOR)?
3. AWS vs other cloud split, and is deep AWS gated in screening?
4. Is the AI-agent infrastructure an ML-serving surface, or orchestration platform only?
5. Is the posting still open?

## Timeline

- Contacted / applied: **2026-10-11** (LinkedIn ATS)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Screen date: — · Interview dates: — · Outcome: pending

## Outcome record

- Stage reached: Contacted
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** location and role type cannot be the cause (remote-from-everywhere; SRE work). A rejection is
  most likely **readiness** (Staff / +7 yrs) or **relevance** (AWS, messaging, chaos).
- What would have changed the outcome: —

## Funnel delta

Applications sent +1 (2026-10-11) · **eu-remote lane** · `tier:b` · `track:ai`. Deliberate long-shot
(seniority filter failed at application time).
