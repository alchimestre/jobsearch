# Otera — Platform Engineer (f/m/d) — Remote Europe

**Posting:** https://www.linkedin.com/jobs/view/4468021476/ · Listed as Berlin, **Remote Europe / "work from anywhere"**
**Org:** Otera (otera.ai) — agentic-AI platform for enterprises (Allianz, Siemens, Bayer, Zurich Insurance); €15M Series A (Red River West, Alpha Intelligence Capital, Hoxton Ventures, Lunar Ventures, Stride VC); ~80 staff
**Market:** EU-remote · **Tier:** C (AI is the product; the platform surface is not AI) · **Channel:** ATS (LinkedIn)
**Applied:** ✅ 2026-09-26 (LinkedIn) · **Salary stated: €90,000** · **Follow-up 1 due:** 2026-10-05 · **Follow-up 2 due:** 2026-10-14 (final)

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
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- Watch: **141 applicants within one week** — highest-volume posting reviewed to date, on an undisclosed
  salary at a Series A. Expect either a fast screen or silence.
- What would have changed the outcome: an ML-serving/inference surface in the responsibilities, or a
  disclosed band clearing €80k
