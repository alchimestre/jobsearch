# MarvelX — DevOps Engineer

**Posting:** https://www.marvelx.ai/careers/devops-engineer · **posted 2026-09-29** (applied day 1–2)
**Org:** MarvelX — AI agents for regulated industries (insurance, financial services); "audit-ready AI workforce for modern insurance carriers and TPAs". Amsterdam-built. Compliance credentials displayed: **ISO 27001, SOC 2, GDPR**.
**Apply route:** Typeform (`form.typeform.com/to/dobvzR4N`) — **not an ATS**, so no board record for jobradar to auto-adopt
**Market:** **NL (Amsterdam, hybrid — 3 days/week in office)** · **Tier:** A/B (owns the platform AI workloads run on) · **Channel:** ATS (company site → Typeform)
**Applied:** ✅ 2026-09-29 · **Salary stated: €85,000 + relocation support requested**
**Stage:** **Closed** 2026-10-05 (refused after the questionnaire, no reason given) — screening complete, not advanced

## Why this fits — the cleanest evidence match in the pipeline

Every "What we're looking for" bullet is met or met-adjacent:

| JD ask | Candidate evidence |
|---|---|
| Own and operate Kubernetes in production | ✅ Core claim |
| IaC with Terraform managing real infrastructure | ✅ Deployed across multi-environment clusters |
| Observability (Prometheus, Grafana, ELK, OpenTelemetry, or similar) | ✅ **Named-match list** — all four plus Loki and Jaeger |
| Multi-cloud (AWS/GCP/Azure) | ✅ Hybrid-cloud, GCP-first, AWS and Azure adjacent |
| GitLab CI/CD or similar | ✅ GitHub Actions + Drone CI (GitLab is a gap, "or similar" applies) |
| Docker, Linux, **scripting** (Bash, Python) | ✅ **Scripting** is the exact wording — not production software |
| Support AI/ML workloads (serving, batch, GPU) | ⚠️ "Support" only; **GPU is nice-to-have**, not a barrier |
| **ISO 27001 / SOC 2 exposure** | ✅ **Led ISO 27001 implementation** at Cometh; HDS-certified healthcare at Docaposte |
| Helm or Kustomize (nice to have) | ✅ Helm confirmed in `docs/resume-edits.md` |

**The contrast that matters:** Munich Electrification asked for *"a track record of building scalable,
production-grade applications"* (fails). This asks for *"Linux and scripting skills (Bash, Python)"* (passes).
Same tool, different bar. This role operates the platform, it does not author the product.

## ⚠️ The blocking issue: relocation, and it is harder here than elsewhere

> **"Based in Amsterdam, at least 3 days a week in the office. Work eligibility in the Netherlands required;
> we are not able to sponsor visas in the Netherlands yet."**

Three compounding problems:

1. **Hybrid, 3 days/week in office, no remote option** — there is no 8–12 week remote-start ramp available
2. **No sponsorship** — EU citizenship gives free movement and the right to work, so legally fine, but **physical relocation must happen before the start date**
3. **`CONTEXT.md` constraint:** *"Physical relocation happens only on a signed offer, funded by relocation assistance or an 8–12 week remote-start ramp."* **This JD offers neither**, and there are no relocation savings

**Fails the relocation hard filter on the letter of the posting.** The mitigating move was made at application:
**relocation support was named in the salary answer** rather than left as a separate conversation.

**Timing feasibility:** a Dutch move fits inside the cliff window (sign ≤ ~2027-03-20 for on-site roles, start
≤ 2027-06-01) **if it is funded**. The blocker is funding, not the calendar.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — ✅ no years figure, no staff title; "small, senior, highly technical team"
- [ ] Compensation ≥ €80k — ⚠️ **undisclosed** ("Competitive salary + equity"). Asked **€85,000**. No `market:nl` floor exists in `CONTEXT.md`; €80k applied by analogy (Amsterdam is a comparable-tier market, not a discount market like Madrid)
- [ ] On-site allows 8–12 week remote start / relocation assistance — ❌ **FAILS on the posting**: 3 days/week in Amsterdam, no sponsorship, no relocation mentioned
- [x] No day-one direct GPU / training / serving requirement — ✅ GPU scheduling is **nice-to-have**; ML involvement is "support"
- [x] Has AI workload exposure AND architectural scope — ✅ owns the platform; "partner with engineering to design production-ready architectures"

## Salary rationale: €85,000

- `[INFERENCE]` Amsterdam platform/DevOps at this scope runs **€70–95k**; upper end for senior ownership. No primary-source benchmarking performed
- **€80k floor applied by analogy** — Netherlands added as a new market, treated as comparable-tier
- **€85k sits mid-band** and matches the figure already used for Peak3 (#20)
- **Dutch 30% ruling** may apply (relocation from >150km, France satisfies; salary threshold) — `[INFERENCE]`. Factor into net-pay negotiation rather than trading gross down for it
- **Equity is not income** under the cliff rules, so it cannot substitute for base

Draft used, with the deliberate deviation of naming relocation in the same breath:

> €85,000 total compensation, depending on the scope of the platform ownership and the on-call model, plus
> relocation support for the move to Amsterdam. Flexible on the base/variable split.

## Recruiter-screen answers (ask before any screen)

1. **Does the offer include relocation support** — relocation budget, housing assistance, or a signing bonus covering the move?
2. **Flexibility on the in-office requirement for the first 8–12 weeks** while relocating from France?
3. Compensation band and equity structure (grant size, vesting, strike price)
4. What does "supporting AI/ML workloads" mean in practice — managed serving endpoints, or self-hosted inference on GPU nodes?
5. On-call model and team size ("small, senior" — how small?)

## Questionnaire — received 2026-09-30, returned the same day (Stage → Screening)

MarvelX's first response to the Typeform application was a **questionnaire**, not a rejection and not a call.
Completed and submitted **2026-09-30** — one business day after applying on day 1–2 of the posting, the
fastest human response in the pipeline to date.

**What this establishes**

- The application cleared the first read. Applying the day the role went live did its job on a Typeform
  route, which leaves the employer no ATS to batch-screen from.
- **Screening, not interview.** A written questionnaire is the cheapest screen available; no MarvelX hour has
  been spent yet.
- The relocation conversation has now started on MarvelX's side of the table, not just in the salary field.

**⚠️ Questionnaire content not captured yet** — questions and answers need recording here, because a
questionnaire normally asks exactly the three open items:

1. **Relocation support** — asked or not? This is the hard-filter failure on the posting.
2. **In-office flexibility for the first 8–12 weeks** while relocating from France.
3. **Salary expectation** — if asked and answered, €85,000 is now on record twice.

Until the content is recorded, treat the relocation gate as **unmoved**: no sponsorship, no relocation
budget, no stated remote start.

## Stack overlap and gaps

**Overlap:** Kubernetes (production ownership), Terraform, observability (Prometheus, Grafana, OpenTelemetry, ELK), Docker, Linux/Bash, Helm, multi-cloud, security/compliance (ISO 27001 led).

**Gaps — state plainly:** **GitLab CI/CD** specifically (Drone CI and GitHub Actions are the evidence; "or similar" applies). **GPU scheduling / ML platform** is nice-to-have and would need honest framing. No production Go/Python claim.

## Timeline

- Contacted / applied: **2026-09-29** (Typeform, day 1–2 of posting)
- **Questionnaire received and returned: 2026-09-30** → Stage **Screening**
- Follow-up 1 due (5–7 business days from the questionnaire): **2026-10-07**
- Follow-up 2 due (10–14 business days): **2026-10-16** (final)
- Screen date: —
- Interview dates: —
- Outcome: refused 2026-10-05; no reason given

## Outcome record

- Stage reached: **Screening** — questionnaire sent 2026-09-30, completed and returned the same day;
  **refused 2026-10-05, no reason given**
- Board Stage: **Closed** (set 2026-10-05)
- Rejection reason: **`unknown`** — no reason given. The relocation gate was the *known* structural risk and
  the *predicted* cause, but **the employer did not say so**; recording a prediction as the cause would
  corrupt the funnel. It stays `unknown`
- Duration: 2026-09-29 application → 2026-10-05 refusal, with a human response (questionnaire) at 1 business
  day and the decision 3 business days after that
- Follow-ups: **none sent** — the refusal arrived 2 days before the first follow-up window (2026-10-07);
  the questionnaire reply already contained the strongest possible application of the relocation ask
- **Feedback request: available and drafted — first in the pipeline.** §3 permits exactly one request for
  specific feedback *after a recruiter-screen rejection*, and this is the only refusal so far that followed a
  screening step. Draft: `docs/outreach/marvelx-feedback-request.md`. **Needs Vincent to send it.**
  - This is the only live chance to convert an `unknown` rejection into a **classified** one, and §7 rules 2
    and 4 are inert without classified reasons
  - If they answer, ask specifically whether the in-office/relocation requirement was the blocker; if they do
    not, close it and record the silence
- Timing advantage, still true: applied day 1–2 of a freshly posted role, questionnaire back in 1 business
  day. Application timing was not the problem
- What would have changed the outcome: relocation support or a funded 8–12 week remote start (raised
  proactively in the application and answered at €85,000); a candidate already resident in the Netherlands
- **Unresolved and now lost:** whether the questionnaire answers were ever read, and whether €85,000 was
  above, in, or below their band. Neither was tested by the refusal
- Next action: **send the feedback request (one only), then close.** No further contact, no re-application
