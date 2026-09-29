# Doctolib — Staff Site Reliability Engineer (x/f/m)

**Posting:** https://www.linkedin.com/jobs/view/4452466223/ · Berlin, Germany (hybrid, up to 2 remote days/week)
**Market:** DE (Berlin) · **Tier:** C (non-AI SRE bridge; ML-platform surface absent) · **Channel:** ATS
**Applied:** ✅ 2026-09-26 (LinkedIn ATS) · **Follow-ups:** none planned (see below)

## Why this fails on arrival

Two §2 hard-reject filters fire **explicitly in the JD**, so this is not a judgement call:

1. **Staff/Principal band.** Title is Staff; the JD demands **8+ years** in SRE, platform engineering, or
   infrastructure in a large-scale multi-team production environment. §2 rejects Staff/Principal roles or
   roles asking 8+ years. The CV shows four years of continuous infra roles (Dec 2021 → Jan 2026); this gap
   is not bridgeable by framing.
2. **No ML-platform surface.** The SRE team owns "platform reliability" across 170+ applications within
   Platform Engineering. The stack is Kubernetes, Terraform, AWS/GCP, Prometheus, OpenTelemetry, Datadog,
   ArgoCD — no ML pipelines, registry, serving, training, or ML observability. Doctolib's AI is a
   product-layer statement ("we leverage AI ethically across our products"), not a platform surface the
   candidate would operate.

The JD invites under-qualified applicants to apply anyway ("if you don't have the exact profile described
below… we still encourage you to apply"). That invitation is **not** evidence the band flexes — the 8+
years and Staff title remain the binding constraints, and a rejection would arrive as `reason:unknown`,
producing no usable funnel signal.

## Hard-filter checklist (§2)

- [ ] Not Staff/Principal (3–6 yrs expected) — **FAIL: Staff title + 8+ years**
- [ ] Compensation ≥ €80k (Berlin) — **unverified**, not disclosed; moot given the above. `[INFERENCE]` a Doctolib Berlin staff SRE clears the floor
- [x] On-site allows 8–12 week remote start / relocation assistance — ✅ relocation support offered; hybrid (2 remote days). Note: "work from abroad up to 10 days/year" is a perk, **not** a remote start
- [x] No day-one direct GPU / training / serving requirement — ✅ none in scope
- [ ] Has AI workload exposure AND architectural scope — **FAIL: architectural scope ✅, AI exposure ❌**

## Craft read

On craft this is close: Prometheus/OTel/Grafana observability, incident response and postmortem practice,
SLO/error-budget definition for multiple product teams, on-call ownership, Kubernetes and IaC. The candidate
evidence covers most of the technical surface. The mismatch is band and domain, not competence — which is
exactly why applying was a long-shot rather than a targeting error.

## Outcome record

- Stage reached: **closed at Contacted, never screened** (ATS application 2026-09-26 → refusal 2026-09-29)
- Board Stage: **Closed** (set 2026-09-29)
- Rejection reason: **unknown** — no reason given. The label set defines `unknown` exactly as "no reason given"; nothing is inferred here
- Duration: **3 calendar days, 2 business days** — the fastest decision in the pipeline so far (vivenu took 14 calendar / 10 business days). This is a screening-out, not a silence-close
- Follow-ups: **none sent, none now owed.** The refusal arrived 9 days before the first follow-up window (2026-10-05)
- What would have changed the outcome: **not derivable**, and — more importantly — **not worth deriving.** Both hard-reject filters were explicit in the JD before applying: Staff title + 8+ years against 4 evidenced, and no ML-platform surface. This was logged as a deliberate long-shot at application time, so the refusal is the expected cost of the long-shot, not new information about targeting
- Feedback request: **not sent.** §3 prescribes the one feedback request only *after a recruiter-screen rejection*; this never reached screening, so it is out of scope
- **§7 rules 1–3 are not triggered.** Rule 1 covers outreach (not ATS) and needs 3 active weeks; rule 2 requires a screen; rule 3 needs week 6. A 2-day ATS rejection on a known long-shot is noise, not a signal
- Next action: **closed.** No further contact. Removal from the follow-up queue

## Funnel delta

- Applications sent: unchanged (2026-09-26), already counted
- Application-to-screen: this application closes as a **screen miss**
- Screen-to-rejection: unchanged (never screened)
- Rejection-reason tally: **`unknown` +1** — now 2 of 2 closed opportunities are `unknown` (Doctolib + vivenu #3)
- Company note: the low-yield read on Doctolib SRE/Platform postings is **reinforced** by a 2-day screen-out. Do not re-apply to Doctolib SRE postings for the primary lane
- Superseded targeting read (2026-09-26, retained for history): Doctolib SRE/Platform postings are a recurring source of non-matching roles for the primary lane — reliability at scale, no ML platform.

