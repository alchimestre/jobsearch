# Anagram — Site Reliability Engineer (SRE), Web3 Infrastructure

**Posting:** https://jobs.ashbyhq.com/Anagram/72bc0471-ab17-4123-81fa-c1ee3921af1f · Ashby id
`72bc0471-ab17-4123-81fa-c1ee3921af1f` · **Location: "Anywhere"** — JD says *"Remote, Hybrid, or In-Office
(Location Flexible)"*
**Org:** Anagram — a **digital assets holding company** that invests in and incubates crypto projects; the SRE
supports "critical infrastructure across our ventures". The Ashby board files this under **"Portfolio Company
Hiring"**, not a named operating entity.
**Market:** **EU-remote** ("Anywhere" is a broad region containing the four target countries) · **Tier:** **C**
(Web3 infrastructure bridge — see the tier note) · **Channel:** ATS (Ashby) · **Track:** `web3`
**Posted:** **2025-02-04** — ~20 months old at application. Near-certainly an evergreen/talent-pool
requisition (see risks).
**Compensation:** **not published.** EU-remote floor is **€80,000** (§2); unverified.
**Applied:** ✅ **2026-10-05** · **Stage:** Contacted · **Issue:** #26
**Follow-ups:** 1st due **2026-10-12 → 2026-10-14** · final **2026-10-19 → 2026-10-23**
**jobradar:** no store row — the posting is not in the local store. Reconcile by the Ashby id above.

## Tier note — `track:web3`, `tier:c`, second Web3 bridge in two applications

Same §2 clause conflict as 1GLOBAL (#22) and Blockstream (#25):

- **§2 reject list:** "Crypto-continuity roles that do not strengthen AI-infrastructure positioning." No ML/AI
  surface here — no serving, no pipelines, no registry.
- **2026-09-29 amendment:** *"Web3 infrastructure is in scope in every lane."* This is genuine Web3
  infrastructure work (blockchain node operations, smart-contract deployment pipelines), so the amendment
  admits it.

**Resolution used here:** admitted as a **Tier C Web3 bridge**, tagged `track:web3`, **not** counted toward
ML-platform conversion. **Third instance of the same clause conflict — take it to the Friday review.**

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — ✅ **"4+ years of experience in DevOps, SRE, or Backend Engineering"**; ~4 evidenced
      years sit at the bar, not above it
- [ ] Compensation ≥ €80k (EU-remote) — **unverified**, no band published
- [x] On-site allows 8–12 week remote start / relocation assistance — ✅ **moot**: the role is explicitly
      remote-flexible ("Anywhere"), so no relocation filter applies. Still confirm the contract entity and
      whether France is an accepted work location
- [x] No day-one direct GPU / training / serving expertise requirement — ✅ none asked
- [ ] Has AI workload exposure AND architectural scope — ❌ **FAILS on AI exposure**: blockchain node
      infrastructure and decentralized systems. Architectural scope ✅ (IaC, observability, CI/CD ownership)

**Verdict: a deliberate long-shot on one unchecked hard filter (compensation) and one explicit failure (AI
exposure)** — but a **cheap** one: no relocation gate, no seniority stretch, and the craft match is direct.

## Craft read — near-exact match on the operational core

| JD requirement | Candidate evidence |
|---|---|
| IaC: Terraform, Kubernetes, containers | ✅ core claim, multi-environment, incl. on-prem bare metal |
| Reliability & observability: monitoring, logging, alerting | ✅ **named-match list** — Prometheus, Grafana, OpenTelemetry, ELK, Loki, Jaeger, Thanos; MTTR reduction |
| CI/CD & automation pipelines | ✅ GitHub Actions, Drone CI, GitOps (Flux, Argo CD) |
| Performance tuning in distributed systems | ✅ capacity and cost work (25% cloud-cost reduction); 40+ protocol networks at Kiln |
| Security: key management, access controls, network security | ✅ **strong match** — Vault, SOPS, External Secrets, Teleport, Kyverno, Cilium network policy |
| 4+ yrs DevOps/SRE/Backend | ⚠️ at the bar (~4 yrs continuous) |
| Coding: Python, Go, Rust, Bash | ⚠️ Bash strong; **Python/Go operational, not production claims** (`CONTEXT.md` Evidence Boundaries); **no Rust** |
| Cloud-native (AWS, GCP, Azure) | ✅ GCP-first, AWS/Azure adjacent |
| *Plus:* blockchain node infrastructure (Ethereum, Solana, Cosmos) | ✅ **direct Kiln/Cometh evidence** — operating multi-protocol network infrastructure, $8B+ secured |
| *Plus:* Web3 security for smart-contract deployments | ✅ Cometh (blockchain dev-tooling company), ISO 27001 led |

## Risks, stated plainly

1. **This is a holding company, not an employer of record.** "Portfolio Company Hiring" means the SRE is
   placed into an unnamed venture. The actual company, team, product and contract entity are **unknown**, and
   that is the first thing a screen must resolve.
2. **20-month-old posting.** Published 2025-02-04 and still listed, filed under a generic portfolio-hiring
   bucket. Most likely a standing pipeline rather than an open role. Do not read silence as a judgement.
3. **Remote "Anywhere" is not proof France is supported.** A US-founded digital-assets holding company may
   contract through a US or offshore entity. Confirm the entity, the contract type, and French eligibility
   before investing time.
4. **No AI surface.** Third crypto-domain role in a row on the trajectory; it builds no ML-platform evidence.
5. **Coding bar.** The JD names Python/Go/Rust; only operational Bash/Python is defensible today.

## Recruiter-screen questions (ask before any screen)

1. **Which portfolio company is this for**, and what does it build? Is Anagram the employer of record?
2. Total compensation range, and in what currency/entity (EU-remote floor €80k)?
3. Is France an accepted work location, and what is the contract type (EOR, contractor, local entity)?
4. Is the requisition active, or is this a standing pipeline across portfolio ventures?
5. How much of the work is node operations versus platform engineering and automation?

## Timeline

- Contacted / applied: **2026-10-05** (Ashby)
- Follow-up 1 due (5–7 business days): **2026-10-12 → 2026-10-14**
- Follow-up 2 due (10–14 business days): **2026-10-19 → 2026-10-23** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** the anonymous-portfolio structure and the stale posting are the two things that make silence
  likely and uninformative. Identify the venture and the entity before spending interview prep.
- What would have changed the outcome: a named portfolio company with an EU entity, a published band clearing
  €80k, and a role description that is not a 20-month-old standing requisition
