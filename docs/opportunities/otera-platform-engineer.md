# Otera — Platform Engineer (f/m/d) — Remote Europe

**Posting:** https://www.linkedin.com/jobs/view/4468021476/ · Listed as Berlin, **Remote Europe / "work from anywhere"**
**Org:** Otera (otera.ai) — agentic-AI platform for enterprises (Allianz, Siemens, Bayer, Zurich Insurance); €15M Series A (Red River West, Alpha Intelligence Capital, Hoxton Ventures, Lunar Ventures, Stride VC); ~80 staff
**Market:** EU-remote · **Tier:** C (AI is the product; the platform surface is not AI) · **Channel:** ATS (LinkedIn)
**Applied:** ✅ 2026-09-26 (LinkedIn) · **Salary stated: €90,000**
**Stage:** **Closed 2026-10-09** (refused, no reason given, pre-screen)
**Follow-ups:** **none sent, none owed** — the first was due 2026-10-05 (never sent) and the refusal landed the day before the final window opened (2026-10-14)

## Why Tier C, not Tier A/B

Otera *sells* agentic AI. But the responsibilities are multi-cloud infrastructure plumbing, not ownership of
the surface AI workloads run on:

> "build the abstractions, tooling, and infrastructure foundations that allow our engineering teams to
> deploy and operate Otera reliably across multiple cloud environments"

Concretely: GCP/Azure/AWS estates, Terraform, Helm, GKE/AKS/EKS, cloud networking, security partnership,
CI/CD, PostgreSQL/Redis/NATS JetStream, observability. **No ML pipelines, model registry, serving,
training, or model observability appears in the JD.** The §2 test — *own or materially operate the platform
ML/AI workloads run on* — is not met. You would build the roads, not run the models.

→ Tier C, admissible only from the last-resort window (~Apr 2027).

**Honest note:** the role is *good work* — genuine multi-cloud abstraction design ("genuinely multi-cloud
rather than simply replicated across providers"), which matches the architectural-scope criterion and the
Kiln/Cometh/Docaposte evidence. The Tier C call is about the ML requirement, not about role quality.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — ✅ LinkedIn band **Mid-Senior level**
- [ ] Compensation ≥ €80k — **not disclosed** ("Competitive Salary Package"). Ask was **€90,000**; unverified `[INFERENCE]` a Series A at this stage pays a 4-year candidate below that
- [x] On-site allows 8–12 week remote start / relocation assistance — ✅ "Remote Europe", work from anywhere. **Best remote fit seen so far** (pending France eligibility confirmation)
- [x] No day-one direct GPU / training / serving expertise requirement — ✅ none named
- [ ] Has AI workload exposure AND architectural scope — ❌ **AI exposure fails**; architectural scope ✅

## Seniority read

JD asks **5+ years public cloud** and **3+ years Terraform + Kubernetes**. Candidate: four years continuous
infra roles (Dec 2021 → Jan 2026), ~5 years of Terraform/Kubernetes in practice. Bottom-left of their range,
not the middle — which argues against pricing up.

## Salary stated: €90,000

Consistent with SAP Fioneer (#9) and vivenu (#3). Berlin mid-senior platform bands observed this session:
Workist €80–100k · ai-coustics €80–100k · MAIA €75–85k · Matomo €70–80k. €90k is the middle of the range
and above the €80k floor with headroom. Differentiating the number per application at the same tier would
read as uncalibrated.

## Recruiter-screen answers (ask before any screen)

1. **Is France eligible under "Remote Europe"?** Critical — "work from anywhere" often means anywhere the
   entity can payroll. Otera is Austrian-hosted on LinkedIn with a German posting. Cross-border payroll open.
2. What is the compensation band for a 4-year candidate? Does €90k sit inside it?
3. Does the platform team own any AI/ML workload surface (inference, model serving), or purely cloud infra?
4. Contracting entity and employment type for a France-resident hire?
5. On-call model and the multi-cloud split (GCP EU / Azure UAE / AWS US)?

## Timeline

- Contacted / applied: **2026-09-26** (LinkedIn ATS), salary €90,000
- Follow-up 1 due (5–7 business days): **2026-10-05**
- Follow-up 2 due (10–14 business days): **2026-10-14** (final)
- Screen date: —
- Interview dates: —
- Outcome: refused 2026-10-09; no reason given (pre-screen)

## Outcome record

- Stage reached: **closed at Contacted, never screened** (applied 2026-09-26 → refusal reported 2026-10-09;
  **exact refusal date not captured**)
- Board Stage: **Closed** (set 2026-10-09)
- Rejection reason: **`unknown`** — no reason given
- Duration: **~10 business days**, i.e. at the far end of the first follow-up window. Slower than the
  two-day n8n triage refusals, slower than Langdock (~7 days) and Workist (~7 days)
- Follow-ups: **none sent, none owed** — the first was due 2026-10-05
- Outreach: **none for this role** (ATS-only application; no draft exists, so nothing was withheld)
- Feedback request: **not sent** — §3 gates it on a recruiter screen, which this never reached
- **What was lost:** the best remote-geography fit in the pipeline — *"Remote Europe / work from anywhere"*,
  mid-senior band, genuine multi-cloud abstraction design (GCP/Azure/AWS, Terraform, Helm, GKE/AKS/EKS) that
  matched the architectural-scope criterion. It was admissible only from the last-resort window because **AI
  exposure failed** (cloud plumbing, no ML surface), so nothing in the primary lane is lost
- **The two questions that never got asked, and died with it:** (1) **is France eligible** under "Remote
  Europe" — the single blocking unknown, since Otera is Austrian-hosted with a German posting; (2) the
  compensation band behind "Competitive Salary Package". The ask was **€90,000**
- **One unverifiable suspicion, stated as such:** a Series A at ~80 staff with an undisclosed band is where
  the €90k ask is most likely to have been above range — but with no reason given, recording that as the
  cause would be a prediction. `[INFERENCE]`, not a finding
- **The volume signal held:** 141 applicants within a week of posting — the highest-volume posting reviewed
  to date. Applying on day one did not buy a screen
- What would have changed the outcome: a disclosed band clearing €80k and confirmed France eligibility
- Next action: **closed.** No further contact, no re-application

## Funnel delta

Applications sent +1 (2026-09-26, EU-remote lane). **Exits as a pre-screen refusal, `reason:unknown`, with no
salary conversation and no geography answer.** EU-remote lane remains the largest open cohort (#1, #5, #14,
#17, #18, #20, #26) but now has **three closed rows, all `unknown`, all pre-screen** (#10, #19, #21).
