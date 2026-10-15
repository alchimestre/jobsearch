# Sinch — Site Reliability Engineer (SRE)

**Posting:** https://www.linkedin.com/jobs/view/4472071666/ · France — **fully remote, based in France**
**Org:** Sinch / **Mailjet** infrastructure (email delivery at scale)
**Market:** FR-bridge (France-remote / EU-remote compatible) · **Tier:** C (strong non-AI SRE bridge) · **Channel:** ATS
**Applied:** ✅ 2026-09-26 (LinkedIn) · **Stage:** **Screening** — ACK received 2026-10-15, application under
review · **Follow-up:** none owed while under review; one line if silent past 2026-10-29

## Why this is the strongest bridge candidate in the pipeline

Three things separate it from vivenu (#3, closed) and ablefy (#4):

1. **Residency is already satisfied.** The JD requires residence in and eligibility to work in France, and
   states plainly that relocation and visa sponsorship are unavailable. Normally a rejection trigger — here
   the candidate is inside the eligible population by default. **First ATS application in the pipeline whose
   location gate costs nothing to clear.**
2. **Fully remote.** No relocation, no remote-start negotiation, no permit lead time. This is the
   EU-remote/France-compatible lane's ideal shape.
3. **Craft match is direct.** The team builds and operates infrastructure at the heart of every Sinch Mailjet
   service: transactional email at scale. Sustained throughput, backpressure, replication lag, degraded
   dependencies, incident response under load — the exact constraints named in the Kiln and Cometh evidence.
   The stack (GCP, Terraform, Ansible, Prometheus, Grafana, PostgreSQL/Cassandra/Elasticsearch, Kafka,
   Python/Bash scripting) overlaps almost entirely with the tooling inventory. SLO definition and tracking is
   a stated responsibility, which is the evidence gap being closed by `ml-platform-on-k8s`.

## Why it is still Tier C

The ML requirement is **not** met. Sinch is a large communications platform; its "AI-infused Super Network"
is a product-layer marketing claim, not an ML platform the SRE team owns. Nothing in the JD describes ML
pipelines, a model registry, serving/inference, training infrastructure, or ML observability. Under §2 this
is a non-AI SRE bridge role → **Tier C**, admissible only from the last-resort window (~Apr 2027).

`[INFERENCE]` on any AI-exposure claim until a screen confirms what the team actually runs.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — ✅ LinkedIn band **Mid-Senior level**; no years figure stated. Closest match yet to the 3–6 year window
- [ ] Compensation ≥ €80k (EU-remote / France-compatible) — **unverified**, not disclosed `[INFERENCE]` a Sinch France SRE clears €80k
- [x] On-site allows 8–12 week remote start / relocation assistance — ✅ **fully remote in France**; better than the filter requires
- [x] No day-one direct GPU / training / serving requirement — ✅ none in scope
- [ ] AI workload exposure AND architectural scope — ⚠️ **partial**: architectural scope ✅ (SLOs, datastore/platform ownership, scaling), AI exposure ❌

## Recruiter-screen answers (ask before any screen)

1. Does the team own any ML/AI serving or training workload, or is the platform purely product infrastructure?
2. Seniority band and expected experience?
3. Total compensation range for the role?
4. Confirm the remote arrangement — fully remote within France, any office expectation?
5. Current stack and reliability maturity: GCP topology, Kafka/Cassandra scale, on-call model, SLO coverage?

## Outcome record

- Stage reached: **Screening** — ACK 2026-10-15: Sinch replied that the application is under review. No
  reason, no next-step date, no screen scheduled. Board Stage set 2026-10-15 (was Contacted)
- Rejection reason: pending. If refusal with no reason → `unknown`
- Follow-ups: **1st was due 2026-10-05, 2nd (final) 2026-10-14 — both now moot.** The ACK answers the only
  question they carried. One line goes out if the review is still silent on **2026-10-29** (10 business
  days from the ACK); no chaser after that
- Still unverified: compensation (no band published), seniority band, whether the team owns any ML/AI workload
- What would have changed the outcome: nothing on the candidate side yet known — the review is live

## Funnel delta

Applications sent +1 (2026-09-26, FR-bridge lane). This is a bridge-lane application, so it counts toward
§6's channel/tier conversion but should **not** be pooled into primary-lane (ML-platform) conversion rates.
