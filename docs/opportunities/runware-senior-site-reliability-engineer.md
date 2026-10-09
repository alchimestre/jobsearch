# Runware — Senior Site Reliability Engineer

**Posting:** applied via https://www.linkedin.com/jobs/view/4442595168/ · **canonical ATS req:**
https://apply.workable.com/j/7869EFBE16 (Workable shortcode `7869EFBE16`, published **2026-07-20**, still
live on the board at time of writing)
**Org:** **Runware** — GPU inference infrastructure vendor. Founded 2023, platform launched Oct 2024. One API
for 400K+ models, serverless GPUs, and reserved/bare-metal GPU capacity on **hardware they design, build and
run** (Sonic Pods: 1MW in a 20-foot container, sited at renewable power). **$66M raised**, including a **$50M
Series A in Dec 2025 led by Dawn Capital**, with Comcast Ventures, Speedinvest, Insight Partners, a16z
Speedrun, DST Global, Begin Capital and Zero Prime. Customers named publicly: **Wix, Higgsfield, NightCafe**.
SOC 2 and ISO 27001 certified, GDPR compliant. Team across **10 countries, 6 time zones**. Founders: Flaviu
Rădulescu (CEO, previously a bare-metal cloud co-founder and R&D head at a company running hundreds of
thousands of servers) and Ioana Hreninciuc (unit economics: margin per user and per session).
**Scale claim:** 1M+ developers; requests served **10B+ (home page) / 20B+ (about page)** — the two pages
disagree; **99.99% uptime over the last 90 days** claimed. Treat both as vendor claims, unverified.
**Market:** **EU-remote** · **Tier:** **A** · **Channel:** ATS (Workable, applied via LinkedIn) · **Track:** `ai`
**Location:** **remote-first**, "*work from home anywhere we can employ you*", twice-yearly company retreats.
**The req lists six countries: United Kingdom, France, Germany, Spain, Italy, Sweden — France is explicitly
in scope.** No relocation required.
**Applied:** ✅ **2026-10-09** (LinkedIn) · **Stage:** Contacted · **Issue:** #32
**Compensation:** **not published.** Berlin/EU-remote floor **€80,000** (§2); benefits list "meaningful stock
options". A Series A at this funding level should clear the floor — **unverified, ask**.
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**
**jobradar:** **board added 2026-10-09** (`workable:runware` in `companies.yaml`, `market: eu-remote`) after
this application exposed the gap. Scan verified: row `0bf2e7aac892449a`, `decision: review`, `mode: remote`.
See "Tooling note" below for the adapter defect found and fixed in the process.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — "Senior Site Reliability Engineer", Workable metadata says **Mid-Senior level**.
      (The board also carries a separate `Staff Software Engineer - Serverless` req — different role.)
- [ ] Compensation ≥ €80k — ⚠️ **unverified**, not published; equity-heavy framing
- [x] **Geography: passes outright, for the first time in the pipeline.** Remote-first, **France explicitly
      listed** among the employable countries. No relocation, no 8–12 week remote-start question, no
      contract-entity risk of the kind that killed Otera (#10) and idnow (#29)
- [x] No day-one GPU / training / serving requirement — ✅ **GPU, CUDA/NVIDIA drivers, vLLM/TensorRT/Triton
      are all under "Bonus"**, not requirements. The hardware depth that makes the vendor tier hard to enter
      (`CONTEXT.md`) is not demanded by this JD
- [x] AI workload exposure AND architectural scope — ✅ the platform *is* the AI infrastructure: *"reliability,
      availability and performance of critical production services"*, SLIs/SLOs, production-readiness
      standards, capacity planning, automated remediation

**Verdict: admissible, and the strongest *strategic* fit in the pipeline.** Geography is settled in the right
direction, the AI surface is the job itself, and the vendor-tier objection does not apply to this particular
JD. The binding unknowns reduce to **compensation** and the two evidence gaps below.

## Tier note — Tier A, vendor tier, and why the usual objection does not bite

`tier:a` = owns the platform the AI workloads run on. Runware is the textbook case: inference serving across
GPU fleets, routing layer, queues, multi-tenant isolation, per-second metering — the reliability role owns the
production behaviour of all of it.

`CONTEXT.md` puts the **GPU/vendor tier in the secondary lane** because it "demands hardware depth
(CUDA/NCCL/RDMA/HPC) with no candidate evidence, at staff/senior bars". **This JD inverts that**: every
hardware item — NVIDIA drivers, CUDA, GPU monitoring, vLLM/TensorRT/Triton — sits in **Bonus**. The
requirements are SRE fundamentals: distributed-systems debugging, observability, Kubernetes/IaC, incident
management, on-call. Recorded here explicitly so the tier assignment is auditable rather than automatic.

## Craft read

| JD requirement | Candidate evidence |
|---|---|
| Strong experience operating and troubleshooting production systems at scale (SRE / Prod Eng / Platform) | ✅ ~4 years; multi-zone, 40+ networks, $8B+ secured |
| **Debugging across applications, databases, queues, containers, networking and infrastructure** | ✅✅ **this is the CV**: Postgres, Redis, Elasticsearch, MongoDB, etcd, Pub/Sub; Traefik, Kong, HAProxy, MetalLB, Cilium, nginx; Kubernetes multi-zone and bare-metal |
| **Observability: metrics, logs and distributed tracing** | ✅✅ Prometheus + Thanos, Grafana, Loki, ELK, **Jaeger tracing**, Datadog, Alertmanager, OpenTelemetry |
| **"Understand SRE principles including SLIs, SLOs, error budgets, capacity planning, incident management and reducing operational toil"** | ⚠️ **split claim.** Incident response/management, capacity planning and toil reduction are defensible today. **An owned SLI/SLO/error-budget programme is an excluded claim** — targeted by `ml-platform-on-k8s` at week 6. Say "understand, not yet owned" and offer the in-progress work |
| Kubernetes, containers, IaC, automated deployment | ✅✅ Terraform/Terragrunt multi-environment, Ansible, Flux and Argo CD GitOps, Helm, Drone/GitHub Actions |
| **"Write software and automation using languages such as Python, Go or PHP"** | ⚠️ **the gate.** Automation and scripting: yes. **Production Python/Go authorship: excluded claim.** At a company whose platform is software, this is the requirement most likely to decide the outcome |
| Ownership, on-call, initial investigation through long-term remediation | ✅✅ production SRE, incident response, RCAs |
| Bonus: high-throughput / low-latency APIs | ⚠️ partial — node/RPC and distributed network ops, not a customer-facing API product |
| Bonus: **bare-metal infrastructure** | ✅ **Docaposte**: MetalLB, HAProxy, Cilium on bare metal; plus Kiln's distributed node fleets. **Genuinely rare in this market and directly relevant to Sonic Pods** |
| Bonus: GPU environments / AI-ML workloads | ⚠️ **GPU-adjacent, not ownership.** The GPU-fleet claim stays off the CV |
| Bonus: RabbitMQ / queues | ⚠️ Pub/Sub and internal queues yes; **RabbitMQ no; Kafka never used** (removed from the inventory) — do not claim either |
| Bonus: MySQL, Redis, ClickHouse | ⚠️ **Redis deployed** ✅; MySQL never used; ClickHouse not used (note: #17 is an *application to* ClickHouse, not experience with it) |
| Bonus: global traffic management, load balancing, CDN, hybrid infra | ⚠️ partial — HAProxy/MetalLB/Traefik/Kong/nginx ingress and hybrid-cloud operations ✅; CDN and global traffic management not evidenced |
| Bonus: automated scaling, capacity management, self-healing | ⚠️ partial — capacity planning yes; self-healing automation not evidenced |

## Risks, stated plainly

1. **The Python/Go requirement** is a must-have, and it is the exclusion in the evidence boundaries. Expect a
   screen or a code exercise around it.
2. **SLO/error-budget language in the JD** versus the excluded claim — handle honestly, do not stretch.
3. **Req age:** published 2026-07-20 and still open ~2.5 months later, with LinkedIn offering "be among the
   first 25 applicants". A long-open senior req can be pipeline-building — or genuinely hard to fill, which
   for this stack is plausible and favours the candidate. Treat silence as normal, not as a signal.
4. **Compensation unpublished** on an equity-weighted package.
5. **On-call**: the JD names an engineering on-call rotation, and the company is small (10 countries) with a
   24/7 platform claim. Ask how often, and how the pager is shared.
6. **Vendor claims** (uptime, request volume, cost-per-generation) are their own marketing; the about page and
   home page disagree on request volume. Do not repeat their numbers back as facts in an interview.
7. **Own-hardware culture**: Sonic Pods means BIOS/kernel-level tuning and physical constraints. This is not a
   cloud-platform role and the hardware side is where the candidate has the least depth — though bare-metal
   Kubernetes is real evidence and unusual.

## What is genuinely attractive

- **The company's entire thesis is the candidate's strongest verified number.** Runware exists to make
  inference *"cost as close to the price of electricity as physically possible"*, "*half the cost of a
  neocloud*", with the co-founder's framing being *"unit economics: margin per user and per session"*.
  Vincent's **cloud spend −25%** and cost-aware platform work land directly on the product's core problem.
- **First application in the pipeline where geography is settled in the right direction** — remote-first with
  France listed, verified on the employer's own ATS rather than inferred from a LinkedIn string.
- **Tier A with the vendor-tier objection genuinely absent** from the requirements.
- **Bare-metal Kubernetes** is real evidence, rare, and directly relevant to hardware they run themselves.
- **ISO 27001 / SOC 2 / GDPR** posture matches the compliance work already on the CV.
- A **funded** Series A ($50M, Dec 2025) rather than a pre-seed, which matters for the €80k floor.

## Questions to put in writing (first follow-up)

1. Base salary band for this role, and the equity share? (§2 floor €80k; no band published.)
2. Which **employment entity** would the contract use — France, or another of the six listed countries?
3. On-call rotation: frequency, escalation, and how it is shared across time zones.
4. What does *"write software and automation"* mean in daily practice — SRE-with-code, or backend
   engineering with an on-call hat?
5. **Is there an SLO/error-budget programme today, or would this role establish it?** (Direct route into the
   one gap that is actively being closed at week 6.)
6. Which parts of the stack are on Sonic Pods (own hardware) versus hyperscaler regions, and does this role
   touch the hardware layer?
7. Why is the req open since July — scope change, or a hard search?

## Timeline

- Contacted / applied: **2026-10-09** (LinkedIn; canonical req published 2026-07-20)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Salary: not stated in the application
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** the geography answer is already known and favourable, so a rejection here cannot be a location
  mismatch — it will be **relevance** (Python/Go software authorship, GPU-adjacent depth) or **compensation**.
  That makes it a much more informative row than the eleven `unknown` closures: for the first time the
  elimination set is small enough to interpret.
- What would have changed the outcome: —

## Tooling note — the board gap this application exposed, and a defect found while fixing it

**Gap:** Runware's board was not polled, so a July posting for the pipeline's best-fit role was invisible to
the tool until it surfaced on LinkedIn. Fixed: `jobradar discover 'https://apply.workable.com/runware/'
--write` added `workable:runware` (`market: eu-remote`) to `companies.yaml`; a scan verified the row landed.
**This was the first Workable board in the watchlist** — 159 boards were tracked, none via Workable.

**Defect found and fixed the same session:** `fetch_workable` in
`tools/jobradar/src/jobradar/sources/ats.py` read `item.get("location")`, but the Workable widget payload
carries **no `location` key** — the countries live in `locations[]` (`country`, `countryCode`) plus top-level
`country`/`city`. Every Workable posting therefore stored `location: ""` and `country: unknown`, was tagged
**`-geo-unverified`** and was mis-scored, despite the payload stating the country. Confirmed on the Runware row
before the fix (`location =`, `country = unknown`, `reasons = +sre,+reliability,-geo-unverified`, while the API
returns six countries for that req). Multi-country reqs also arrive as either one entry with several
`locations[]` or several single-country entries.

Fixed in a new `_workable_location()` helper: countries from `locations[]`, joined with `; `, falling back to
the flat `city`/`country`/`state` pair; `remote` still comes from `telecommuting`. A test
(`test_workable_joins_countries_from_locations`) covers both payload shapes; the suite is **173 passed**.
Verified against the live board after a rescan: the row now reads
`location: United Kingdom; France; Germany; Spain; Italy; Sweden`, `country: fr`, `mode: remote`,
`reasons: +sre,+reliability` — `-geo-unverified` gone. Joining the list is safe for the gate: `country()`
matches target countries before the non-target list, and `SCOPE_BLOCKED` does not include UK/ES/IT, so the
extra countries cannot flip the row to `restricted`.
