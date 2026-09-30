# Synthesia — (Senior or Staff) Backend Engineer, AI tooling

**Posting:** https://de.linkedin.com/jobs/view/senior-or-staff-backend-engineer-ai-tooling-at-synthesia-4472733469 (applied via LinkedIn job-alert link)
**Company:** Synthesia — AI video platform for business; London HQ, $4B valuation, Series E $200M (total >$530M); investors incl. Accel, NVentures (NVIDIA), Kleiner Perkins, GV.
**Market:** Berlin (DE) · **Tier:** B (nearest bucket — see caveat) · **Channel:** ATS (LinkedIn → Synthesia)
**Applied:** ✅ 2026-09-29 (LinkedIn, submitted) · **Stage:** Contacted
**Follow-ups:** 1st due 2026-10-06 → 2026-10-08 · final 2026-10-13 → 2026-10-19
**Evidence version used:** pre-project

## Tier caveat

The role is on Synthesia's **Developer Platform team** — internal developer tooling, CI/CD, developer
insights/SDLC metrics, AI-assisted QA and AI-assisted development — and the req is titled **Backend
Engineer**. §2's Tier B ("SRE/platform role supporting ML teams at an AI-native company") is the closest
bucket: AI-native employer, platform function. But the team's customers are all Synthesia engineers, not
an ML-serving organisation, and the role is a software-engineering position rather than SRE/platform
engineering. Recorded as B for funnel continuity; treat as B-boundary.

## Hard-filter checklist (§2)

- [ ] Not Staff/Principal — **FAILS**: req is "(Senior **or Staff**)", asks **7+ years as a software
      engineer, 2–3 of them at senior/staff**. Vincent has ~4 years total (Dec 2021 → Jan 2026). This is
      squarely in §2's reject class "roles asking 8+ years".
- [x] Compensation ≥ €80k (DE) — **PASSES**: "salary starts at EUR/GBP/CHF 130,000 base + equity (RSUs)".
      Clears every floor.
- [x] On-site allows 8–12 week remote start / relocation — **PASSES**: JD prefers in-office *or remote* in
      UK/Germany/Switzerland/Ireland, and "may be able to support remote workers in other locations across
      Europe subject to compliance." France is plausible [INFERENCE]; no relocation needed. Note: "we do
      not relocate people."
- [ ] No day-one direct experience requirement — **FAILS**: core requirement is 7 yrs as a software
      engineer; the process includes a Python implementation exercise. `CONTEXT.md` Evidence Boundaries
      exclude production Python/Go ("operational scripting only").
- [ ] AI workload exposure AND architectural scope — **PARTIAL**: architectural scope is real (owns
      dev-platform technical direction, CI/CD, deprecation/data-driven decisions, 12-month horizon).
      AI workload: it is AI *tooling for engineers* ("AI-powered developer tools", AI-assisted testing),
      i.e. the application layer — not the platform Synthesia's models run on. Strictly, the §2 ML
      requirement is **not** met. [INFERENCE]

## Verdict

A **deliberate long-shot**, consistent with the funnel rule. It clears the two filters that actually gate
application (compensation, remote-from-France) and it is at a legitimate AI-native company — but it fires
the seniority filter hard (7+ yrs vs ~4) and the core-competency filter (production software engineering),
and it does not satisfy the ML-platform requirement that defines the primary lane. Apply-anyway was
defensible as volume; expect a relevance/readiness rejection and record it.

## Readiness gaps this application exposes

1. **Seniority**: 7+ yrs SWE is not flexible-looking; the req's own "2–3 years at senior/staff level" is
   satisfied but the raw-years bar is not.
2. **Language claim**: Python/Go are operational, not production — do not upgrade (see `docs/resume-edits.md`).
3. **Story to lead with if screened**: internal platform ownership and developer-velocity outcomes
   (GitOps delivery, reusable Terraform modules, observability MTTR reduction, cost reduction) map onto
   "shipped infrastructure/tooling that measurably improved developer velocity". Lead with those, not with
   ML-serving claims.

## Hiring process (from the JD — prep if contacted)

1. 30–40 min call with Technical Recruiter
2. 45 min with an Engineering Manager (past projects)
3. 90 min Product Discovery/Implementation — collaborative, **Python**, not Leetcode-style
4. 60 min System Design — usually a real production problem
5. 60 min with leadership — collaboration/growth

## Recruiter-screen questions (ask before any screen)

1. Is the 7+ years of software engineering a hard bar, or can strong platform/infrastructure scope substitute?
2. Is the Python implementation stage pass/fail on production-style code, or on problem decomposition?
3. Total compensation including RSU grant size/vesting and the location differential (Berlin vs remote)?
4. Remote from France — is that within the "other locations across Europe" clause, and what is the entity
   (OysterHR) and start lead time?
5. Which team(s) does Developer Platform serve, and does it own anything on the ML/AI serving or training path?

## Timeline

- Contacted / applied: 2026-09-29 (LinkedIn)
- Follow-up 1 due (5–7 business days): 2026-10-06 → 2026-10-08
- Follow-up 2 due (10–14 business days): 2026-10-13 → 2026-10-19
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: **closed at Contacted, never screened** (ATS application 2026-09-29 → refusal same day)
- Board Stage: **Closed** (set 2026-09-29)
- Rejection reason: **`unknown`** — no reason given. The note *predicted* relevance/readiness; no reason was
  offered, so nothing is inferred and nothing is recorded as the cause. Recording the prediction instead of
  the fact would corrupt the funnel
- Duration: **refused same day as application** — a resume-screen-out. Faster even than Doctolib (2 business
  days), consistent with the pattern for roles failing explicit seniority bars
- Follow-ups: **none sent, none owed** (refusal arrived before the first window, 2026-10-06)
- Feedback request: **not sent.** §3 prescribes the one feedback request only after a *recruiter-screen*
  rejection; this never reached screening
- **§7 rules 1–3 not triggered.** Rule 1 covers outreach (not ATS) and needs 3 active weeks; rule 2 requires
  a screen; rule 3 needs week 6
- Recorded cause of the deliberate long-shot (predicted **before** applying, not derived from the refusal):
  **two hard filters fired explicitly in the JD** — `(Senior or Staff)` asking **7+ years as a software
  engineer** (2–3 at senior/staff) against ~4 evidenced, and a **Python implementation exercise** against an
  evidence boundary excluding production Python claims. **Compensation (€130k base + RSUs) and
  remote-from-France both passed**, so neither was the constraint
- What would have changed the outcome: seniority and production software-engineering evidence. The
  `ml-platform-on-k8s` artifact addresses Python but not the years bar
- Next action: **closed.** No further contact

## Funnel delta

- Applications sent: unchanged (2026-09-29), already counted
- Application-to-screen: closes as a **screen miss**
- Rejection-reason tally: **`unknown` +1 → 3 of 3 closed opportunities are `unknown`** (vivenu #3, Doctolib
  #6, Synthesia #16)

### ⚠️ The `unknown` rate is now a real measurement problem

Three rejections, three silences, all pre-screen. §7's diagnostic rules 2 and 4 (screen-to-rejection,
compensation mismatch) both depend on classified rejection reasons, and §3's single feedback request is
available only *after a recruiter screen*. **No pre-screen refusal can ever be classified.**

Consequence: the funnel can currently distinguish *nothing* about why applications fail. Every closed row is
uninformative. Two structural implications worth raising at the Friday review:

1. **Pre-screen volume produces no learning.** Volume only pays off if some applications reach screens. The
   primary-lane roles (#12 Langdock, #11 Workist, #9 SAP Fioneer) are where a screen would generate signal.
2. **Deliberate long-shots are now a measurable tax.** Doctolib and Synthesia both failed on seniority bars
   that were visible in the JD before applying. Neither produced information, and both consumed an
   application. Consider tightening the seniority filter rather than spending volume on roles that fire
   `8+ years`/`Staff` explicitly
