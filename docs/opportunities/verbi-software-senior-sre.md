# VERBI Software — Senior SRE (m/f/x)

**Posting:** https://www.linkedin.com/jobs/view/4475245312/ (LinkedIn, de.linkedin.com mirror)
**Org:** **VERBI Software GmbH** — Berlin, family-owned, founded 2001. Makes **MAXQDA**, the leading software
for qualitative and mixed-methods data analysis (150 years of company history not needed; the anchor is the
product). New cloud/AI product: **MAXQDA Tailwind**. Platform is **AWS-centric (~90%)**, plus 1&1 hosting and a
small on-prem bare-metal setup.
**Market:** **DE (Berlin)** · **Tier:** **C** (non-AI platform role at a legacy software vendor; AI-product
adjacency only, no ML-platform ownership in the JD) · **Channel:** ATS (LinkedIn) · **Track:** `bridge`
**Applied:** ✅ **2026-10-11** (LinkedIn) · **Stage:** **Closed 2026-11-05**
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**

## Hard-filter checklist (§2 + lane filters)

| Filter | Result |
|---|---|
| JD language — English or French | ✅ **PASS** — English |
| Location — FR-based / FR-employable remote / on-site with funded relocation or FR remote start | ❌ **UNRESOLVED — hybrid on-site in Berlin, no relocation or remote-start support stated** |
| Role type — no software-engineering roles | ✅ **PASS** — SRE / DevOps / Platform Engineer; infra work, no product or application authorship |
| Not Staff/Principal | ✅ Senior band, "5+ years" — a years bar, not a scope blow-up |
| Compensation ≥ €80k (Berlin floor) | ⚠️ **NOT STATED** — no band in the JD; unverified |
| AI workload exposure AND architectural scope | ⚠️ **AI-product adjacency only** (MAXQDA Tailwind), not ML-platform ownership → **Tier C** |

**Verdict: location hard filter fails unchecked, so this is a deliberate long-shot.** Vincent applied already,
so the location question moves into the first follow-up rather than a pre-application message. Recorded as a
long-shot to keep the funnel interpretable, per `AGENTS.md`.

## Craft read — JD requirements vs evidence

| Requirement | Evidence |
|---|---|
| 5+ years Platform/DevOps/SRE | ⚠️ four years of continuous infra roles (Dec 2021 → Jan 2026). Lead with scope, not tenure |
| Strong hands-on **AWS** in production | ⚠️ **AWS is the standing gap** — evidence is GCP-first, AWS-adjacent. The platform is ~90% AWS, so this is the largest risk |
| IaC, CI/CD, containers, Linux | ✅✅ Terraform/Ansible, Drone CI, GitHub Actions, Docker, Linux |
| SRE principles, reliable distributed systems | ✅✅ production SRE at Kiln/Cometh/Docaposte; incident response |
| Modernize legacy infra pragmatically and safely | ⚠️ **not directly evidenced** — framing claim; needs a concrete migration story |
| Kubernetes, Terraform, Prometheus/Grafana | ✅✅ all four in **deployed** evidence |
| Cost optimization and security best practices | ✅✅ −25% cloud cost at Cometh; ISO 27001 / HDS hardening |
| One programming language (Python or Go preferred) | ⚠️ operational scripting only — do not upgrade to production-language claim |
| Nice-to-have: hybrid / on-prem | ✅✅ bare-metal K8s at Docaposte (MetalLB, Cilium, HAProxy); 1&1 + on-prem is a direct match |
| Nice-to-have: ISO 27001, SOC 2 | ✅ ISO 27001 (evidence boundary); SOC 2 via HDS/regulated context `[INFERENCE]` |

## Risks

1. **AWS is the core stack and the candidate's weakest cloud.** The JD is explicit: "AWS-centric (~90%)".
   This is the fourth-to-fifth consecutive AWS gap in the pipeline; the highest-weight risk.
2. **Location is unresolved and currently fails.** Hybrid on-site Berlin, no relocation funding stated. This
   alone makes it a long-shot against the France-anchored allocation.
3. **Legacy modernization** is named as a proven-ability requirement and is not yet a concrete CV story.
4. **"Act as a technical mentor"** — formal mentoring is not on the CV; answer from cross-team platform work.
5. **No compensation band** — the Berlin €80k floor is unverified. Ask in writing.

## Questions to put in writing (first follow-up)

1. Is the role open to a France-based candidate, and does VERBI fund relocation or allow an 8–12 week remote
   start from France before a Berlin move?
2. What is the total compensation band for this role?
3. How much of the stack is AWS vs 1&1 / on-prem, and is AWS depth gated at interview?
4. Is MAXQDA Tailwind's infrastructure an ML-serving surface, or product infrastructure only?
5. On-call model and team size?

## Timeline

- Contacted / applied: **2026-10-11** (LinkedIn ATS)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Screen date: — · Interview dates: — · Outcome: **rejected 2026-11-05; reason unknown**

## Outcome record

- Stage reached: Contacted
- Rejection reason (relevance / readiness / compensation / location / unknown): **unknown** — rejected 2026-11-05 by VERBI Software GmbH with a template response that cites the number of qualified applicants and offers no feedback
- The unchecked location filter (hybrid Berlin, no funded relocation or French remote start stated) remains the most likely elimination. The employer did not confirm it, so relevance and compensation stay possible
- **Watch:** if VERBI does not fund relocation and does not allow a French remote start, the location filter
  is the elimination cause and a rejection is expected. Otherwise the elimination set is relevance (AWS) or
  compensation.
- What would have changed the outcome: —

## Funnel delta

Applications sent +1 (2026-10-11) · **DE (Berlin) lane** · `tier:c` · `track:bridge`. Deliberate long-shot
(location hard filter unchecked at application time).
