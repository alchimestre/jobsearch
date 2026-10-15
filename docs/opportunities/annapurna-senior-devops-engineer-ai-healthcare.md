# Annapurna (agency) — Senior DevOps Engineer, AI + Healthcare client, Berlin

**Posting:** https://www.linkedin.com/jobs/view/4465325023/ (LinkedIn job id `4465325023`) · posted 2026-10-08,
**30 applicants** at time of reading
**Agency:** **Annapurna Recruitment** (`uk.linkedin.com/company/annapurna-recruitment`) — UK agency, offices
London/Berlin, *"Tech Recruitment Partner for DACH Scale-Ups | Series A–C Specialist"*. Poster:
**Dan Jeffery**, LinkedIn DM open. Division: **Tech & GTM** (the agency's other divisions are Annapurna
Executive, HR, Interim, Finance, Marketing — see "Agency context" below).
**Client:** **unnamed.** *"Our client is combining AI & Healthcare to revolutionise patient care globally"*,
continuing growth across the engineering team. Berlin-based, hybrid.
**Market:** **DE** · **Tier:** **B** (SRE/DevOps at an AI-native) · **Channel:** **recruiter** (the 10% lane)
· **Track:** `ai`
**Applied:** ✅ **2026-10-09** · **Stage:** Contacted · **Issue:** #31
**Compensation:** **not published.** Suggested by the benefits list only: stock options, 30 vacation days +
birthday, Germany Transport Ticket, Urban Sports Club, flexible hours, hybrid. Berlin floor **€80,000** (§2).
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**
**jobradar:** no store row (agency posting, not an employer ATS board).
**Policy note:** agency recruiters are **inbound/opportunistic only** (`docs/search-plan.md` §4, wayfinder
ticket 08) — this is an inbound-posted agency role, logged for funnel completeness, **not** treated as a
primary channel. Precedent: #13 Bubblemaps via Yofy, also `channel:recruiter`.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — "Senior DevOps Engineer"; production ownership expected, no staff-level scope
      claimed
- [ ] Compensation ≥ €80k (Berlin) — ⚠️ **unverified, no band.** Scale-up Series A–C per the poster's own
      blurb, which is the band where a base under €80k is plausible; stock options cannot count toward the
      floor
- [ ] On-site DE with 8–12 week remote start or relocation — ⚠️ **partially satisfied, needs confirming.**
      The posting says **hybrid working setup** and lists *"opportunity for remote working and 'workaction'
      supported flexibility"* as a benefit, which is materially better than the full-on-site Berlin rows
      (#29 idnow, #30 Atlantic). **No relocation assistance mentioned.** Whether the first 8–12 weeks can run
      remotely from France is unverified
- [x] No day-one direct GPU / training / serving expertise requirement — ✅ the JD asks to **"support GPU
      clusters, training job orchestration"**, not to own NVIDIA-stack/HPC depth. The GPU claim stays off the
      CV, as `CONTEXT.md` requires
- [x] AI workload exposure AND architectural scope — ✅ *"own and evolve their platform and infrastructure
      across cloud, **edge, and ML environments**"*, enabling product and ML teams to ship compliant AI

**Verdict: admissible, and the best *stack overlap* in the pipeline. Two unknowns, both binding: the base
band and whether a France-based remote start is acceptable.**

## Craft read — the closest stack match logged so far

| JD requirement | Candidate evidence |
|---|---|
| **Production Kubernetes**: AWS EKS, bare-metal K3s, on-prem K3s appliances | ✅ multi-environment/multi-zone production K8s; **bare-metal at Docaposte** (MetalLB, HAProxy, Cilium); fleet-scale node operations across 40+ networks at Kiln |
| **GitOps: FluxCD** | ✅ **Flux deployed at Kiln** — an exact hit, not an adjacent one (Argo CD also `used`) |
| IaC: CloudFormation, Ansible | ⚠️ **gap in the named tools** — IaC depth is Terraform/Terragrunt. CloudFormation and Ansible are not in `docs/tooling-inventory.md`. Say so rather than stretch it |
| **Edge/on-prem appliance lifecycle**: VM image builds, TLS automation, staged rollouts | ⚠️ partial — **cert-manager (TLS automation) and Flux staged rollouts are real**; shipping and lifecycling physical appliances is not |
| **Monitoring/observability**: Prometheus, Grafana, Loki, **Tempo**, OpenTelemetry | ✅ **near-exact** — Prometheus/Thanos, Grafana, Loki, Jaeger tracing, Alertmanager, Datadog. OpenTelemetry and Tempo specifically: not in the inventory |
| **Security, compliance, secrets**: hardening, access control, audit logging, **SOPS/KMS** | ✅ **strongest section** — SOPS deployed, Vault, External Secrets, Teleport (identity-aware access), Kyverno policy, Cilium network policy, **ISO 27001 lead**, GDPR. Healthcare-adjacent compliance reads well here |
| **ML infrastructure**: GPU clusters, training job orchestration, ML data pipelines | ⚠️ **the AI bullet, and it is "support"**. GPU-adjacent, not direct ownership (`CONTEXT.md` excludes the GPU-fleet claim). Defensible framing: the Kubernetes platform the ML workloads run on |
| CI/CD pipelines | ✅ GitHub Actions, Drone CI |
| **On-call**, incident detection, triage, post-incident reviews | ✅ production SRE across two employers; on-call and incident response |
| Hybrid Berlin, team events in Berlin | ⚠️ location satisfies Berlin; relocation is self-funded unless stated otherwise |

## Risks, stated plainly

1. **Unnamed client.** No company to research, no way to verify funding, headcount or runway before a call.
   The AI-and-healthcare description is all there is.
2. **Agency channel.** Annapurna holds the relationship; the résumé goes to the client through a third party,
   and the recruiter's screening is an extra filter with its own incentives. Policy keeps this opportunistic.
3. **Compensation unpublished**, on a Series A–C scale-up with equity-heavy framing.
4. **CloudFormation/Ansible** are the two named tools with no evidence — a recruiter skimming for keywords
   will notice.
5. **Healthcare compliance** may bring medical-device or patient-data obligations not covered by ISO 27001
   alone.
6. **Job-search hygiene:** an unnamed client posting on LinkedIn with 30 applicants in a day is the standard
   shape of a role that may already be filled or may be a pipeline-building post. Treat silence as expected.

## What is genuinely attractive

- **The closest stack overlap in the pipeline**: production K8s including bare-metal, **FluxCD**, cert-manager
  TLS automation, Prometheus/Grafana/Loki, SOPS/Vault secrets, on-call — seven of the eight bullet groups are
  direct evidence, not adjacent.
- **Hybrid, not full on-site** — the first Berlin row where remote working is stated as a benefit rather than
  an exception.
- **A named contactable human** (Dan Jeffery) in the `channel:recruiter` lane, which the plan wants at 10% and
  the tracker has barely used.
- **ML infrastructure exposure** without a GPU-ownership gate — the honest level of the candidate's AI claim.

## Questions to put to the recruiter, in writing, before any call

Per §2 of `docs/search-plan.md` (mandatory before a recruiter screen):

1. **Base salary band** for the role, and what share is stock options?
2. **Location:** is the first 8–12 weeks remotely from France acceptable, and is there relocation support for
   Berlin?
3. **Who is the client** — name, incorporation, funding stage and headcount? (Unnamed-client postings stay
   unresolved until this is answered.)
4. What is actually in production today, and what does "cloud, edge, and ML" mean in practice — how much is
   the on-prem/edge appliance fleet versus EKS?
5. Is the GPU capacity operated in-house, and is training-job orchestration owned by this team or by the ML
   team?
6. What is the on-call rotation, and is there a compliance obligation beyond GDPR (MDR, patient data)?

## Agency context — Annapurna's divisions

Annapurna Recruitment operates as a generalist agency across permanent, interim and executive search, with
these practice divisions (annapurnarecruitment.com/about/team): **Tech & GTM** · **Annapurna Executive** ·
**HR** · **Interim** · **Finance** · **Marketing**. This role sits in **Tech & GTM** — the division that
carries the technology/DACH scale-up lines, with a Data & AI desk inside it. The other divisions are not
relevant to this search.

## Timeline

- Contacted / applied: **2026-10-09** (LinkedIn, via Annapurna)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Salary: not stated in the application (no figure submitted)
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** an agency posting with an unnamed client gives the recruiter every reason to leave the candidate
  in a pipeline. The written questions above are the only way to convert it into a real process — per the
  2026-10-09 rule, ask them in the **first follow-up**, not at a screen that may never come.
- What would have changed the outcome: —

## Funnel delta

Applications sent +1 (2026-10-09). **DE lane, `tier:b`, `track:ai`.** Second-ever `channel:recruiter` issue
(after #13 Bubblemaps) — the lane the plan allocates 10% and the tracker has run at **2 of 30 labelled rows
(≈7%)**.
