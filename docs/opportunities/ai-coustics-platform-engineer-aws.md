# ai-coustics — Platform Engineer (AWS)

**Posting:** https://www.linkedin.com/jobs/view/4478225161/ · **Berlin, hybrid** (office + remote)
**Company:** ai-coustics — audio intelligence for voice agents and Physical AI. SDK on customer devices,
models served from their own platform. Customers named in the JD: Perplexity, PolyAI, LiveKit, AssemblyAI,
Telli. Backers: Connect Ventures, Partech, Inovia Capital, angels from HuggingFace, DeepMind, Amazon.
**Stack in the JD:** EKS, Aurora Postgres, ElastiCache, CloudFront, Temporal, Terraform, GitOps.
**Market:** DE (Berlin lane, 10%) · **Tier:** B (platform/SRE at an AI-native; owns the platform that serves
the models) · **Channel:** ATS (LinkedIn) · **Track:** `ai`
**Compensation:** €80,000–100,000 base + stock options (published) — clears the €80k Berlin floor.
**Applied:** ✅ 2026-10-18 · **Stage:** Contacted · **Issue:** #45
**Follow-ups:** 1st due 2026-10-23 → 2026-10-27 · final 2026-10-30 → 2026-11-05
**Evidence version used:** pre-project

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — ✅ "5+ years", senior level, reports to the CTO
- [x] JD language — English (posted on LinkedIn, English body)
- [x] Compensation ≥ €80k (DE) — ✅ published band €80–100k, plus options
- [ ] On-site Germany with relocation assistance or an 8–12 week remote start — ❌ **not stated.** The JD
  offers "Berlin office with a hybrid setup". It assumes residence in Berlin. No relocation clause.
- [x] No day-one direct GPU / training / serving expertise requirement — ✅ infrastructure only
- [x] AI workload exposure and architectural scope — ✅ owns the platform serving "millions of hours each
  month"; single accountable owner, security and cost included

**Verdict: passes on role, language, seniority and compensation. Fails the location sub-filter as written**
because no relocation support is offered and the job is hybrid in Berlin. Logged as a deliberate long-shot
until Vincent confirms relocation or a remote start in writing. Ask in the first screen.

## Craft read

| JD requirement | Candidate evidence |
|---|---|
| 5+ yrs production AWS + Terraform | ⚠️ Terraform ✅ core; AWS is adjacent — the production depth is GCP (Cometh) and hybrid (Kiln) |
| Deep EKS: node pools, IP planning, upgrades, placement | ✅ multi-zone/multi-environment production Kubernetes, upgrades and capacity |
| CKA or AWS Certified CloudOps Engineer — Associate | ❌ **no certification in the evidence record.** Must be acquired or negotiated |
| IAM and least privilege explainable to an auditor | ✅ ISO 27001 led at Cometh; Teleport, Vault, Kyverno, SOPS |
| Single accountable infrastructure owner | ⚠️ stretch — engineer in small teams, not sole owner of a company platform. Kiln and Cometh are the nearest |
| Linux, networking, debugging | ✅ core claim |
| Automate everything, changes reviewed and reversible | ✅ GitOps (Flux, Argo CD), IaC |
| AI coding tools daily | ✅ 2026 AI-assistance proofs of concept |

Bonuses: SOC 2 controls (ISO 27001 ✅ adjacent), Istio (❌), Temporal (❌), GitHub Actions with OIDC (✅
adjacent), cost optimisation (✅ −25%), CloudFront and WAF (⚠️ CDN/edge via nginx, Traefik, Kong).

## Risks

1. **Location is the binding gate.** Hybrid Berlin, no relocation support stated. Vincent is in France and the
   Berlin lane is 10%. Raise it before investing in the process.
2. **No CKA / AWS certification.** The JD makes one mandatory. Either take one (a few weeks) or state a date
   for it.
3. **"Single accountable owner" is an explicit screen.** Answer with the closest real shape: small team,
   end-to-end ownership of the platform surface, not a large SRE team.
4. **AWS depth is the weakest technical claim.** The band expects deep EKS-on-AWS; the evidence is
   Kubernetes-strong but GCP-first.

## Questions for the screen

1. Remote start from France for 8–12 weeks, or relocation assistance?
2. Is the CKA/AWS certification a hard gate, or can a dated commitment replace it?
3. Which AWS accounts and how many EKS clusters today?
4. Who owns SOC 2 evidence now, and what is missing?
5. On-call rotation and expected page volume?

## Timeline

- Contacted / applied: 2026-10-18 (LinkedIn ATS)
- Follow-up 1 due (5–7 business days): 2026-10-23 → 2026-10-27
- Follow-up 2 due (10–14 business days): 2026-10-30 → 2026-11-05 (final)
- Screen date: — · Interview dates: — · Outcome: pending

## Outcome record

- Stage reached: Contacted
- Board Stage: Contacted (issue #45)
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** location is the first gate (hybrid Berlin, no relocation or remote start stated), then the
  mandatory CKA / AWS certification for which no evidence exists.
- What would have changed the outcome: a funded relocation package or an 8–12 week remote start from France

## Funnel delta

Applications sent +1 (2026-10-18) · **DE lane (Berlin)** · `tier:b` · `track:ai` · published band clears the
€80k floor → deliberate long-shot on the location sub-filter, recorded so the funnel stays interpretable.
