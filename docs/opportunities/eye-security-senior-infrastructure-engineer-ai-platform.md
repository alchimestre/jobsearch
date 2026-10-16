# Eye Security — Senior Infrastructure Engineer – AI Platform (f/m/x)

**Posting:** https://jobs.ashbyhq.com/eye-security/9e6f9a27-fba1-4adb-bcdc-9d4b5688d0e6 (Ashby board
`eye-security`) · internal title **Infrastructure Engineer IV** · published **2026-09-25**
**Org:** **Eye Security** — Dutch cybersecurity provider with **embedded cyber insurance** for European
organisations; HQ **The Hague**, **200+ FTEs**, teams drawn from national CERTs, intelligence agencies and
tech. Mission framing: enterprise-grade cybersecurity for businesses beyond the large players.
**Market:** **NL** · **Tier:** **B** (see the note — the AI-platform ownership is real but it is a *first area*
of a broader cloud role at a non-AI-native employer) · **Channel:** ATS (Ashby) · **Track:** `ai`
**Location:** ⚠️ **"The Hague – hybrid"**, from the employer's own ATS. The JD body also says *"remote-friendly
culture with quarterly meetups and annual company retreats"* — **the two conflict**, and the ATS string is the
more specific one. **Nothing about France eligibility, and no relocation support mentioned.**
**Applied:** ✅ **2026-10-09** · **Stage:** **Closed — refused 2026-10-16** · **Issue:** #38
**Compensation:** **not published** — no range on the posting and none in the Ashby board payload for any of
their 29 roles. NL floor is not defined in this repo (`market:nl` has no allocation yet); the DE/EU-remote
floor of **€80,000** is the only nearby reference `[INFERENCE]`.
**Follow-ups:** **none sent** — the refusal arrived **2026-10-16**, the day follow-up 1 opened
**jobradar:** board **added 2026-10-09** (`ashby:eye-security`, `market: other` — their board spans NL, DE, AT
and the Nordics, so no single market label is honest).

## Hard-filter checklist (§2)

- [ ] Not Staff/Principal / seniority — ❌ **6+ years required** (*"6+ years of hands-on experience in Platform
      Engineering, DevOps, SRE"*) against ~4 evidenced, with the role expected to **mentor mid-level
      engineers**. The steepest stated bar of any role logged today
- [ ] Compensation ≥ €80k — ⚠️ **unverified**; nothing published anywhere on their board
- [ ] On-site DE/NL with remote start / relocation — ⚠️ **fails on the ATS location**: **The Hague – hybrid**,
      no France eligibility, no relocation support stated. NL is an admissible country since 2026-09-30, but
      admissibility of the *country* is not admissibility from *France*
- [x] No day-one GPU / training / serving requirement — ✅ explicit: *"not an ML research or applied science
      position. You will not train or fine-tune models, build feature pipelines, or work as a prompt engineer"*
- [x] AI workload exposure AND architectural scope — ✅ *"your first major area of ownership will be the
      infrastructure behind AI-powered capabilities"*, with the wider cloud platform as the long-term surface

**Verdict: admissible on the work, three requirements unmet (6+ years, significant AWS, production code
authorship) and the location unresolved — the weakest of the day on hard filters, and simultaneously the
strongest on the one AI requirement that matters.**

## The requirement this role uniquely rewards

> *"Hands-on experience building and shipping a non-trivial agent or LLM-backed workflow, **either in production
> or as a side project with real users**, with evidence that it was genuinely useful."*
> *"You can speak concretely about the decisions you made around tool use, context and state, evaluation,
> failure handling, autonomy, cost, and latency, as well as how you deployed and operated the system and what
> it changed for the people using it."*

**This is the first JD in the entire pipeline where the 2026 AI-orchestration work is a stated requirement
rather than a nice-to-have** — and the JD explicitly permits the side-project route and explicitly excludes ML
research, fine-tuning and prompt engineering. The evidence boundary in `CONTEXT.md` allows the work *"at the
application layer"*, which is exactly the layer this JD wants. The gate is not the claim, it is the narration:
**prepare the concrete answers** — tool use, context and state, evaluation, failure handling, autonomy, cost,
latency, how it was deployed and operated, and what changed for its users. Same discipline as
`docs/interview-incident-stories.md`, different subject.

## Craft read

| JD requirement | Candidate evidence |
|---|---|
| **6+ years** platform/DevOps/SRE | ❌ ~4 evidenced; **mentoring mid-level engineers** is also expected |
| **Significant AWS**; scalable, resilient, secure AWS infrastructure | ❌ **AWS is absent from `docs/tooling-inventory.md`** — cloud depth is GCP plus hybrid/on-prem. Fourth JD today requiring AWS as the primary cloud (#32, #33, #34, #38) |
| **Authoring reusable Terraform modules for other teams, with versioning and release practices — not only working within an existing codebase** | ⚠️ Terraform/Terragrunt across multi-environment is strong; **authoring versioned modules for other teams** is a step beyond and is unverified. A precise, testable question — expect it in interview |
| GitOps, CI/CD, observability | ✅✅ Flux `deployed` + Argo CD, Drone CI, GitHub Actions; Prometheus/Thanos, Grafana, Loki, ELK, Jaeger, Datadog |
| **Production code in Go, Python or TypeScript** | ❌ **the excluded claim** (production authorship). Third JD today requiring it |
| **Shipped a non-trivial agent or LLM-backed workflow** | ✅ **the strongest match in the pipeline** — see above |
| Workload identity, access controls, secrets, least privilege, secure coding | ✅✅ Teleport, Vault, SOPS, External Secrets, Kyverno, Cilium, ISO 27001 lead |
| Distributed tracing across agent and tool calls; semantic failure detection; evaluation of non-deterministic behaviour | ⚠️ tracing yes (Jaeger, OpenTelemetry in the boundary claim); **evaluation and regression-testing of non-deterministic systems is the genuinely new skill** the JD names and the candidate does not yet hold |
| Usage and cost attribution | ✅ **cloud spend −25%**, capacity planning — the cost instinct transfers directly to token/agent cost |
| Startup/scale-up, ambiguity, prioritisation | ✅ Kiln, Cometh; regulated and novel domains |
| Nice-to-have: Bedrock/AgentCore/Strands/**LangGraph**/MCP/tool gateways | ⚠️ **verify before claiming** — the 2026 orchestration work may touch MCP/tool gateways; if it does, this is a strong differentiator, and if it does not, say so |
| Nice-to-have: **EU data-residency constraints for AI workloads** | ✅ HDS-certified healthcare infrastructure, GDPR, French data protection |
| Nice-to-have: cost optimisation, compliance, developer platform enablement | ✅ all three |
| English fluency | ✅ |

## Risks, stated plainly

1. **Location conflict.** The ATS says The Hague – hybrid; the JD says remote-friendly with quarterly meetups.
   A Dutch hybrid role is a relocation, and no relocation support is mentioned. **This is the third
   residency-gated application today** (#36 MAIA explicit, #37 Redcare probable, #38 The Hague).
2. **Three requirements unmet**: 6+ years, significant AWS, production code authorship. Any one of them is a
   normal miss; all three together plus a relocation question makes this a long shot.
3. **Compensation unavailable anywhere on their board** — 29 roles, no published ranges.
4. **The evaluation/regression-testing-of-non-deterministic-systems requirement** is a real new skill, not a
   framing exercise. Do not bluff it; the JD asks for *practical* ways.
5. **Reusable Terraform modules with versioning** — a specific, checkable claim that is currently unverified.

## What is genuinely attractive

- **The agent/LLM-workflow requirement** — the only JD in the pipeline that would *reward* the 2026 work as a
  stated requirement, with the side-project route explicitly accepted and ML research explicitly out of scope.
- **The AI-infrastructure surface is the first area of ownership**, with explicit guardrails, identity, cost and
  observability duties — the platform side of AI systems rather than the model side.
- **EU data-residency and compliance for AI workloads** is a nice-to-have here and a lived experience in the
  CV (HDS, ISO 27001), which is rare and increasingly demanded.
- Cost attribution across agent and tool calls extends the −25% cost story into the AI-spend problem.
- Cybersecurity with embedded insurance is a regulated, high-stakes domain where reliability and least
  privilege matter — the same shape as the environments already worked in.

## Questions to put in writing (first follow-up — never sent)

1. **Which countries can employ for this role** — is France possible, or is The Hague hybrid absolute? Is
   relocation supported?
2. Salary band? (Nothing published on the board.)
3. Is **6+ years** firm, and is the mentoring expectation formal?
4. How much of the role is the AI platform versus the wider cloud platform?
5. What does "evaluate non-deterministic behaviour" look like in practice there today?
6. Which AWS AI services are actually in use (Bedrock? AgentCore? something else)?

## Timeline

- Contacted / applied: **2026-10-09** (Ashby, via LinkedIn)
- **Refused: 2026-10-16** — before follow-up 1 was sent (it opened that day, Fri)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20** — not sent
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final) — not sent
- Screen date: —
- Interview dates: —
- Outcome: **negative**

## Outcome record

- Stage reached: **closed at Contacted, never screened** (Ashby application 2026-10-09 → negative answer
  2026-10-16)
- Board Stage: **Closed** (was Contacted; set 2026-10-16)
- Salary: not stated in the application
- Rejection reason: **`unknown`** — no reason given. The pre-application prediction was **readiness** (6+
  years, significant AWS, production code authorship) or **location** (The Hague hybrid, no France
  eligibility, no relocation support). A five-business-day refusal names neither, so the label stays
  `unknown` rather than a guess.
- Duration: **5 business days / 7 calendar days** — a screen-out, not a silence-close. Third-fastest refusal
  after Synthesia #16 (same day) and Voyage Privé #43 (1 business day).
- Follow-ups: **none sent** — the refusal arrived on the day the first window opened.
- What would have changed the outcome: a written answer on France eligibility or relocation support **before
  applying** (question 1 of the unsent list), and a published band. Both were unverified at application time
  and neither is testable from a bare refusal.
- **Watch:** as predicted. The three unmet requirements plus the unresolved location made this the weakest
  hard-filter row logged on 2026-10-09, and it closed without a screen. The agent/LLM-workflow match, the
  strongest in the pipeline, never got read.
- Next action: **closed.** No further contact. Issue closed with `reason:unknown`.

## Funnel delta

Applications sent +1 (2026-10-09) · **NL lane** · `tier:b` · `track:ai` · board gap closed (Eye Security was
untracked; their board carries Berlin-hybrid roles worth watching later). **Ninth application logged today**,
and the third consecutive one whose binding constraint is relocation or residency.

Closed 2026-10-16 at Contacted, never screened, `reason:unknown` — the **16th closed row**, and the count of
unclassified closures is now **16 of 16, with 15 of them pre-screen** (MarvelX #21 remains the only closure
that reached a live screening step). It adds nothing to the classified-rejection count.
