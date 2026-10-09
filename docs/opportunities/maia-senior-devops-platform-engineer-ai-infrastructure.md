# MAIA — Senior DevOps / Platform Engineer, AI Infrastructure (m/f/x) — **deliberate long-shot**

**Posting:** https://www.linkedin.com/jobs/view/4465551573/ (LinkedIn job id `4465551573`; posted ~3 weeks
before reading, **157 applicants**)
**Org:** **MAIA** — *"the AI platform built for companies where generic AI tools break down because the data is
complex, the stakes are high, and precision matters"*: complex documents, AI in real workflows, organisational
knowledge, and the systems underneath. Team meets in **Leipzig**. `⚠️ [INFERENCE]` The LinkedIn company slug is
`prodlane-maia` and the JD's framing overlaps the agentic-enterprise-data platform at `maia.ai`, but the two
were not confirmed as the same entity — **do not repeat company facts from that site as if verified.**
**Market:** **DE** · **Tier:** **B** (upper end; see note) · **Channel:** ATS (LinkedIn) · **Track:** `ai`
**Applied:** ✅ **2026-10-09** · **Stage:** Contacted · **Issue:** #36
**Compensation:** **€75,000 – €85,000 published** (LinkedIn "MAIA provided pay range"), plus **VSOP**.
**Follow-ups:** **none owed** — see the verdict below.

## Verdict: fails two hard filters → recorded as a deliberate long-shot

Per `AGENTS.md`, a role that fails a hard filter still gets an issue so the funnel data stays interpretable.
This one fails twice, and the first failure is absolute:

1. **❌ Residency — the fatal one.** *"This role is open **exclusively to candidates currently based in
   Germany**. Applications from outside Germany cannot be considered."* and *"Fully remote work from anywhere
   within Germany."* Vincent is based in **France**. The §2 filter requires that an on-site DE role either
   allows an 8–12 week remote start from France or provides relocation assistance — this posting offers
   **neither**, and its remote work is explicitly bounded to German residency. **The application cannot be
   considered as written**, which is why no follow-up is owed.
2. **⚠️ Compensation — a disclosed partial breach.** The DE floor is **€80,000** and the published band is
   €75,000–€85,000 — so the floor sits **exactly at the band's midpoint**, and the employer states the figure
   is *"depending on experience and scope"*. Clearing the floor requires landing in the upper half. This is
   **better than Lity #8** (where the floor was the band's literal ceiling) but it is still a breach at the
   bottom of the range, disclosed by the employer rather than inferred by us.

- [ ] Not Staff/Principal — ✅ passes (senior IC, explicitly *"without people management"*)
- [ ] Compensation ≥ €80k (DE) — ⚠️ **fails at the bottom of the band** (floor = midpoint)
- [ ] On-site DE with remote start / relocation — ❌ **fails: Germany-residency only**
- [x] No day-one GPU / training / serving requirement — ✅ *"We do not expect you to arrive as an expert in GPU
      operations or self-hosted inference"*
- [x] AI workload exposure AND architectural scope — ✅ explicit: shape AI infrastructure, evaluate inference
      providers, path to self-hosted LLM serving

**Why it was logged rather than dismissed:** the technical fit is unusually strong (below), and the Berlin lane
is the preferred first physical move — so if the residency requirement ever softens, or if a relocation
conversation becomes possible, the record already holds the analysis. Until then it is a long-shot: **the
employer's own text excludes it.**

## Tier note

**Tier B**, at the upper end — one step below #30 Atlantic. The must-haves are platform operations
(self-administered Linux, PostgreSQL, observability, security), while **AI-infrastructure ownership is
prospective**: *"Over time, this may include GPU infrastructure and serving technologies such as vLLM"*, with
GPU/LLM-serving experience *"helpful but not required"*. The JD does carry a dedicated **"Your AI foundation"**
requirements section and the employer is AI-native, which is what keeps it in the `ai` track and near the top
of tier B.

## Craft read — the must-haves are almost a transcription of the inventory

| JD requirement | Candidate evidence |
|---|---|
| **Linux servers you administered directly**; *"experience limited to fully managed hyperscaler services is not sufficient"* | ✅✅ **the anti-hyperscaler requirement is the profile**: bare-metal Kubernetes at Docaposte (MetalLB, Cilium, HAProxy), distributed node fleets at Kiln (40+ networks, $8B+) |
| **Docker and Docker Compose in production**; **reverse proxies or API gateways such as Traefik or Kong** | ✅✅ **both named tools are in the inventory as `deployed` at Cometh** — Traefik and Kong — plus nginx ingress and HAProxy |
| **PostgreSQL**: backups and restores **personally configured and tested**, performance analysis, connection pooling | ✅ PostgreSQL `deployed` at two employers ⚠️ **but**: K8s-level backup/restore (Velero) is deployed, whereas **Postgres-specific restore testing and connection pooling are not evidenced** — this is the row to prepare hardest, and the JD is explicit that the restores must be personally tested |
| CI/CD with **GitHub Actions, GitLab CI** | ✅ GitHub Actions `used`, Drone CI `deployed`, GitOps with Flux/Argo CD ⚠️ GitLab CI not used |
| **Terraform, Pulumi** or comparable IaC | ✅✅ Terraform (deployed, multi-environment) and Terragrunt — the JD's first choice |
| Observability with **Grafana, Loki, Prometheus, Sentry** | ✅ **three of the four are in the inventory** (Grafana, Loki, Prometheus + Thanos, Alertmanager) ⚠️ Sentry not used |
| Security: IAM, least privilege, secrets management, vulnerability scanning, patching | ✅✅ Teleport (identity-aware access), Vault, SOPS, External Secrets, Kyverno policy, Cilium network policy, production hardening |
| **ISO 27001 technical controls with continuously generated audit evidence** (helpful, not required) | ✅✅ **a lead ISO 27001 implementation** — the differentiator in this JD, and the "evidence generated continuously" framing is exactly what a real implementation produces |
| **AI foundation**: how RAG systems work and where they fail in production; LLM serving trade-offs (latency, throughput, reliability, cost, operational complexity) | ⚠️ **the honest gap**: AI orchestration work at the application layer, no production RAG system. The JD mitigates it (*"do not expect an expert"*), and "evaluating providers on reliability, latency, cost" is a judgement exercise the cost and reliability evidence speaks to |
| Use AI tools productively **while remaining accountable for every decision** | ✅✅ the 2026 work, framed the way the JD frames it |
| Incidents: root causes, runbooks, documentation, lasting improvements | ✅✅ incident response, post-incident reviews, hardening |
| Cost transparency; build/buy and hosting decisions | ✅ **cloud spend −25%**, capacity planning |
| Hetzner, NixOS, self-hosted Supabase (helpful) | ❌ none evidenced |
| SLOs, error budgets, incident reviews (helpful) | ⚠️ incident reviews yes; **an owned SLO/error-budget programme is an excluded claim** |
| English fluent; German helpful | ✅ |

## What is genuinely attractive about the role

- **Sole technical ownership** — *"initially the only dedicated Platform Engineer"*, working directly with the
  CTO: the ownership density this search is looking for, in a well-funded AI startup.
- **Self-administered Linux and European infrastructure providers, not managed hyperscalers** — the JD's
  hard requirement is the opposite of a managed-cloud background, which is rare and matches exactly.
- **Traefik/Kong, Terraform, Grafana/Loki/Prometheus, ISO 27001** — four independent exact hits.
- **An explicit path into AI infrastructure** (inference providers, then possibly vLLM/GPU) with no expectation
  of arriving as an expert — the cleanest route from SRE into the ML-serving lane seen in this search.
- **The written application** asked three questions — the most critical production system, one risk/incident
  improved, and why the autonomy fits — *"written by yourself, no AI-generated cover letter"*. That is a
  well-designed screen, and it maps onto the material in `docs/interview-incident-stories.md`.

## Risks (beyond the two failed filters)

1. **157 applicants in three weeks** — high volume, and the employer states it reviews against a *"deliberately
   focused profile"*, so the residency rule is likely enforced mechanically at the screening stage.
2. **Postgres backup/restore being a stated gate** and not currently evidenced at depth.
3. **Sole platform engineer** in a Germany-only remote setup — high autonomy, and correspondingly high
   expectation of prior independent ownership.
4. Company identity not fully disambiguated (`prodlane-maia` vs the `maia.ai` site) — relevant only if it
   progresses.

## Questions, if it ever progresses

1. Is the Germany-residency requirement **absolute**, or could it flex for an EU citizen relocating, or with a
   remote start?
2. Does the band reach €85k for a candidate at this experience level?
3. What are the current PostgreSQL backup/restore and connection-pooling arrangements?
4. Which parts of the estate run on Hetzner/self-managed hardware versus AWS/Azure/GCP?

## Timeline

- Contacted / applied: **2026-10-09** (LinkedIn)
- **Follow-ups: none owed** — the posting states applications from outside Germany cannot be considered, so a
  follow-up would only restate the exclusion. If a reply arrives, treat it as upside
- Screen date: —
- Interview dates: —
- Outcome: pending (expected: no response)

## Outcome record

- Stage reached: Contacted
- Salary: **€75,000–€85,000 published** (floor at the band's midpoint)
- Rejection reason (relevance / readiness / compensation / location / unknown): **`location` is the predicted
  one** — but note the label is applied only on an actual rejection, and a silent no-response stays `unknown`
- **Watch:** this is the first row where the predicted reason is known in advance and is **not** a judgement
  about the candidate. If it closes, record it as `location` **only if the employer says so** — a silent
  application that fails a residency gate is exactly the kind of row that pollutes the `unknown` pile
- What would have changed the outcome: the same role posted as EU-remote, or with relocation support

## Funnel delta

Applications sent +1 (2026-10-09) · **DE lane** · `tier:b` · `track:ai` · **fails the residency filter and the
bottom of the compensation band** → deliberate long-shot, recorded so the funnel stays interpretable. Fifth
application logged today.
