# Filigran — Senior Platform Engineer

**Posting:** https://jobs.ashbyhq.com/filigran/db3ab63a-73c2-42aa-9ca1-704bc66afc20 · Ashby id
`db3ab63a-73c2-42aa-9ca1-704bc66afc20` · **Location: France** · `isRemote: true`, `workplaceType: Remote`
— **remote-first**, not "remote in some other country"
**Org:** Filigran — French cybersecurity company, founded 2022, open-source first (OpenCTI, OpenBAS). Product:
XTM, an *"agentic Continuous Threat Exposure Management"* platform (threat intelligence, exposure validation,
cyber-risk reduction). Goes to market as SaaS, in **sovereign and regulated environments**, and as an
**on-premises appliance** customers run themselves.
**Team:** Platform Engineering, **~15 people across three verticals**; reports to the **Director of Platform
Engineering**; works with a Technical Product Manager, staff engineers, dev teams and customer support.
**Market:** **FR-bridge** · **Tier:** **B** (SRE/platform at an AI-forward, agentic-product company — see the
tier note) · **Channel:** ATS (Ashby) · **Track:** `ai`
**Posted:** **2026-10-06** — applied the next day. Best timing of any application in the pipeline.
**Compensation:** **not published.** France-compatible floor is **€80,000** (§2). French scale-up senior
platform bands are `[INFERENCE]`; **unverified**.
**Applied:** ✅ **2026-10-07** (Ashby) · **Stage:** Contacted · **Issue:** #28
**Follow-ups:** 1st due **2026-10-14 → 2026-10-16** · final **2026-10-21 → 2026-10-27**
**jobradar:** no store row. Reconcile by the Ashby id above.

## Tier note — `tier:b`, `track:ai` (flagged for review)

- The team **owns the Kubernetes substrate behind an agentic product**, in SaaS, sovereign/regulated and
  on-premises shapes. That is not "AI infrastructure" in the ML-serving sense, so it is not Tier A.
- But three stated responsibilities are AI-infrastructure work in the agent-ops sense: *"Use AI agents
  throughout your daily work … while staying accountable for everything you review and ship"*, *"Help design
  **the playground for agents**: make our repositories, documentation and guardrails agent-friendly, so other
  teams can contribute safely"*, and *"Take problems from first signal to shipped solution: scope them,
  propose an approach, and document your decisions so others (humans and agents alike) can build on them."*
- **Judgement call, flagged explicitly:** `track:ai` puts this in the same conversion cohort as Langdock
  (#12, Tier B) rather than with the `track:bridge` rows. Raise at the Friday review if that reads as
  generous — the workload has no ML/GPU surface, and the AI content is agentic-workflow and guardrail
  engineering rather than model serving.

## Hard-filter checklist (§2)

- [ ] Not Staff/Principal — ⚠️ **"5+ years as a Platform Engineer, SRE, DevOps or Cloud Engineer"**; ~4
      evidenced. **One year short on the letter of the JD** — the only filter this fails outright, and it is
      a soft one (the band is 5+, not 8+ or staff)
- [ ] Compensation ≥ €80k (France-compatible) — **unverified**, no band published
- [x] Remote start / relocation — ✅ **moot and the strongest in the France lane**: the role is remote-first
      with no relocation requirement, so no ramp is needed
- [x] No day-one direct GPU / training / serving expertise requirement — ✅ none asked
- [ ] Has AI workload exposure AND architectural scope — ⚠️ **half**: architectural scope is strong (own
      design/build/operate of clusters, a **major Helm chart rework**, the on-premises appliance, incident
      management and post-incident reviews, capacity planning). AI exposure is agentic-workflow and
      guardrail engineering, not ML-platform work

**Verdict: admissible France-lane primary application; one soft filter short (years) and one unverified
(compensation).** Not a long-shot: the craft match is the closest of any French-lane role logged so far.

## Craft read — the closest match to the actual evidence base

| JD requirement | Candidate evidence |
|---|---|
| 5+ yrs platform/SRE/DevOps | ⚠️ ~4 years continuous; every other line on this table is a direct match |
| **Hands-on running Kubernetes in production — operating and troubleshooting clusters, not just deploying** | ✅ **the core claim** — multi-environment/multi-zone production K8s at Kiln; bare-metal tooling (MetalLB, Cilium, HAProxy) at Docaposte |
| **Bare-metal or on-prem infrastructure, networking/storage/cluster lifecycle** (nice-to-have) | ✅ **exactly the Docaposte work** — MetalLB bare-metal load balancing, Cilium networking/network policy. Also hybrid-cloud at Kiln |
| **Ansible + Helm charts** | ✅ **Terraform/Ansible IaC** evidenced; **Helm usage confirmed** (`docs/resume-edits.md`) |
| CI/CD (GitHub Actions or similar) | ✅ **GitHub Actions**, Drone CI, GitOps via Flux and Argo CD |
| Observability (Prometheus, Grafana) | ✅ **named-match stack** — Prometheus, Grafana, Loki, OpenTelemetry, ELK; MTTR reduction evidence |
| Security mindset — secrets, access, network exposure, blast radius | ✅ **strong** — Vault, SOPS, External Secrets, Teleport, Kyverno, Cilium, cert-manager |
| Harden for **regulated environments (FedRAMP, SecNumCloud)** nice-to-have | ✅ **ISO 27001 implementation led at Cometh**; regulated healthcare (HDS-certified, Docaposte). ⚠️ FedRAMP/SecNumCloud specifically: not evidenced |
| Elasticsearch / RabbitMQ / Redis / S3-compatible storage (nice-to-have) | ✅ per `docs/tooling-inventory.md` (employer attribution partly pending) |
| Terraform (nice-to-have) | ✅ multi-environment Terraform |
| Willingness to code — *"read and write scripts and tooling (mostly Python)"* | ✅ **defensible as written**: operational scripting, not production Python authorship (the CV states this boundary) |
| Full professional proficiency in English; **fluent French** (nice-to-have) | ✅ **French native, English professional** — a real advantage in a French remote-first company |
| Public-cloud provider comfortable or willing | ✅ GCP-first, multi-cloud |
| AI-oriented mindset — uses AI tools/agents, reviews output critically | ✅ independent 2026 AI assistance/orchestration proofs of concept (application layer, per the evidence boundary) |

Direct-miss list: **no MLOps/ML-lifecycle surface**, and Python stays at scripting level. Neither is asked.

## Risks, stated plainly

1. **Years.** 5+ asked, ~4 evidenced. This is the filter most likely to screen it out before a human reads
   the CV — the same barrier as the staff-level roles, one notch softer.
2. **No published band.** Filigran is a fast-growing, venture-backed company with a global hiring footprint
   and equity in the package; that usually clears €80k for this scope, but it is `[INFERENCE]`, not a fact.
   Asking early is cheap and this is the binding filter.
3. **On-call load is explicit and heavier than most:** ~one day shift and one night shift every two weeks,
   **plus a weekend every ~6 weeks** — compensated, but it is a real constraint to accept knowingly.
4. **`track:ai` is a judgement call** (above). If it is really a bridge row, the ML-platform conversion
   cohort is being flattered.
5. **Competition shape.** Remote-first French company with a public brand and a fresh posting → high volume.
   Timing was optimal (applied day 1); differentiation has to come from the *specificity* of the match
   (bare-metal + Helm + ISO 27001 + French), which is unusually good here.

## The one non-obvious lever

Filigran is **open source**: OpenCTI and OpenBAS are public repositories the platform team works around, and a
stated responsibility is literally *"make our repositories, documentation and guardrails agent-friendly."*
A small, real contribution — documentation, a Helm/Ansible improvement, an agent guardrail — is visible to
the exact team that would read the application, and it is the kind of evidence this candidate can produce
without new domain expertise. Flagged as an option, not a plan; it costs evidence-lane hours, not application
hours.

## Recruiter-screen questions (ask before any screen)

1. Total compensation range for this level (the §2 France-compatible floor is €80k) — base and equity split?
2. Is the 5+ years requirement hard, or is depth of production Kubernetes ownership the actual bar?
3. On-call: how is the shared rotation staffed across the ~15-person team, and how is night/weekend work
   compensated in practice?
4. Does the role sit on the SaaS platform, the on-premises appliance, or across both?
5. What does "agent-friendly repositories and guardrails" mean in practice today — is there existing tooling
   to extend, or is it greenfield?

## Timeline

- Contacted / applied: **2026-10-07** (Ashby)
- Follow-up 1 due (5–7 business days): **2026-10-14 → 2026-10-16**
- Follow-up 2 due (10–14 business days): **2026-10-21 → 2026-10-27** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** compensation is unpublished and binding — ask it in the first exchange.

## Funnel delta

Applications sent +1 (2026-10-07, FR lane). **Second-strongest craft match in the whole pipeline** on the
evidence base as written (behind only the closed Workist #11), and the first French-lane role since Lity (#8)
with no relocation question at all.
