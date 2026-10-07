# 360Learning — Senior DevSecOps Engineer

**Posting:** https://jobs.lever.co/360learning/1bc6a2b3-ff85-498f-a0c1-b8a463fc992e · Lever id
`1bc6a2b3-ff85-498f-a0c1-b8a463fc992e` · **Paris, Remote** — JD: *"full remote work possible anywhere in
France"*
**Org:** 360Learning — French collaborative-learning (LMS) SaaS, founded 2013, **$240M raised, 400+
employees**, 1,500–1,700 organisations on the platform. **Azure + Kubernetes**, **ISO 27001:2022 and SOC 2
Type II certified**.
**Team:** the Security & IT team — described as *"small, senior … broad scope: information security,
compliance, infrastructure governance and internal tooling"*, with dual audit accountability. Named contacts:
**Guillaume Seigneuret, CISO and "Hiring Coach"** (quoted in the JD), a **Head of Security**, a **Head of
DevOps**, a Security Engineer, DevOps engineers.
**Market:** **FR-bridge** · **Tier:** **C** · **Channel:** ATS (Lever) · **Track:** `bridge`
**Created:** **2026-10-06** — applied the next day.
**Compensation:** **not published** — *"base salary, a variable component and equity"*. France-compatible
floor is **€80,000** (§2). **Unverified.**
**Applied:** ✅ **2026-10-07** (Lever) · **Stage:** Contacted · **Issue:** #27
**Follow-ups:** 1st due **2026-10-14 → 2026-10-16** · final **2026-10-21 → 2026-10-27**
**jobradar:** no store row. Reconcile by the Lever id above.

## Admission note — a bridge row admitted on its weakest clause

Two §2 clauses apply and only one of them admits this:

- **ML-preference-not-a-gate (2026-09-29):** *"A role with no ML surface is admissible when it clears the
  compensation floor, the seniority band, the start-date constraint, and offers architectural scope — Web3
  infrastructure roles by default, other platform/SRE roles case by case."* This is a *case by case*, and it
  clears three of four: architectural scope (roughly half the role is greenfield build owned end to end),
  start-date (remote in France, no relocation), seniority (5+, one year short — same soft gap as Filigran).
  Compensation is unverified.
- **Bridge Opportunity definition (stricter):** *"a France-based or EU-remote role considered only when it
  materially strengthens AI-infrastructure positioning or enables later relocation."* This role is **security
  engineering**, not platform engineering, and it does **not** build ML-platform evidence.

**Why it is still admitted, stated honestly:** it strengthens the **regulated / compliance-heavy segment** of
AI-infrastructure work, which is not a side quest — it is a recurring hard requirement in this exact pipeline
(Filigran: FedRAMP and SecNumCloud hardening; the sovereign-deployment and on-prem-appliance shapes across the
France lane). **ISO 27001 and SOC 2 audit ownership, automated audit evidence, and vulnerability management
at scale** are transferable, in-demand evidence of that kind, and the candidate has the strongest possible
starting position on it (led ISO 27001 at Cometh; HDS-regulated healthcare at Docaposte). It is an
**income-and-evidence** application, not a positioning pivot — and it does not change the primary lane.

**Flagged for the Friday review:** two of this week's three France-lane applications (this one and Filigran #28)
are security-flavoured, and the second is the stronger fit. Deciding whether the France lane is drifting
toward security/compliance infra — and whether that is where the evidence actually points — is a targeting
question, not a logging one.

## Hard-filter checklist (§2)

- [ ] Not Staff/Principal — ⚠️ **"5+ years"**; ~4 evidenced, same soft gap as Filigran
- [ ] Compensation ≥ €80k (France-compatible) — **unverified**, no band published; equity is explicitly part
      of the package, which makes the base the question to ask
- [x] Remote start / relocation — ✅ **moot**: full remote anywhere in France
- [x] No day-one direct GPU / training / serving expertise requirement — ✅ none asked
- [ ] Has AI workload exposure AND architectural scope — ❌ **FAILS on AI exposure**: the platform is an LMS
      and the role is infrastructure security. Architectural scope ✅ (owns the infra scope of vulnerability
      management, detection content as code, audit-evidence automation, credential elimination on critical
      paths)

**Verdict: a deliberate bridge row — one explicit filter failure (AI exposure), two unchecked (years,
compensation), admitted for income in lane #1 plus regulated-environment evidence.** Logged on the same terms
as the Web3 rows: tagged so it cannot flatter the ML-platform conversion rate.

## Craft read — real matches, and a genuinely empty quadrant

| JD requirement | Candidate evidence |
|---|---|
| 5+ yrs infra/cloud/platform **with strong security focus** | ⚠️ ~4 years, and the security focus is real: **ISO 27001 implementation led at Cometh**, HDS-regulated healthcare at Docaposte, hardened crypto infrastructure at Kiln |
| Production Kubernetes: **RBAC, network policies, admission controllers, secrets handling, workload identity, runtime security** | ✅ mostly: Cilium network policy, Kyverno admission control, Vault/SOPS/External Secrets, Teleport, cert-manager. ⚠️ **workload identity** and **runtime security** (Falco-class tooling) are not evidenced |
| Cloud, *"ideally Azure. Strong AWS or Google Cloud … with a genuine interest in converting"* | ⚠️ **GCP-first**; AWS adjacent. **Azure/AKS is the recurring gap** — the same one flagged on Workist (#11). The JD explicitly accepts a converter |
| IaC: Terraform, GitOps workflows, CI/CD | ✅ multi-environment **Terraform**, **Flux** and Argo CD GitOps, GitHub Actions |
| Scripting: **Python or Go**, plus shell; *"comfortable reading and writing code, opening pull requests on repositories owned by other teams"* | ⚠️ Bash strong; **Python/Go operational, not production claims** (evidence boundary). *"Open PRs on other teams' repos"* is a working-style match, not a language match |
| **Log analysis and investigation: cloud audit logs, query languages, correlation across identity, network and application sources** | ⚠️ **the weakest match.** Observability stack is evidenced (Prometheus, Grafana, Loki, OpenTelemetry, ELK) but **SIEM query languages and detection/correlation work are not** |
| Audit evidence and controls (ISO 27001 / SOC 2) | ✅ **ISO 27001 lead at Cometh** is the single strongest line in the application. ⚠️ **SOC 2 Type II not evidenced** |
| Vulnerability management ownership | ⚠️ adjacent (hardening work, CVE response in operations); not owned end to end before |
| Fluent English (B2+) / FR | ✅ native French, professional English |

**The empty quadrant:** this is a *security operations* role. Detection content as code, SIEM connector
coverage, honeypots, alert triage and incident investigation are new surface — and the interview process
tests exactly that, with a **live exercise: incident investigation, or review of an insecure infrastructure
configuration**. The second variant is winnable on candid evidence (hardening, network policy, secrets,
Kubernetes configuration review). The first is not, without preparation.

## Risks, stated plainly

1. **It is not the target role.** Security engineering for an LMS. No ML surface, no platform ownership, and
   the CV trajectory becomes "reliability → security" rather than "reliability → ML platform".
2. **The interview bar is security depth**, including a live incident-investigation variant that the evidence
   base does not currently reach.
3. **Azure/AKS** — unavoidable conversion question, identical to #11.
4. **Two of the four interview stages are security-specific** (Head of Security in both the discovery and
   live-exercise stages) — this will not be carried by SRE stories alone.
5. **Compensation unpublished with equity in the mix**; the France floor is €80k and this must be asked
   immediately.

## Recruiter-screen questions (ask before any screen)

1. Total compensation for this level — base range, variable target and equity — against the €80k floor?
2. Which variant is the live exercise likely to take — incident investigation or insecure-configuration
   review? (It changes what is worth preparing.)
3. Is Azure depth required, or is GCP-first acceptable with conversion on the job, as the JD allows?
4. How much of the role is greenfield build versus audit/maintenance work, and what does "roughly half is
   greenfield" mean concretely today?
5. How do the security team and the platform team split ownership — who carries the on-call pager for
   infrastructure alerts?

## Outreach option (named contact)

The JD quotes the **CISO, Guillaume Seigneuret**, as "Hiring Coach" — a rare, named decision-maker for a role
with no outreach message yet. The devsecops/ISO-27001 evidence is the one thing Vincent can claim that most
applicants cannot. Not drafted here; say the word and it will be, in applicant voice per
`docs/writing-style.md`.

## Timeline

- Contacted / applied: **2026-10-07** (Lever)
- Follow-up 1 due (5–7 business days): **2026-10-14 → 2026-10-16**
- Follow-up 2 due (10–14 business days): **2026-10-21 → 2026-10-27** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** this is the pipeline's clearest case of *apply-then-discover*: a security role logged as a bridge,
  where the interview content and the compensation are both unknown.

## Funnel delta

Applications sent +1 (2026-10-07, FR lane). **Bridge row, `track:bridge`** — excluded from the ML-platform
conversion cohort by label, on purpose.
