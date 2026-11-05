# Atlantic VC portfolio venture — Platform Engineer (gn) @ AI Efficiency Venture, Berlin

**Posting:** https://jobsatlanticvc.recruitee.com/o/platform-engineer-gn-ai-efficiency-venture-berlin · Recruitee
offer id **2776762** · **Berlin, Germany · on-site, five days a week**, no remote option stated
**Org:** An **unnamed Atlantic (Atlantic Labs) portfolio venture at pre-seed**, hiring its first platform
engineers. Product: a **routing layer across closed and open-weight models behind one API** — requests split
into components, routed to the right model within a cost budget, fine-tuned on customer data, checked against
agreed quality standards. Team: founder, CTO, founding AI engineer. *"People already waiting to use it."*
**Market:** **DE** · **Tier:** **A** (see the tier note) · **Channel:** ATS (Recruitee) · **Track:** `ai`
**Posted:** not shown · **Applied:** ✅ **2026-10-09** · **Stage:** Contacted · **Issue:** #30
**Compensation:** **not published.** Berlin floor **€80,000** (§2); equity is described as "meaningful" — at
pre-seed that is a lottery ticket and **cannot** be counted toward the floor.
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**
**jobradar:** no store row for this posting; reconcile by the Recruitee offer id above.

## Tier note — Tier A, on the strongest reading yet seen

Per §2, Tier A is the role that **owns or materially operates the platform the AI workloads run on**. This JD
states it almost line for line:

> **"European infrastructure and model serving:** build and operate our cloud infrastructure, including **the
> GPU capacity used to serve open-weight models**."
> *"You will also work alongside our founding AI engineer on **evals, embeddings and open-weight model
> serving**."*

Plus the LLM **gateway and router**, cost-per-call accounting, token-cost visibility, and agent infrastructure
(tool calls, cost limits, human approvals, interruptible runs). That is the ML-serving surface with
infrastructure ownership attached — Tier A, not the "SRE at an AI company" reading of Tier B.

**Counter-argument, recorded:** the role is also, plainly, the **LLM gateway and billing plumbing** at a
pre-seed company, and the surface is thin — one founder, a CTO and a founding AI engineer. `track:ai` puts it
in the same cohort as Workist (#11) and Langdock (#12). Judgement: **tier:a** stands, because GPU serving
capacity and the routing/evals layer are owned rather than used. Raise at the Friday review if that reads as
generous.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — ✅ **"several years of backend engineering with real users, typically three to six,
      and meaningful ownership"** — inside the 3–6 band, and the first row where the candidate's ~4 years sit
      in the *middle* of the stated range rather than under it
- [ ] Compensation ≥ €80k (Berlin) — ⚠️ **unverified**, no band. Pre-seed + "meaningful equity" is exactly the
      shape where the base lands under the floor; equity is not income here
- [ ] On-site DE with 8–12 week remote start or relocation assistance — ❌ **unverified and unsupported on the
      letter of the JD**: *"based in our Berlin office five days a week"*, no remote start and **no relocation
      assistance mentioned**. Same structural gap as the other Berlin on-site rows, worse than most because
      pre-seed rarely funds a move
- [x] No day-one direct GPU / training / serving expertise requirement — ✅ **explicitly a plus, not a gate**:
      *"Kubernetes experience is useful, particularly for our GPU infrastructure"*, *"familiarity with LLMs,
      embeddings, evals, model serving"*. The GPU claim stays out of the CV, which is what the evidence
      boundary requires
- [x] AI workload exposure AND architectural scope — ✅ **the strongest pass in the pipeline**: AI exposure is
      the role's core, and ownership is explicit (*"take capabilities from design through to production,
      thinking through their APIs, failure modes, deployment, observability and ongoing operation"*)

**Verdict: admissible — the highest AI-infrastructure surface logged to date, with the best seniority fit
(3–6 asked, ~4 evidenced). Two filters unverified and both binding: compensation and relocation funding.**

## Craft read

| JD requirement | Candidate evidence |
|---|---|
| Several years backend **with real users**, 3–6, meaningful ownership | ✅ ~4 years production ownership; the band fits |
| **Strong Python** — async, typing, testing | ❌ **the gate.** `CONTEXT.md`: Python is operational, not production authorship. Every backend here is Python/FastAPI/Pydantic. Expect a code screen |
| Postgres, Redis, queues | ✅ data stores and messaging per `docs/tooling-inventory.md`; event-driven delivery |
| **Terraform** | ✅ multi-environment Terraform |
| **Kubernetes, particularly for GPU infrastructure** | ✅ production K8s, multi-environment/multi-zone + bare-metal (Docaposte). ⚠️ **GPU workload** operation: GPU-adjacent, not direct ownership |
| Networking, tenant isolation, secrets/KMS, IAM | ✅ **strong** — Cilium network policy, Vault/SOPS/External Secrets, Teleport, Kyverno, ISO 27001 lead |
| **Cost optimisation, measuring savings** | ✅ **the standout match** — cost-reduction track record (Cometh, cloud spend −25%); the JD wants caching, history compression, model selection with measured savings |
| Observability, reversible migrations, safe releases | ✅ Prometheus/Grafana/Loki/OpenTelemetry, GitOps rollouts (Flux, Argo CD), incident response |
| **Practical agentic engineering** — use coding agents, develop and evaluate their workflows, review what they produce | ✅ **a rare direct ask for the 2026 AI-assist/orchestration work** — the one AI claim defensible today, framed at the application layer as the evidence boundary requires |
| ML systems: LLMs, embeddings, evals, serving, fine-tuning, streaming, token costs | ⚠️ conceptual plus application-layer PoCs; no production ML system. The JD says *"working understanding"* and *"fundamentals"* — the honest level |
| Scaleway, LiteLLM, Langfuse, Zitadel, pgvector, Next.js/TypeScript | ⚠️ none evidenced (Scaleway is a French sovereign cloud — GCP/AWS-adjacent knowledge transfers, but it is a new platform) |
| Fluent English; German a plus | ✅ |

**The shape in one line:** infrastructure, cost discipline, secrets and reliability are a direct match; the
**Python-backend authorship** and the ML-serving layer are not. At a pre-seed company whose entire backend is
Python, the first filter is a code screen.

## Risks, stated plainly

1. **Pre-seed.** No funding disclosure beyond "backed by Atlantic at pre-seed", no customers in production yet
   (*"people already waiting to use it"*). On the income cliff, a pre-seed base under €80k with equity as the
   upside is the worst possible compensation shape — ask the base **first**, in writing.
2. **No relocation support mentioned**, on-site five days a week, starting ASAP. Moving to Berlin is
   self-funded unless they say otherwise. That is the second binding unknown.
3. **Python authorship** is the stated core skill and the known evidence gap.
4. **Unnamed employer.** The venture has no public name — due diligence is impossible, and the interview will
   be the only way to learn what the company actually is. Ask directly and early.
5. **Intensity, honestly advertised:** *"We work with intensity, move quickly from decisions to execution"*,
   *"an ambitious timeline"*. Start-up pace claims are normal; at pre-seed with three named people they are
   literal.

## What is genuinely attractive

- **The only row in the pipeline where the AI-infrastructure claim is the job itself** rather than an
  adjacent surface, and the one row whose stated seniority band the candidate sits inside rather than under.
- **Cost work is a first-class responsibility** — the CV's cost evidence (cloud spend −25%) maps onto the
  product's own thesis.
- **Agentic engineering is a hiring criterion**, and the 2026 harness/orchestration work is real, current and
  demonstrable.
- Founder-adjacent ownership at a stage where platform decisions shape the product.

## Recruiter/founder questions (ask in writing, before any call)

1. **Base salary band for this role**, and how much of the package is equity? (§2 floor is €80k; equity at
   pre-seed is not income.)
2. **Relocation:** is there support for moving to Berlin, and can the first 8–12 weeks start remotely from
   France?
3. What is the venture's name, incorporation and current funding — and how many months of runway?
4. How much of the work is **shipping Python services** versus infrastructure and platform engineering?
5. Who is actually in production on the platform today, and what does "people already waiting to use it" mean
   concretely?
6. Does the GPU capacity live on Scaleway, and is it operated by this team or rented/managed?

## Timeline

- Contacted / applied: **2026-10-09** (Recruitee, Atlantic venture board)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Salary: **not stated in the application** (no figure was submitted — unlike idnow #29 and Otera #10)
- Rejection reason (relevance / readiness / compensation / location / unknown): **unknown** — rejected 2026-11-05 by the Atlantic/FoodLabs Talent & Venture Development team, which states it cannot give individual feedback
- Rejection named the role "Agentic Platform Engineer (gn) @ AI Venture, Berlin". Mapped to this record on portfolio, city and the `(gn)` marker; the tracked title reads "Platform Engineer (gn) @ AI Efficiency Venture" [INFERENCE: same venture, retitled in the application form]
- The on-site Berlin requirement with no relocation support was the known unchecked filter. The template gives no cause, so the rejection does not confirm location as decisive
- **Watch:** the two binding unknowns (base, relocation) are both answerable by the employer in one message.
  Per the new rule recorded 2026-10-09, they go in the **first follow-up**, not into a recruiter call that may
  never happen.
- What would have changed the outcome: —

## Funnel delta

Applications sent +1 (2026-10-09, DE lane). **Tier A, `track:ai` — counted toward the ML-platform conversion
cohort**, unlike the four bridge rows logged this week (#22, #25, #26, #27, #29). With Workist #11 closed, this
is the pipeline's only live Tier A row.
