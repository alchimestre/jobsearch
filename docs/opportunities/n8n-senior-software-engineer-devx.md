# n8n — Senior Software Engineer - DevX

**Posting:** https://www.arbeitnow.com/jobs/companies/n8n/senior-software-engineer-devx-berlin-79819 · **Berlin**,
Engineering, Full Time · **delisted from n8n's Ashby board** before this doc was written
**Org:** n8n — open workflow orchestration platform repositioned for the AI/agent era. 260+ staff, centre of
gravity **Berlin**, 650K+ developers, 190K+ GitHub stars, **$5.2bn valuation**.
**Team:** Developer Experience / Developer Platform, working with Security, AI/Agents, Architecture and product
engineering.
**Market:** **DE (Berlin)** · **Tier:** **B** (AI-native company, Berlin lane — see the caveat) · **Channel:** ATS
(Ashby) · **Track:** `ai`
**Applied:** ✅ date **not captured** (the posting was live ~2026-09-28 and was gone from the Ashby board by
2026-10-05) · **Stage:** **Closed** 2026-10-05 (refused)
**Compensation:** **unknown** — not disclosed on the listing; n8n publishes bands per role on Ashby
(`#23` was €91.4K–€171.7K, WE/NE €114.3K–€149.3K), so a comparable band is [INFERENCE], not evidence.
**Logged retroactively:** this application was never in jobradar's store or in the issue tracker; it was
reported by Vincent at refusal time. Everything below is reconstructed from the aggregator copy of the JD.

## Tier caveat — AI dev-tooling, not ML-serving

Identical in kind to `#23`. Tier B is the AI-native-company / Berlin lane. The role **does not own the ML/AI
serving platform**: it keeps n8n "operating as an AI-native engineering organization where agents are embedded
across the development cycle" — guardrails for autonomous agents, isolated execution environments, monorepo
agent-readiness, Linear/GitHub/CI integration, benchmarks from historical engineering tasks, adoption and
quality metrics. Real AI-systems work, but developer productivity, not model serving. Ranked below a true
ML-platform role, above any Tier C bridge.

## JD-to-evidence map

| JD must-have | Candidate evidence |
|---|---|
| Autonomous coding agents / agent orchestration / internal AI developer tooling | ⚠️ **the sharpest gap.** Evidence Boundaries allow only *"AI assistance/orchestration proofs of concept (application layer — never presented as platform or infrastructure ownership)"*. No production agent-platform ownership |
| Agentic workflows that work *with* developers, not beside them | ⚠️ same. Daily agent-tooling practice is real, org-scale deployment is not evidenced |
| Strong engineering foundations (platform, DevEx, infra, tooling, CI/CD) | ✅ core claim — Kubernetes, Terraform, multi-environment delivery, GitHub Actions and Drone CI |
| Ambiguity leadership on a first-of-a-kind initiative | ✅ **led the ISO 27001 implementation** at Cometh; infrastructure-to-architecture translation |
| Modern workflows: GitHub, CI, testing, monorepos, issue tracking, release risk | ✅ CI/CD, GitOps (Flux, Argo CD); ⚠️ **monorepo experience not evidenced** |
| Safety-first judgment: permissions, secrets, sandboxing, human-in-the-loop | ✅ **strong match** — Vault, SOPS, External Secrets, Teleport, Kyverno policy, Cilium network policy/isolation |
| Measurable systems thinking: benchmarks, quality signals, adoption metrics | ⚠️ MTTR reduction, 25% cloud-cost reduction, SLO practice (artifact) — no agent-benchmark or quality-signal work |
| Clear written communication | ✅ runbooks, playbooks, internal documentation |
| Cross-functional influence without formal authority | ✅ |
| *Nice-to-have:* TypeScript monorepo | ❌ **no TypeScript/Node production claim** |
| *Nice-to-have:* GitHub Actions, Linear, preview environments, internal dev platforms | ✅ GitHub Actions; ⚠️ Linear and preview environments not evidenced |

## Hard-filter checklist (§2) — assessed **after** the refusal

- [x] Not Staff/Principal — no staff title, no 8+ years stated
- [ ] Compensation ≥ €80k (DE) — **unverified**; not published on the listing. `#23`'s published band suggests
      the employer pays above the floor, but that is a different req
- [~] Location / relocation — the listing shows **Berlin** and the role sits in a "remote-first" team;
      remote-in-EU from France is plausible but was never confirmed. `#23` had the same ambiguity and it was
      never resolved
- [x] No day-one GPU / training / serving expertise requirement — none asked
- [x] AI exposure AND architectural scope — ✅ agentic platform ownership, guardrails, sandboxing,
      benchmark design. Not a runbook role

## Outcome record

- Stage reached: **closed at Contacted, never screened** (applied ~2026-09-28/30 → refusal reported
  2026-10-05; **application and refusal dates not captured**)
- Board Stage: **Closed** (set 2026-10-05)
- Rejection reason: **`unknown`** — no reason given
- Follow-ups: **none sent, none owed** (the refusal predates any follow-up window; the application was not
  logged when made, so no window was ever scheduled)
- Feedback request: **not sent** — never reached a screen
- **Logged after the fact, deliberately.** An application that produced no issue, no opportunity doc and no
  jobradar row cannot be reviewed at the Friday review and cannot be counted in the funnel. It is recorded
  now for accounting only; the honest verdict on the role is unknowable because it never reached a human

## ⚠️ n8n double application — second company in the pipeline with this pattern

This application and **#23 (Agentic Engineering Platform Engineer)** were sent to the **same team at n8n**
(Developer Experience / DevXP) **within days of each other**, and **both were refused without a screen**
(#23 refused 2026-10-02, this one 2026-10-05).

- The two JDs are near-duplicates in scope: agent guardrails, sandboxed execution, monorepo agent-readiness,
  Linear/GitHub/CI integration, agent benchmarks and adoption metrics.
- Two refusals from one team in three days is **not** two independent data points. Treat it as **one** result:
  n8n triages engineering applications fast and silently.
- **Never apply to a second req on the same team without disclosure.** This is the third double-application
  in the pipeline (Nebius #18/#19, Cohere #1/#14, now n8n #23/this). The Nebius and Cohere cases were flagged
  *before* the second application; this one was not flagged at all because the first application was never
  logged.
- **Next action: closed.** No further contact. Do not apply to a third n8n req.
