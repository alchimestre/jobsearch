# idnow — AI Platform Engineer (f/m/d)

**Posting:** https://www.arbeitnow.com/jobs/companies/idnow/ai-platform-engineer-berlin-berlin-munchen-bavaria-196219
**Org:** IDnow — European leader in digital identity and fraud prevention; AI-driven SaaS identity
verification (financial services, telecom, travel, gaming). **Offices in Germany, UK, Romania and France**;
backed by **Corsair Capital** and Seventure Partners (private equity, not venture).
**Team:** **"Internal IT"** — see the tier note; this is a corporate-IT/automation function, not product
infrastructure.
**Locations:** **Berlin or Munich, Germany — or Rennes, France**
**Market:** **DE** · **Tier:** **C** (see tier note) · **Channel:** ATS (Arbeitnow → idnow) · **Track:** `bridge`
**Posted:** 2026-10-07 · **Applied:** ✅ **2026-10-07** · **Stage:** Contacted · **Issue:** #29
**Compensation:** **not published.** Berlin floor **€80,000** (§2). Target recommendation below.
**Follow-ups:** 1st due **2026-10-14 → 2026-10-16** · final **2026-10-21 → 2026-10-27**
**jobradar:** uid **`07a91d9debeb76db`** · score **9** · `decision high` · lane `de` · country `de` · mode
`onsite` · reasons `+ai-platform,+platform`.

## Tier note — the title is stronger than the job

The tool's keyword scorer rates this **`high` (9)**, and the title says *AI Platform Engineer*. The body does
not support Tier A or B:

- The department is **Internal IT**: enterprise integration, middleware and automation, not the platform the
  identity products run on.
- The core deliverables are **integrations and middleware code** — GitLab CI/CD pipelines, Terraform on AWS,
  **AI-driven middleware in Node.js and/or Python**, **MCP servers**, data integration via APIs, webhooks and
  messaging.
- Kubernetes/containerisation is explicitly *"a plus"*, not a responsibility. There is no cluster, fleet or
  ML-lifecycle ownership anywhere in the JD.

**Judgement: `tier:c`, `track:bridge`,** so it stays out of the ML-platform conversion cohort. Re-tier at the
screen if it turns out this team genuinely owns the AI-serving substrate — nothing in the posting suggests it.

## Hard-filter checklist (§2)

- [ ] Not Staff/Principal — ⚠️ *"5+ years in IT Integration, DevOps, or Software Engineering"*; ~4 evidenced
      (same soft gap as Filigran #28 and 360Learning #27)
- [ ] Compensation ≥ €80k (Berlin) — **unverified**; see the target below. This is the binding filter
- [x] Remote start / relocation — ⚠️ **on-site in Berlin/Munich or Rennes; no relocation assistance and no
      remote-start language in the JD.** Mitigation: **Rennes in France** makes the move domestic rather than
      cross-border — but see the compensation trap below
- [x] No day-one direct GPU / training / serving expertise requirement — ✅ none
- [ ] Has AI workload exposure AND architectural scope — ⚠️ **partial**: AI/LLM integration and AI middleware
      are real, and there is integration architecture to own; but the role is closer to automation/runbook
      work than to platform ownership

**Verdict: admissible DE-lane bridge, one filter unverified and binding (compensation), one soft-miss
(years).** Not a long-shot; also not a primary-lane application.

## Craft read

| JD requirement | Candidate evidence |
|---|---|
| 5+ yrs integration / DevOps / SWE | ⚠️ ~4 years, DevOps-side strong |
| **GitLab** CI/CD: pipelines, runners, artifacts, orchestration | ⚠️ **GitHub Actions + Drone CI** evidenced; GitLab is a migration, not a claim |
| **Terraform** + **AWS** | ⚠️ multi-environment **Terraform** ✅; **AWS is not the home cloud** (GCP-first, multi-cloud) — the recurring gap (#11, #27) |
| Automation: Python, Bash, JS/Node | ⚠️ Bash strong; Python operational only; **Node.js not evidenced** |
| Data integrations: APIs, webhooks, ETL, queues, event-driven | ✅ real operational experience (event-driven delivery, messaging) |
| **MCP (Node.js) servers** — config, extension development, deployment | ⚠️ **not evidenced**; the 2026 agent/orchestration PoCs are the closest thing |
| AI/ML concepts, model APIs, prompt engineering, LLM integration | ✅ the independent 2026 AI-assist/orchestration work (application layer — the honest framing) |
| Strong backend development (Node/Python) | ❌ **the excluded claim.** `CONTEXT.md` Evidence Boundaries: Python/Go are operational, not production authorship. This JD asks for shipped middleware code |
| Networking, IAM, security best practice | ✅ strong (Teleport, Vault, Kyverno, Cilium, ISO 27001 lead) |
| Docker / Kubernetes (plus) | ✅ core claim |
| Documentation and cross-team collaboration | ✅ evidenced |

**The honest shape:** the DevOps half of this job is a match, the software-engineering half is not. The role
asks for a code-shipping integration engineer; the CV is a production platform/SRE CV with scripting-level
programming. Expect the technical screen to probe Node/Python authorship.

## Compensation — what to specify

Anchors, in order of strength:

1. **§2 floor (binding): Berlin €80,000** — do not go below it.
2. **Employer-disclosed Berlin senior-platform band already seen in this pipeline: €80,000–100,000** (Workist
   #11, Tier A). Berlin seed/scale-up rows this week ran 60–100k (Charly), 60–100k and 50–90k (Quobyte),
   75–80k (PAGNOS, remote).
3. **ERI/SalaryExpert Germany, DevOps Engineer, Sept 2026:** entry **€59k**, average **€85k**, senior
   **€104k**.
4. Levels.fyi Munich SWE median *total* comp ≈ $98.7k — big-tech-weighted, treat as a ceiling signal only.
5. Munich runs roughly **5–10% above Berlin** for the same level; Berlin cost-of-living pressure is lower.
6. Glassdoor's IDnow page reports a company-wide range starting around **€70k** across all German roles —
   `[INFERENCE]`, read from a search snippet, not verified on the page.

**Recommendation**

| If the form is… | Berlin | Munich |
|---|---|---|
| a range field | **€85,000–95,000** | **€90,000–100,000** |
| a single number | **€90,000** | **€95,000** |
| the package is equity-light (likely — PE-owned) | anchor the base at the **top** of the range | same |

- **Why not lower:** the floor is €80k and this is an on-site role with no relocation support; §2 requires a
  non-relocating role to "pay for the missing half of the goal", so pricing at 80–85k is a loss.
- **Why not higher:** 5+ years is asked and ~4 are evidenced, the core deliverable is code the evidence base
  does not claim, and Munich/Berlin *senior platform* medians sit in the mid-80s to mid-90s outside big tech.
  Quoting €105k+ invites a screen-out on level rather than a negotiation.
- **Phrase to use:** *"€85,000–95,000 depending on the level and the full package"* (Munich: 90–100k). It
  names a floor that is above the §2 minimum, leaves room to be raised, and does not anchor at the walk-away
  number.
- **Ask in the same breath:** the bonus (if any) and whether the German entity is the employer as well as the
  French one — idnow has both, and the Rennes option must not be used to apply the French market band, which
  would breach the €80k floor.

**Quoted: €95,000, entered as a single figure on 2026-10-07 with no base/variable split** (reported
2026-10-08). That is exactly the Munich single-number guidance and the top of the Berlin band — defensible
for Munich, a stretch for Berlin at a 4-years-evidenced senior bar. **The one thing to settle in the first
exchange: whether €95k means base.** German "Gehaltsvorstellung" is normally read as base, and idnow's
package may carry a bonus; if €95k is treated as total with a ~10% variable, the base lands near €86k —
above the §2 floor but below the €90k Berlin target. Say "base" explicitly.

## The Rennes trap

The JD offers **Rennes, France**. It looks like the cheapest path (domestic move, no visa, no language risk),
but the §2 floor for France-compatible roles is the **same €80,000**, and French regional platform salaries
outside Paris sit far below the German bands (`[INFERENCE]`). If a recruiter steers to Rennes *and* to French
compensation, the floor breaks. Decide before the call: Rennes is acceptable **only** if it carries a German-level
base, otherwise this becomes a Germany-only application.

## Recruiter-screen questions

1. Which location is actually being hired for — Berlin, Munich, or Rennes?
2. What is the base band for this level in the German entity, and is there a bonus? (Do not volunteer a number first.)
3. How much of the role is *shipping code* in Node.js/Python versus configuration and pipeline work?
4. Is the team Internal IT for the whole group, or does it own anything in the product's AI/platform path?
5. Is an 8–12 week remote start from France possible, or is on-site expected from day one?

## Timeline

- Contacted / applied: **2026-10-07** (Arbeitnow → idnow)
- Follow-up 1 due (5–7 business days): **2026-10-14 → 2026-10-16**
- Follow-up 2 due (10–14 business days): **2026-10-21 → 2026-10-27** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- **Salary quoted: €95,000 (single figure, 2026-10-07; base/variable split not specified)**
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** this is the third row this week where **AWS-primary** experience is the stated requirement
  (#11 Workist, #27 360Learning, #29 idnow) — it is now the single most repeated gap in the DE/FR lanes.
- What would have changed the outcome: —

## Funnel delta

Applications sent +1 (2026-10-07, DE lane). **Bridge row, `track:bridge`** — excluded from the ML-platform
conversion cohort by label, deliberately, despite the title and the tool's score of 9.
