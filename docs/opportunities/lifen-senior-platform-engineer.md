# Lifen — Senior Platform Engineer (France, full remote)

**Posting:** https://jobs.ashbyhq.com/lifen/559eedd0-bffe-475a-8b21-5b3540709e4a (Ashby board `lifen`)
· JD written **in French**
**Org:** **Lifen** — French health-data company, founded **2015**. Products are **AI-based** solutions for
sharing medical information between health professionals and accelerating clinical research. **150+ people**,
**800 hospitals** and **150,000 health professionals** connected, *"impact sur des millions de patients en
France chaque jour"*, now preparing to expand across Europe. Team: **Cloud Services** (infrastructure),
described as senior and growing, working on the platform that lets development teams host, deploy and operate
their applications securely and autonomously, in a **multi-cloud environment with a progressive migration from
AWS to GCP**.
**Market:** **fr-bridge** (French employer, **entire team works remotely from France** — *"L'équipe travaille
entièrement à distance depuis la France"*) · **Tier:** **B** · **Channel:** ATS (Ashby) · **Track:** `ai`
**Applied:** ✅ **2026-10-09** · **Stage:** Contacted · **Issue:** #35
**Compensation:** **not published.** France-compatible floor **€80,000** (§2). ⚠️ `CONTEXT.md` flags
**French bands as `[INFERENCE]` estimates** — no primary-source benchmarking was done. **This is the binding
unknown.**
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**
**jobradar:** board **added 2026-10-09** (`ashby:lifen`, `market: fr`) — Lifen was untracked. Scan verified row
`a34389004106ac08`: `Senior Platform Engineer`, `location: France`, `country: fr`, `mode: remote`,
`decision: review`, score 4, `lane: fr`.

## Tier note

**Tier B, `track:ai`** on the same basis as #31 (Annapurna): the **employer's product is AI** (medical-data AI
at national scale, with named interfaces to Data, IA and Security/Compliance teams), while **the role itself
owns no ML platform** — it is internal-developer-platform and cloud-services engineering. Recorded explicitly
so the label is auditable rather than automatic.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — *"expérience confirmée"* in infrastructure/SRE/platform; senior IC, no staff scope
- [ ] Compensation ≥ €80k (France-compatible) — ⚠️ **unverified and the likely eliminator.** A 150-person French
      health-tech scale-up is precisely the shape that prices a senior platform engineer **below €80k**. No band
      published; French bands are `[INFERENCE]` in this repo. **Ask in the prequalification call with Laura**
- [x] Geography — ✅✅ **the cleanest pass yet**: French employer, **fully remote from France**, no relocation,
      no entity question, and no 8–12 week remote-start negotiation. The fastest lane in the plan
- [x] No day-one GPU / training / serving requirement — ✅ no ML-infrastructure ownership in the JD
- [x] Architectural scope — ✅ evolves an **Internal Developer Platform** serving **50+ internal clients**,
      owns platform architecture in multi-cloud, and is measured on **adoption** rather than tickets

**Verdict: admissible and among the strongest fits in the pipeline — for the first time the stack, the domain
and the geography all line up at once. One unknown, and it is compensation.**

## Craft read — the JD names nearly every tool in the inventory

| JD requirement | Candidate evidence |
|---|---|
| **Terraform / Terragrunt** (must-have, named) | ✅✅ **both named tools are in `docs/tooling-inventory.md`** — Terraform multi-environment IaC (deployed) and Terragrunt (used) |
| **FluxCD** (must-have, named) | ✅✅ **Flux `deployed` at Kiln** — the second JD this week naming Flux exactly (with Annapurna #31). Argo CD also `used` |
| **Deep expertise in one CSP**, managed services: Kubernetes, Object Storage, Database, Message Bus, KMS | ✅✅ **GCP** — multi-zone Kubernetes on GCP (Cometh), BigQuery, Pub/Sub. Object storage: **Ceph** (`used`). Database: PostgreSQL, MongoDB, Redis (`deployed`). Message bus: **GCP Pub/Sub** (`deployed`) — Kafka was never used, do not claim it. KMS: SOPS (`deployed`), Vault, External Secrets |
| **Monitoring/metrics: Victoria Metrics, Grafana, EFK** | ✅ Prometheus/Thanos/Alertmanager (Victoria Metrics is a Prometheus-compatible TSDB — the transfer is direct), **Grafana**, **EFK** via ELK and Loki, Jaeger tracing |
| Container orchestration and a resilient automated deployment pipeline | ✅✅ GitOps (Flux/Argo CD), Helm, Drone CI `deployed`, GitHub Actions, Docker |
| **Regulated environment** (nice-to-have) | ✅✅ **the strongest domain match in the pipeline**: Docaposte was **HDS-certified health-data infrastructure** and the CV says *"recovered and stabilized critical Kubernetes clusters in a regulated healthcare environment"*; also led **ISO 27001** implementation. Lifen is *health data*: the same regulatory world |
| Scale-up / infrastructure supporting **multiple SaaS products** | ✅ Kiln (40+ networks, 10+ protocols, $8B+), Cometh (multi-zone delivery platform) |
| **Concrete use of AI tools at work, with attention to results** (nice-to-have) | ✅✅ the 2026 AI-assist/orchestration work — and the JD asks for *outcomes*, which is exactly how it is framed in the evidence base |
| Distributed team, written communication, autonomy but not alone | ✅ strong written-communication instinct (the outreach drafts, documentation habits) — ⚠️ verify the counter-evidence: name one concrete remote/distributed team you worked in |
| Cross-team collaboration, explaining complex concepts to non-technical stakeholders | ✅ architecture-translation bullet; cross-team risk mitigation; driving adoption is the same skill |
| **Internal Developer Platform** for 50+ internal clients, self-service, adoption-driven | ⚠️ **partial and must be framed honestly**: platform tooling, GitOps self-service patterns and cross-team platform work — but **not an owned IDP product**. The JD's own framing (*"une plateforme n'a de valeur que si elle est utilisée"*) is the strength: adoption-and-autonomy is how the current work is already measured |
| French-language working environment | ✅ French speaker — the JD and the team language are French |

## Risks, stated plainly

1. **Compensation is unpublished and the floor is real.** A 150-person French scale-up in health data is the
   profile most likely to sit under €80k for a senior platform engineer, and this repo has no primary-source
   French band data. **Ask in the prequalification call, not later** — it is one question and it decides
   whether the rest of the process is worth three more interviews.
2. **Four-step process with an unusual middle step:** a **1h30 live incident simulation** — clone a repository,
   run an application locally, share the screen, explain the diagnostic approach, with a GitHub account and
   technical prerequisites required beforehand. This is where preparation pays: see
   `docs/interview-incident-stories.md` and be ready to narrate the Docaposte cluster recovery out loud while
   debugging. **72h feedback between steps**, and a **reference check at the end** — references must be
   prepared before the final stage, not after it.
3. **IDP ownership is not directly evidenced.** Expect the question "what have you built for other engineers,
   and how did you know it was adopted?" Answer from the GitOps/self-service and cross-team work, and be
   explicit about the boundary.
4. **Run rotations are described as potentially demanding** (*"peuvent être prenantes"*) — they are honest
   about it, and it is a two-week build/run cycle.
5. **Multi-cloud migration in progress** — AWS→GCP means legacy AWS surfaces will be touched. His AWS gap
   (three JDs today required it) is *reduced* here because GCP is the destination and the named focus, but it
   is not zero.

## What is genuinely attractive

- **The cleanest geographic pass in the pipeline**: French employer, **fully remote from France**, fastest lane,
  no relocation, no entity question — unlike every other application logged today.
- **The stack overlap is near-exact and on the *target* platform**: Terraform **and** Terragrunt, **FluxCD**,
  GCP, Grafana, ELK/EFK, Kubernetes — and the AWS→GCP direction means the current GCP depth is the destination
  rather than the compromise.
- **HDS/health-data experience in a health-data company** is the single most transferable credential in the
  whole search, and it is real production experience rather than adjacency.
- **AI-tool usage with attention to results** is listed as a nice-to-have — the rare JD where 2026 work is
  directly on the list.
- **Adoption-driven platform work** ("help the teams solve it themselves, not instead of them") matches the
  architecture-translation differentiator better than any other JD reviewed.
- **Named process, named contact (Laura, TA), 72h SLAs** — a professional pipeline, and the incident case suits
  an SRE's actual strengths.

## Questions to put in writing (first follow-up / prequalification)

1. **Salary band** for the role? (The €80k floor is the gate; French bands are unbenchmarked in this search.)
2. How far along is the AWS→GCP migration, and what is still AWS-only?
3. What does the run rotation look like in practice — hours, escalation, and who carries it?
4. What has already been built on the IDP, and what does "adoption" mean in their metrics?
5. Is the contract French (Lifen entity), and is there any on-site expectation in Paris?
6. Which managed services are the KMS and message-bus choices today?

## Timeline

- Contacted / applied: **2026-10-09** (Ashby)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Prequalification (Laura, TA): —
- Hiring manager: — · Technical case: — · Cultural alignment: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Salary: not stated in the application
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** geography is settled in the right direction, so a rejection would be **compensation** or
  **relevance** (IDP ownership, AWS legacy) — the elimination set is small and interpretable, like #32 Runware.
- What would have changed the outcome: —

## Funnel delta

Applications sent +1 (2026-10-09) · **FR-bridge lane (the 50% lane, and the one with the fewest live rows)** ·
`tier:b` · `track:ai` · board gap closed (Lifen was untracked). Fourth application today; the first that is
French-employer and fully remote from France.
