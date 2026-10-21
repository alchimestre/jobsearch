# Bubblemaps — SRE / Data Engineer (via Yofy recruiter)

**Company:** Bubblemaps (bubblemaps.io) — "The Onchain Intelligence Layer". Blockchain forensics and onchain
analytics: wallet clustering, token distribution tracking, fund tracing across 15+ chains (Ethereum, Solana,
BNB, Avalanche, Polygon, Base, Arbitrum, HyperEVM, TON, Tron, Monad, Aptos…). Products: Bubblemaps V2,
Intel Desk (community investigations / "InfoFi"), iframe widget, API.
**Backers:** Consensys, Polygon, Avalanche, Aptos, Ledger, The Sandbox, Linea, Fuel, Ince, Momentum6, V3ntures
**Recruiter:** Yofy (agency/external recruiter) — name incomplete, needs capture on next contact
**Role:** SRE / Data Engineer · **Market:** FR (French company, Web3 — confirmed by Vincent 2026-09-29) · **Tier:** C (no ML-platform surface) · **Channel:** recruiter
**Stage:** **Interview** — technical round **passed** (reported 2026-10-18); **final round with the CTO on 2026-10-20** · **Comp quoted by recruiter: €60,000–80,000** · **Candidate asked: €70,000 minimum — still unconfirmed** · **Paying entity and remote policy still unknown**

## Market note — FR-bridge, and that strengthens the case for holding it

Confirmed 2026-09-29: Bubblemaps is a **French** company (Web3). This matters more than it looks:

- It lands squarely in the **FR-bridge lane** (50% allocation, the largest lane) rather than EU-remote.
- A **French entity means French employment terms** — CDI, French payroll, no EOR or cross-border wrapper.
  That removes the contracting-entity risk that shadowed Otera (#10).
- **No relocation or permit friction**, consistent with the destination hierarchy's first tier.
- The recruiter is French and the role is FR-based, so the €70k ask reads as a normal French platform
  salary rather than an outlier. `[INFERENCE]` the band was quoted in French market terms.

**But it does not change Tier C.** France-remote, French-payroll, and no-ML-platform are independent
properties. Geographic fit is good; strategic fit is still the weakest logged.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — ✅ no indication
- [ ] Compensation ≥ €80k (FR-bridge) — ⚠️ quoted band tops out exactly at the floor. Asked €70,000 minimum, which is **below** the floor but consistent with the late-cliff/last-resort flex (€70k) — this is a **floor exception**, deliberate, and must be recorded as such
- [ ] On-site / remote — **location still unconfirmed on the call**, but confirmed French company. French employment terms expected (CDI, French payroll); **remote policy not yet established**
- [x] No day-one direct GPU / training / serving expertise — ✅ none implied
- [ ] ML/AI surface AND architectural scope — ❌ **no AI/ML surface.** Blockchain forensics and onchain analytics. Data engineering here means chain indexing/ingestion pipelines, not ML lifecycle. Preferred, not required (§2, amended 2026-09-29), so this is a Tier C note rather than a rejection.

**Tier C — and arguably the weakest strategic fit logged to date.** Two independent problems: the floor is
breached, and the domain is a lateral move back into crypto rather than toward ML platform.

## The €70,000 decision — this needs scrutiny

The €80,000 floor is a **hard constraint** under §2, and §8 states plainly: *"Compensation and relocation
filters are hard constraints. Funnel pressure does not override them."* €70,000 is admissible **only** in
late-cliff mode (~Feb 2027) or the last-resort window (~Apr 2027). Neither is active — today is 2026-09-29
and the mode timeline is cliff-anchored, not week-anchored.

So this application is running **outside the plan** on compensation. That may still be the right call, but it
should be a **conscious labelled exception**, not a quiet drift:

- It does not count toward the primary lane and must not be pooled with it.
- If it progresses, record it as a **deliberate floor exception** so the funnel stays interpretable and the
  floor does not appear to have moved.
- The recruiter quoted €60–80k and the ask was €70k — landing mid-band. [INFERENCE] the CTO conversation is
  the real gate; comp may not be the binding constraint.

## If the CTO is open to freelancing — TJM (added 2026-09-29)

Reference: full-time engagement, 200 billable days/year (4–5 weeks unpaid leave + sick/bench).
Employer cost multiplier 1.42 [INFERENCE — standard cadre range 1.40–1.45; no reduction générale at 70k].

| | €60k | €70k | €80k |
|---|---|---|---|
| Client all-in cost | ~€85k | **~€100k** | ~€114k |
| Cost-parity TJM @200 d | €426 | **€500** | €568 |
| @210 d | €405 | €476 | €541 |
| @218 d | €390 | €459 | €521 |

- **€500/day = the €70k ask expressed as client cost** — the defensible floor.
- **€550/day = ~€77k CDI-equivalent**, i.e. the top of their own band. **This is the opening ask.**
- **€600/day (~€84k-equivalent)** only if part-time, or if the CDI would have carried tokens/equity.
- Never let the client convert TJM = gross ÷ 218 (would give €321). Anchor on *cost*: 70k gross costs
  them ~€100k all-in.

Pitch: *"A CDI at 70k costs you about €100k all-in. At 200 billed days that's €500/day cost-neutral; I'm
asking €550 because I'm funding my own leave, sick cover and unemployment insurance."*

Caveats to resolve on the CTO call: days/month and duration; whether Bubblemaps contracts directly or via
Yofy (agency margin compresses the rate); and that invoicing >9 days/month zeroes ARE, so part-time only
makes sense at €550+.

## Why it may still be worth pursuing

1. **Income continuity outranks everything at the cliff**, and a live recruiter conversation at €70k is a real
   option to hold — not a role to invest heavily in.
2. **Data engineering exposure** is genuinely adjacent to the gap list. Chain indexing and large-scale
   ingestion is closer to pipeline work than anything in the current evidence.
3. **Kiln evidence transfers directly**: 40+ protocol networks, multi-protocol integration in hybrid cloud,
   sustained protocol-level traffic. This is the strongest domain overlap of any role logged, because it is
   the *same domain*.
4. Crypto-native companies are usually remote-first, which suits the EU-remote/France-compatible lane.

## Why it does not advance the thesis

- No ML/AI platform surface anywhere in the company description. "Data" here is onchain analytics, not model
  lifecycle.
- The CV already has Kiln, and a second crypto role deepens the existing specialisation instead of building the ML-platform evidence.
- The `ml-platform-on-k8s` artifact remains the thing that closes the real gaps; this role competes for the
  same hours without contributing evidence to it.

## CTO call — 2026-09-30 → technical interview (Stage → Interview)

The CTO gate opened: **advanced to a technical interview** (reported by Vincent 2026-09-30).

**Captured from the CTO call (2026-09-30):**

- **The role is genuinely SRE + Data**, not a choice between two postings — Vincent's read of the call.
- **The technical round is with a data engineer.** The interviewer owns the data half, so the round will
  weight ingestion/indexing and data-platform depth, with SRE answers as the reliability frame around it.
- **No salary discussed.** The €70,000 ask is still neither accepted nor refused; the recruiter's €60–80k
  quote remains the only number on the table.
- **Still unknown:** remote/hybrid policy, which entity pays (direct French CDI vs Yofy EOR/contractor), and
  the round's format and duration.

**What changed, and what did not**

- **Changed:** the role is real. A CTO conversation that advances is the strongest signal any Tier C role has
  produced, and `channel:recruiter` now has an active technical process — the first in the pipeline.
- **Unchanged:** the floor exception. €70k is still below the €80k floor, still admissible only in late-cliff
  (~Feb 2027) or last-resort (~Apr 2027), and **neither is active**. Advancing does not move the floor; the
  exception stays labelled and unpooled with the primary lane.
- **Ranking:** Web3 infrastructure is admitted in every lane and Kiln transfers directly, so there is no
  ML-surface penalty. But this is French, Tier C and €70k — it ranks below #21 MarvelX and the AI lane on
  compensation alone.

## Technical interview — prep

**The interviewer is a data engineer and the role is SRE + Data — prep both halves, data-weighted.** The
format is still unknown; ask in the first two minutes.

### 1. What the interviewer tells you

- **Data depth is the screening axis.** Expect volume, schema, reorgs, duplicates, backfill and
  query-performance questions. SRE is the frame around those answers, not the subject.
- **The wedge is the platform side of that pipeline.** §2's own sub-filter prefers the
  platform/infrastructure side over pipeline authoring, and the same logic holds here: reliability, capacity,
  observability and cost **of** the pipeline are defensible; pipeline authorship is not evidenced anyway.
- **Still worth asking early:** the round's format (live coding vs design vs incident walkthrough), its
  duration, and who else is in the loop.

### 2. Receipts to lead with (no new claims needed)

| Story | Anchor |
|---|---|
| Distributed infrastructure at scale | Kiln: infrastructure securing **$8B+ across 40+ protocol networks**, sustained protocol-level traffic |
| Multi-protocol integration in hybrid cloud | Kiln: **10+ protocols** integrated into hybrid-cloud environments — the nearest thing to chain-indexing work in the CV |
| Multi-zone Kubernetes on GCP | Cometh: standardised observability (Prometheus, Grafana, OpenTelemetry, ELK), **MTTR reduction**, **25% cloud-cost reduction** |
| On-prem bare-metal Kubernetes | Docaposte: MetalLB, Cilium (CNI/network policy), HAProxy, HDS-certified healthcare |
| Platform tooling operated | Velero (backup/restore), Teleport, cert-manager, Flux, nginx |
| Compliance | **Led the ISO 27001 implementation** at Cometh |

**No throughput numbers** — Vincent cannot disclose load figures. Keep scale structural (networks, protocols,
zones, assets secured).

### 3. Gaps that will come up — the honest answers

- **Production Python/Go:** operational scripting only, no production claim (`CONTEXT.md` Evidence
  Boundaries). Answer plainly and pivot to the `ml-platform-on-k8s` artifact, which is Python end-to-end
  (pipeline, serving, drift job, tests). Do not upgrade the claim before the artifact exists.
- **Formal SLO/error-budget methodology:** the artifact is where that becomes evidenced (SLIs, error-budget
  policy, burn-rate alerts, runbook). "Building it now" — not "ran it at scale" (see §7: zero technical
  interviews after six active ATS weeks pauses new ATS applications for a funnel audit, and this interview is where those
  hours go).
- **Chain-indexing / ETL ownership:** not evidenced. Nearest real experience is protocol integration at Kiln,
  not indexer authorship. Say so.
- **Chaos engineering as a named practice:** fault injection is not a listed claim yet; the artifact's failure
  drills are the plan for it.

### 4. What a data engineer will probe — and the answer shape

| Likely question | Where the evidence is | Honest limit |
|---|---|---|
| Ingesting 15+ chains: RPC/WS backlog, rate limits, node failures | Kiln: 40+ protocol networks, **10+ protocols integrated**, sustained protocol-level traffic | Vincent operated that infrastructure; he did **not** author the indexer |
| Reorgs, duplicate and late blocks | no direct evidence | Say so, then reason from idempotency and replay (block height + hash keys, idempotent upserts, deterministic replay). Reasoning is fine; claiming experience is not |
| Backpressure and indexer lag when a chain outpaces the pipeline | production backpressure and incident response at Kiln | Frame as platform reliability: lag SLIs, alerting, queue depth, autoscaling |
| Storage and query at scale (Postgres / ClickHouse / Timescale) | tooling inventory: PostgreSQL, MongoDB, Elasticsearch, Redis (employer attribution pending for part of that list) | Data-store **operations**, not schema or data-model authorship |
| Cost per chain / per TB / per query | Cometh: **25% cloud-cost reduction**; capacity planning at Kiln | The strongest quantitative story available |
| Pipeline reliability: freshness SLOs, error budgets, runbooks | the `ml-platform-on-k8s` artifact (SLIs, burn-rate alerts, runbook) | "Building it now" — not "ran it at scale" |
| Kubernetes for the pipeline (scheduling, nodes, retention, upgrades) | core claim: multi-zone/multi-environment production Kubernetes | Direct |

### 5. Time-box — do not let this crowd out the primary lane

- The split is known, so **deep prep on both halves is warranted** — but **compensation is still undiscussed**
  and the floor exception is unchanged: €70k is below the floor, admissible only in late-cliff (~Feb 2027) or
  last-resort (~Apr 2027), and **neither is active**.
- Ask compensation, remote policy and paying entity **before or at the round**, not after.
- A €70k Tier C role does not outrank the `market:de` / EU-remote AI lane (#9 SAP Fioneer, #11 Workist,
  #12 Langdock) or the artifact hours.
- The artifact does double duty: SLO and failure-drill material rehearsed here is the same material the
  primary lane screens on. If comp stays at €70k, treat the round as **rehearsal plus income insurance**, not a
  lane shift.


## Technical interview — working reference (2026-10-05)

Interview: **2026-10-06 morning, with a data engineer.**
**Status: ✅ took place 2026-10-06. Outcome and interviewer feedback not yet reported** — Vincent will
debrief later. Do not record a result, a stage change, or a follow-up date until that debrief; the next step
(second round, take-home, or silence) is unknown.
Preparation is ongoing, not evidence of production
Kafka/ClickHouse expertise. Vincent identified source-to-storage lag and replay from committed offsets;
reorg recovery and database correctness still need practice.

### Evidence boundary

Bubblemaps' [public map API](https://docs.bubblemaps.io/data/api/tokens/map) documents holders, grouped
transfers, clusters, cached results, update timestamps, forced refresh and historical queries. Its private
architecture is unverified. Everything below is a **proposed design**, not a description of their stack.

### Proposed pipeline and choices

```text
chain source → chain adapter → Kafka → processors / ClickHouse ingestion
                                          ↓
                              queryable data and derived state
                                          ↓
                                    API / cache → map UI
```

- An adapter decodes chain-specific data. Standardization can happen before Kafka, or a processor can
  consume raw topics and publish standardized topics. Kafka itself does not normalize data. Keep source
  identity and chain-specific semantics; new chains can require downstream changes.
- Kafka provides retained logs and independent consumer progress. Direct database writes with a durable
  chain checkpoint are a simpler alternative when history retrieval and one destination suffice.
- A topic has partitions: separate ordered logs. Kafka preserves append order within a partition, not
  blockchain chronology. Backfills, multiple producers and reorgs need application-level handling.
- A candidate key is `(chain, token)` for token-local work. A popular token can become a hot partition.
  Changing partition count or routing can move keys; ordering assumptions need a migration plan.
- In a normal consumer group, each partition has one assigned consumer at a time. Rebalancing changes
  ownership. Extra consumers beyond available partitions do not increase active consumption parallelism.
- A committed offset identifies the **next record to read**, per group/topic/partition. Write durably,
  then commit; crashes can replay writes. Kafka supports auto-commit too, but it must not outrun processing.
  Offsets can instead be stored with results where the destination supports an atomic implementation.
- ClickHouse suits column scans and aggregations; PostgreSQL also supports history and append-only data.
  Neither database determines whether the application's data model preserves history.
- A unique-looking event key does not enforce uniqueness in ClickHouse. ReplacingMergeTree merges rows
  with equal sorting keys eventually. Correct query-time deduplication, such as FINAL with a suitable
  schema, must precede aggregation. GROUP BY with SUM alone still counts duplicates.
- Incremental materialized views process inserted batches. Source deletes and later source deduplication
  do **not** automatically repair their target tables. Derived state needs explicit correction or rebuild.
- Balances can come from authoritative chain state at a known block. A balance snapshot plus complete,
  valid changes can avoid full-history replay where token semantics permit it. Transfer logs alone are
  not universally sufficient. Observed events are not automatically canonical truth.

### Incident drill: ClickHouse stops accepting writes

1. **Detect:** compare a chain's chosen safe/finalized target with the last **contiguous, fully processed**
   checkpoint. A maximum observed height can hide gaps. Track checkpoint age and hash as well as height.
   An API-level freshness probe measures user impact; internal metrics locate the failure: insert errors,
   consumer lag per partition, disk capacity, replication and merge backlog.
2. **Protect:** do not commit failed writes. Bound consumer buffering and retries. Monitor Kafka disk and
   retention headroom. Historical recovery from a chain provider requires accessible retained history;
   do not assume any RPC endpoint can supply it.
3. **Restore:** identify and repair the database fault, check durable writes, then verify each committed
   offset is still available. Do not silently reset to latest if retention removed needed records.
4. **Reconcile:** a Kafka offset is not a chain checkpoint. Check the stored checkpoint hash against the
   current canonical chain. If it differs, walk back to a common ancestor and repair the affected range.
   Replayed events also need canonical checks or a reliable reorg-correction stream: even unread Kafka
   records may describe blocks orphaned during the outage.
5. **Repair safely:** stop conflicting writes for the affected scope; preserve last known-good serving
   data or label it stale. Invalidate orphaned block hashes, fetch the replacement branch and explicitly
   rebuild affected balances/aggregates from valid state. Wait for repair visibility, validate a consistent
   checkpoint, then publish repaired data and invalidate affected caches. Resume through an idempotent
   path; a key alone is not idempotency. Avoid blind height-range deletes racing with replacement writes.
6. **Verify:** recovery processing exceeds arrivals; backlog drains; contiguous canonical checkpoints
   advance within the chosen freshness target; no missing ranges remain. Compare sampled balances at
   the **same block hash**, verify maps/cache freshness and sustained database health. Exact equality to
   latest chain head is neither necessary nor sufficient.

### Reorg example

Stored branch: `100:A → 101:B → 102:C`. Current branch: `100:A → 101:X → 102:Y → 103:Z`.
Block 100 is the common ancestor. Invalidate B/C, ingest X/Y/Z, and repair derived state from a valid
checkpoint. Height 102 existing in both branches does not make the data equivalent. On EVM chains, an
observed log can be identified by chain, block hash, transaction hash and log index; canonical membership
is a separate fact. Other chains need their own event identities.

### Next practice and morning recall

- Explain why equal maximum heights can hide missing blocks and orphaned data.
- Explain row versus column storage, sorting keys versus partitions, replicas versus shards, and why
  many tiny inserts burden ClickHouse merges. These topics still need a focused lesson.
- Explain Kafka replication, acknowledgments and retention; no buffering system gives unlimited safety.
- Redraw the pipeline; give one reason and one cost for each component. Ask the interviewer which parts
  match their actual design, their freshness target, reorg policy and most recent production incident.
- Keep experience claims separate from design reasoning: production SRE and protocol infrastructure are
  evidenced; indexer authorship and production Kafka/ClickHouse depth are not established here.

### Primary references

- [Kafka consumer semantics](https://kafka.apache.org/41/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html)
- [ReplacingMergeTree](https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/replacingmergetree)
- [ClickHouse views and source-change limitations](https://clickhouse.com/docs/reference/statements/create/view)
- [Canonical block references and balance reads](https://eips.ethereum.org/EIPS/eip-1898)

## Final round — CTO (2026-10-20)

Personas loaded for this round: `agency-deal-strategist` (economic buyer, terms, qualification gaps),
`agency-french-consulting-market-navigator` (CDI vs freelance, Yofy margin, TJM), `agency-sre-site-reliability-engineer`
(technical frame). Platform and security personas are not relevant — no IDP or audit scope in this role.

**The round decides two things:** whether Vincent can own reliability of a 15+ chain indexing pipeline without
a team around him, and the terms. Everything technical is secondary to those two.

### Stories to rehearse (90 seconds each, seven beats from `docs/interview-incident-stories.md` §3)

1. **Frame D — Kiln fleet degradation.** 40+ production networks, $8B+ secured, multi-protocol integration.
   Strongest domain overlap: same problem class as their indexer fleet.
2. **Frame E — Cost runaway, −25%.** Cometh. Ties directly to cost-per-chain and capacity questions.
3. **Frame A — Bare-metal HDS cluster recovery.** Docaposte. Proves recovery under a control plane you cannot lean on.

Each needs the false lead and the permanent change. A story without those two reads as a summary.

### Honest limits, stated before they are probed

- Indexer authorship: none. Operated the infrastructure and integrated protocols; did not write the indexer.
- Production Kafka/ClickHouse depth: design reasoning only; the working reference above is proposed design.
- Owned SLO/error-budget programme: building it in the `ml-platform-on-k8s` artifact, not run at scale.
- Production Python/Go: operational scripting only.

### Answer shapes

| Likely CTO question | Shape |
|---|---|
| How would you make indexing reliable across 15 chains? | Per-chain freshness target, contiguous checkpoint (height + hash), reorg correction path, backpressure and lag alerts, cost per chain |
| On-call with a small team | Tiered alerting, noise budget, runbooks per failure class, page only on user-visible impact |
| Build or buy the data stack | Managed Kafka/ClickHouse first; self-host only where cost or query shape demands it |
| First 90 days | Measure current lag and gaps per chain, inventory the adapters, set freshness targets, cut the worst noise |
| Why leave AI-platform direction for this | Kiln receipts are the same work; state the Web3 lane plainly, no apologising |

### Questions to ask (five, in this order)

1. Who owns the indexer today, and what is the on-call rotation?
2. Which stack: Kafka, ClickHouse, which RPC providers, how many chain adapters?
3. Where does reliability hurt most now — reorgs, lag, or cost?
4. Is the contract a direct French CDI, or through Yofy? Remote or hybrid?
5. What is the confirmed band, and when is the review?

### Terms

- **€70k ask stands.** It is a labelled exception, already below the €80k floor. Do not move it down under pressure.
- **Freelance fallback:** €550/day opening, €500/day floor (cost parity with €70k CDI at 200 billable days).
  Confirm whether Bubblemaps contracts directly or via Yofy — agency margin compresses the rate.
- **Do not name a number first** if the CTO raises comp; make them state the band.
- A €70k French CDI that starts quickly outranks a better-titled role that needs a move. That is the earliest-start rule.

## Product and infrastructure map (sourced 2026-10-18)

All facts below come from `bubblemaps.io`, `docs.bubblemaps.io` (API v0.3.2) and `wiki.bubblemaps.io`.

### What the product is

- **Bubblemaps V2** (v2.bubblemaps.io): a token map of the **top 250 holders**, bubbles sized by holdings,
  links between bubbles where a transfer happened (any token, sometimes cross-chain). Clusters of linked
  holders are the core insight. The map is guaranteed refreshed **within the last 6 hours**.
- **Magic Nodes**: adds non-holder intermediaries (addresses that forwarded everything and now hold 0), which
  exposes clusters the default map misses. Shiba Inu example: seven added addresses turn a 3% cluster into a
  large one.
- **Time Nodes**: splits a CEX/DEX into time windows, so wallets funded in the same window link to each other.
  Newly shipped: clusters started listing their time nodes in the API on **2026-10-16**.
- **Time Travel**: historical state of a map at a chosen timestamp.
- **Intel Desk** (intel.bubblemaps.io): community investigations. Cases are pages; BMT votes set a multiplier
  (80% of votes → 8x); investigators earn points for featured threads; anyone can fund a bounty.
- **B2B**: iframe widget and the Data API, sold on credits. The wiki says most revenue comes from B2B iframe
  integrations and onchain investigation services. $3M equity raised in 2023; BMT emissions start in 2026.

### Data model, documented

- A token key is `(chain, address)`; `native` covers the chain coin.
- Transfers are grouped by `(from_address, to_address, token_ref)` and returned as `GROUPED_TRANSFER`.
- Only **indexed tokens** create clusters, to avoid dust-attack false positives. A token's own map always
  includes its transfers.
- Nodes carry `holder` / `magic` / `time` / `manually added` roles, wallet types (EOA, contract, CEX, DEX) and
  tags (fresh, supernode, transfer count). Supernodes (>200k transfers) are hidden and excluded from links
  between two supernodes.
- Metrics: supply share held by CEXs, DEXs, contracts, fresh wallets (<10 days); `top_10_adjusted`;
  `bundles` (largest 10 clusters); score 0–100; Gini; Herfindahl-Hirschman; Nakamoto coefficient.

### Infrastructure, documented versus inferred

Documented: map computation with caching (TTL depends on token age, `X-Dt-Update` header, `refresh=true`),
history queries by timestamp, server-side clustering with magic and time nodes, per-chain chain ids, a
credit-metered API, and a cache-hit path measured in milliseconds against up to a minute for outliers.

[INFERENCE] the internals, since no public architecture exists: per-chain RPC/WS ingestion and block
checkpointing, a transfer store, a clustering worker, a map cache, and the API in front. Their own docs hint at
the shape: cache TTL by token age implies a refresh scheduler; history mode implies stored per-block state;
supernode suppression implies precomputed transfer counts.

```text
RPC / WS per chain → adapters → transfer + holder store → clustering (links, magic, time) → map cache → API
                                                                                         ├→ V2 app
                                                                                         ├→ iFrame widget
                                                                                         └→ B2B API
Intel Desk (cases, votes, bounties) sits beside the data layer and feeds investigations.
```

### Non-SRE experience to surface

1. **Governance and compliance**: led the ISO 27001 implementation at Cometh. Auditors, controls, evidence.
2. **Cost ownership**: 25% cloud-cost reduction at Cometh. Unit economics matter for a data product.
3. **Architecture translation**: Kiln bullet, infrastructure constraints turned into product and engineering
   decisions across teams.
4. **Regulated operations**: HDS-certified healthcare at Docaposte. Correctness under audit and recovery.
5. **Developer-facing documentation**: written at Bitgen. Relevant to a company that sells an API.

Do not claim customer-facing sales or data science. The nearest real shape is cross-team and audit work.

### Web3 culture, shown not announced

- Kiln (40+ networks), Bitgen (Ethereum on Kubernetes), Cometh (blockchain tooling) are real crypto receipts.
- Use the domain vocabulary correctly: finality, reorg, RPC provider, indexer, CEX/DEX flows, wallet
  clustering, sybil, sniping, airdrop farming.
- Be able to walk one map out loud: a token, its clusters, and what the cluster means.
- The CTO will test judgement, not vocabulary. Say what a reorg does to a pipeline, and what you would do about it.

### Questions for the CTO

1. How many RPC providers per chain, and what happens on a provider outage?
2. Is clustering computed on write or on read, and how long does a new chain take to onboard?
3. Which storage holds transfers and history today?
4. What breaks first when a new chain is added?
5. Team size, on-call, and who owns the indexer today?

## Recruiter-screen answers

**Answered on the 2026-09-29 call:**
- Compensation: recruiter quoted €60–80k; candidate asked **€70,000 minimum**

**Still unanswered — open as of the recruiter call; confirm which of these the CTO call closed:**
1. **Remote policy** — French company confirmed; is the role remote, hybrid, or on-site?
2. **Which entity pays** — Bubblemaps directly as a French CDI, or via Yofy as EOR/contractor? (French company makes direct employment likely, but confirm)
3. **SRE vs Data Engineer split** — the title covers two distinct roles. Which is the actual job?
4. **Team size, on-call model, current infrastructure** — and what is actually in production today?
5. **Whether the €70k ask is accepted**, and the full band for this level — **not raised on the CTO call**; still open
6. **Where the data pipelines ingest from** and at what volume (chain indexing scale)

## Timeline

- Recruiter call: **2026-09-29**
- **CTO call: 2026-09-30 → advanced to the technical interview** (Stage → Interview)
- Scheduled: **technical interview 2026-10-06 (morning), with a data engineer** — role is SRE + Data
- Screen dates: **2026-09-29** (recruiter) · **2026-09-30** (CTO)
- Interview dates: technical round with a data engineer — **2026-10-06 (morning)**
- Outcome: pending

## Outcome record

- Stage reached: **Interview** (technical)
- Rejection reason: n/a — process active
- Watch: **compensation, remote policy and paying entity are still undiscussed**, and the round is data-heavy
  because the interviewer is a data engineer. The floor exception is unchanged.
- **Floor exception recorded and unchanged.** The €80k floor has not moved; this stays a labelled exception
  and does not pool with the primary lane.
