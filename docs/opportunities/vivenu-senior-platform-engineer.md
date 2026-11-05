# vivenu — Senior Platform Engineer (d/f/m)

**Posting:** https://www.linkedin.com/jobs/view/4460371549/ · Germany (vivenu, Frankfurt)
**Recruiter:** Anna Boiarynova (Senior Talent Acquisition) — https://www.linkedin.com/in/anna-boiarynova-0014bb11
**Market:** EU-remote (stated preference) · **Tier:** B (non-AI platform role at a product company; AI-workload exposure unconfirmed → treat as C until confirmed) · **Channel:** ATS
**Applied:** ✅ 2026-09-11 (submitted) · **Closed:** ❌ 2026-09-25 (refusal, **no reason given**) · **Follow-ups:** not sent (refusal superseded them)

## Why this is outside the current lanes

Frankfurt is not in the destination hierarchy (EU-remote/FR → Berlin → Switzerland) and the role is
**not** an ML platform / MLOps role. ML/LLM exposure is **preferred, not required** (§2, amended
2026-09-29), so the ML link is a note rather than a filter. The JD states the team uses LLM tooling
("healthy amount of skepticism for LLM generated code") but does not describe an ML-serving surface.
This role is admissible at Tier B-secondary at best, with the architectural-scope check **unchecked**.
Applying anyway is a deliberate long-shot; record it as such so the funnel data stays interpretable.

Also note the JD asks **5+ years**; the CV shows four years of continuous infra roles (Dec 2021 →
Jan 2026). Do not inflate; lead with scope, not tenure.

## The three application answers

### 1. Experience with high-traffic platforms

*87 words — style: `docs/writing-style.md`*

> Four years of production infrastructure. At Kiln (SRE, 2024–2026) I operated the distributed
> infrastructure securing $8B+ in digital assets across 40+ protocol networks, carrying sustained
> protocol-level traffic, and integrated 10+ protocols into hybrid-cloud environments. At Cometh
> (2023) I ran multi-zone Kubernetes on GCP, standardized observability (Prometheus, Grafana,
> OpenTelemetry, ELK) to cut MTTR, and reduced cloud cost 25% through architecture changes.
> At Docaposte I ran Kubernetes in HDS-certified healthcare. Same constraints at each: backpressure,
> replication lag, incident response under load, and one degraded dependency taking the platform down.

**No load figures.** Vincent cannot disclose throughput numbers — keep the answer structural
(networks, protocols, zones). The scale anchors are `$8B+`, `40+ protocol networks`, `10+ protocols`.

### 2. Salary expectations

> For a senior platform role at this level I'm targeting **€90,000–€100,000** total compensation,
> depending on platform ownership scope and the on-call model. Flexible on the base/variable split.

Single number if pressed: **€90,000**. ≤ 40 words; keep the same shape. The scope/on-call clause is
the only hedge worth keeping — it buys a range without sounding uncertain.

### 3. Core tech stack

*84 words*

> **Orchestration:** Kubernetes · Helm · Docker
> **Cloud & infra:** GCP · Linux · Terraform · etcd
> **Platform:** nginx · Traefik · HAProxy · Kong · MetalLB · Cilium · Flux · cert-manager · Velero · Kyverno · Teleport · Vault · SOPS · External Secrets
> **Delivery:** GitHub Actions · Drone CI (build, test, deploy pipelines)
> **Observability:** Prometheus · Grafana · OpenTelemetry · ELK · Loki · Datadog · Jaeger · Thanos
> **Data & messaging:** PostgreSQL · MongoDB · Elasticsearch · Redis · GCP Pub/Sub

**Do not upgrade Python/Go to production-language claims** until the `ml-platform-on-k8s`
artifact makes it true (`CONTEXT.md` Evidence Boundaries).

### Optional location line — only if the form asks

> I'm based in France and open to EU-remote, and I'm fully mobile within the EU regarding relocation
> timing.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal (senior, but no 8+ yrs demand)
- [x] Compensation ≥ €80k (asking €90–100k)
- [ ] AI workload exposure — **unconfirmed**, and **not a filter**: preferred, not required (§2, amended 2026-09-29)[INFERENCE: JD mentions LLM tooling, no ML-serving surface]
- [x] No day-one direct GPU / training / serving requirement
- [ ] On-site allows 8–12 week remote start / relocation assistance — **unasked**; ask at screen
- [x] Architectural scope (infrastructure design decisions, reusable Terraform modules, platform ownership)

## Recruiter-screen answers (ask before any screen)

1. Does the platform team own any ML/AI serving or training workload, or is it purely product infrastructure?
2. Seniority band and expected experience — is the 5+ years a hard bar?
3. Total compensation range for the role?
4. Remote start from France possible, or relocation assistance provided?
5. What does the current stack look like (GCP services, Terraform layout, Kubernetes topology, on-call model)?

## Outcome

- Stage reached: **closed at Contacted; no screen reported** (ATS application 2026-09-11 → refusal email 2026-09-12)
- Board Stage: **Closed** (reported and closed in the tracker on 2026-09-25)
- Rejection reason: **`location`** — the email says only candidates with a valid German work permit who can start short-term without relocation sponsorship were considered.
- Mail sent: **2026-09-12** · refusal received/reported: **2026-09-25**.
- Duration: 1 calendar day from application to refusal email; 14 days from application to tracker report/closure.
- Follow-ups: **none sent.** Follow-up 1 (due 2026-09-18) was missed during the 2026-09-14 → 09-23 pause; refusal mail had arrived before follow-up 2 due 2026-09-25.
- What would have changed the outcome: valid German work authorization and short-term availability without relocation sponsorship.
- Feedback request: **not sent.** §3 prescribes it only *after a recruiter-screen rejection*; no screen is reported.
- Next action: **closed.** No further contact. Removal from the follow-up queue; issue #3 closed with `reason:location`.

## Funnel delta

Rows this changes in §6's dashboard: applications sent (unchanged, 2026-09-11), application-to-screen (this application closes with no screen reported), screen-to-rejection (unchanged), rejection-reason tally (`location` +1).
