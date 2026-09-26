# Langdock — (Senior) Platform Engineer (m/f/d)

**Posting:** https://www.linkedin.com/jobs/view/4451363314/ · Berlin, **in-office** at Greifswalder Strasse 212
**Org:** Langdock — AI platform for enterprise AI adoption; 10,000+ companies; **$40M ARR** with a small team; customers include Merck (33,000 MAU), Merck's "myGPT Suite", BASF, Axel Springer, SumUp, Deutsche Bahn, Eppendorf
**Market:** DE (Berlin) · **Tier:** **A** — strongest fit in the pipeline · **Channel:** ATS (LinkedIn)
**Applied:** ✅ 2026-09-26 (LinkedIn) · **Comp (employer-disclosed): €90,000–140,000 gross + equity**
**Follow-up 1 due:** 2026-10-05 · **Follow-up 2 due:** 2026-10-14 (final)

## Why this is the best-targeted role so far

The JD's own framing maps onto the positioning thesis almost line for line:

> "Platform Engineers own the shared capabilities that Langdock's products are built on. They treat these
> capabilities as **internal products**: defining the interfaces other teams build against and remaining
> accountable for their reliability, evolution, and operation over time."

The entry wedge — *making the platform that hosts models observable, resilient, reproducible, cost-aware* —
is the job description. Specifically:

- **The Model Gateway** — "one **inference boundary** for every Langdock product, with a model-agnostic API
  over managed and customer-provided models… provider adapters, routing across accounts and regions, rate
  limits, bounded fallback, streaming safety, usage tracking, and a control plane." This is serving-path
  reliability ownership, stated outright.
- **A durable agent runtime** — separating runtime from product state, durable runs that survive process
  death, recovery without repeating committed tool calls, deterministic context reconstruction. SRE
  reasoning applied to LLM infrastructure.
- **Production confidence for shared systems** — reusable load testing for HTTP/gRPC/streaming, structured
  logging without user content or PII, **online database changes for PostgreSQL tables measured in hundreds
  of gigabytes or terabytes**.
- **Code execution as a shared service** — permission model, resource budgets, operational boundary for
  untrusted JS/Bash/Python execution.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — ✅ explicitly **3–6 years** ("we generally expect this judgment to come from at least three to six years of full-time experience"); Mid-Senior band. Candidate has four — **dead centre**
- [x] Compensation ≥ €80k (DE) — ✅ **PASS, employer-disclosed €90–140k**; candidate's €90k ask sits at the **bottom** of the band. Clearly the best band in the pipeline
- [x] On-site / remote-start — ❌ **in-office**, "We do not currently sponsor visas", "You need an existing right to work in Germany". **Estonia/EU citizen needs no visa ✅, but the role is on-site in Berlin — the 8–12 week remote-start-from-France requirement is NOT satisfied by the posting.** This is a physical-relocation role from day one
- [x] No day-one direct GPU / training / serving expertise — ✅ none required; Kubernetes/Terraform/networking/databases/queues are the asks
- [x] Has AI workload exposure AND architectural scope — ✅ **PASS, strongly.** Model Gateway, agent runtime, authorization service, integration/tool platform

⚠️ **The one real problem: on-site from day one, no remote start offered.** Per §2 this is a hard-reject
condition ("On-site roles without relocation assistance or an 8–12 week remote start"). No relocation
package is mentioned in the JD during work-authorised. Candidate is an EU citizen so work authorisation is
fine; the missing piece is the relocation/ramp. **Raise it at first contact** — it is the single thing that
could end this process, and it is better to know at screen than at offer.

## The two application questions (answered by Vincent, text not recorded here)

The form asked:

1. *"After exploring Langdock, what part of the product or its underlying platform would you most like to
   improve, and why?"*
2. *"What platform, backend, or infrastructure work are you most proud of? What made your work exceptional?"*

Q2 was **not** resolved before submission — the grilling session stopped at the first branch (which role
holds the proudest-work story; recommendation was Kiln, with a specific incident needed rather than a scope
claim). Q1 depends on Q2, since Q1 is Q2 pointed at Langdock's product surface. Vincent submitted without
completing the grilling.

**To retrieve the submitted text:** the application went through LinkedIn; the answer text will be in the
submission confirmation email or the sent-application record. Recover it and store it here so the answers
can be reused in the interview and kept consistent with what was claimed.

## Why the questions matter more than usual

Both questions map onto JD language, so weak answers are visible:

- Q2 tests *"Given an underspecified systems problem, you identify the most important invariant, decide
  where to go deep, and defend what you deliberately leave out."* It wants the invariant, not the tool list.
  `docs/writing-style.md` rule: outcomes and ownership, no tool enumeration.
- Q1 tests whether the candidate read the JD. The strongest honest answer names a **specific named platform
  area** (Model Gateway / agent runtime / authorization migration / code-execution service) and reasons
  about the invariant, rather than "I'd improve observability".

## Recruiter-screen answers (ask before any screen)

1. **Is an 8–12 week remote start from France possible, or is relocation support offered?** The JD says in-office and no visa sponsorship; work authorisation is already held as an EU citizen, so this is purely a ramp/relocation question. **Blocking.**
2. Level and band: where would €90k land on the €90–140k ladder, and what scope defines each level?
3. Which platform area would the candidate start in (Model Gateway, agent runtime, authorization, code execution, integration platform)?
4. Team shape: squad size, on-call model, and who owns shared services operationally?
5. Kubernetes estate: GCP/AWS/Azure **and on-premises** — what does the on-prem deployment look like in practice?

## Stack overlap and gaps

**Overlap:** Kubernetes (incl. on-prem — matches Kiln and Docaposte bare-metal), Terraform (+**Terragrunt**,
which appears in `docs/tooling-inventory.md` under unplaced tools), PostgreSQL, Redis, Datadog (used at
Kiln), networking, queues.

**Gaps (state plainly, do not overclaim):**
- **TypeScript / Node.js** — the JD wants strength here, and "You are strong in TypeScript and Node.js". Not in current evidence.
- **Go** — "Experience with Go is useful; willingness to work in it matters more." Conditional Go work exists in the plan; no production Go claim is defensible yet.
- **Bazel monorepo, Protobuf/gRPC, SpiceDB, BullMQ** — new.
- The JD does allow for this: *"You should be familiar with most of this. We trust you to pick up the rest quickly."*

## Timeline

- Contacted / applied: **2026-09-26** (LinkedIn ATS)
- Follow-up 1 due (5–7 business days): **2026-10-05**
- Follow-up 2 due (10–14 business days): **2026-10-14** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Highest-priority application in the pipeline.** Tier A, disclosed band topping the pipeline at €90–140k,
  best seniority match (3–6 yrs vs. 4), and the JD describes the target role. If Langdock responds, it
  outranks everything else including Workist and SAP Fioneer.
- Watch: **200+ applicants within 2 days** — the highest-competition posting reviewed to date. Application
  strength matters more here than volume.
- What would have changed the outcome: a remote-start option (the on-site requirement is the main structural
  risk)

## Funnel delta

Applications sent +1 (2026-09-26, DE lane). Primary-lane eligible (Tier A) — counts toward ML-platform
conversion alongside #9 SAP Fioneer and #11 Workist.
