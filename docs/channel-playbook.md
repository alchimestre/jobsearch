# Channel Playbook — how the pipeline gets fed

**Status:** written 2026-09-29. Companion to `docs/12-week-strategy.md` §3 (search channels).
Everything marked **[VERIFIED 2026-09-29]** was fetched or probed live while writing this; **[INFERENCE]**
means reasoned from documentation or UI conventions, not verified in this session.

## 1. The problem this fixes

The strategy allocates **60% hiring-manager/founder outreach · 25% filtered ATS · 10% recruiter · 5%
evidence**. The tracker on 2026-09-29 held 13 issues: **12 `channel:ats`, 1 `channel:recruiter`,
0 `channel:outreach`**. Both live feeds — LinkedIn job notifications and APEC inbound — are *push*
channels, so they can only ever fill the 25% lane. That is why the pipeline looked busy and produced
tier-C bridge roles (Doctolib Staff SRE, Sinch SRE, ablefy DevOps).

Two failure modes, two fixes:

| Failure | Evidence | Fix |
|---|---|---|
| Inbound-only intake | 0 outreach issues vs a 60% target | ATS watchlist → hiring-manager messages (§3) |
| Title alerts too broad | every LinkedIn-sourced issue is tier C | Rewrite saved searches to the §2 title list, exclude seniority/GTM (§4) |

A role that fails a hard filter still gets an issue (deliberate long-shot), but it should not be how the
pipeline is *fed*.

## 2. Source stack

`jobradar` (submodule `tools/jobradar`, §6) polls the ATS layer and the machine-readable feeds. Everything
in this table was verified today unless marked otherwise.

### 2.1 Employer ATS boards — the first place a role appears

Public JSON/XML, no auth, no scraping. Polled directly by the tool.

| ATS | Endpoint | Adapter verified |
|---|---|---|
| Ashby | `api.ashbyhq.com/posting-api/job-board/<token>` | ✅ (vCluster Labs: 19 reqs, incl. *AI Infrastructure Engineer — Remote*) |
| Greenhouse | `boards-api.greenhouse.io/v1/boards/<token>/jobs` | ✅ (GitLab: 199 reqs) |
| Lever | `api.lever.co/v0/postings/<token>?mode=json` | ✅ |
| Workable | `apply.workable.com/api/v1/widget/accounts/<token>` | ✅ — but returns **429** after bursts; treat as best-effort |
| SmartRecruiters | `api.smartrecruiters.com/v1/companies/<token>/postings` | ✅ (BoschGroup: 4,801 reqs) |
| Personio | `<token>.jobs.personio.de/xml` | ✅ (DACH SMB/scale-up boards) |
| Recruitee | `<token>.recruitee.com/api/offers/` | ✅ |

Token case is **not** significant (checked Ashby + Greenhouse), so `discover` can guess slugs safely.

### 2.2 Machine-readable aggregators (polled by the tool)

| Source | What it gives | Verified volume |
|---|---|---|
| HN *Ask HN: Who is hiring?* (Algolia API, 1st of each month) | Employer + role + location + contact, written by the hiring manager | Sept 2026 thread: 255 top-level posts, **36 matching the target titles** |
| Arbeitnow API | Germany-wide, English-speaking/visa/remote filters | 13,190 open, 474 added/day; API 326/page |
| RemoteOK | Remote-first, global | 99 live |
| WeWorkRemotely DevOps RSS | Remote DevOps/SRE | 19 items |
| EU Remote Jobs RSS | EU-timezone remote | 15 items |
| SwissDevJobs RSS | Switzerland | 195 items |
| GermanTechJobs RSS | Germany | 291 items |
| CryptoJobsList RSS | Crypto/Web3, all functions — polled, filtered by the scorer | 100 items; employer recovered from the `-at-<company>` URL slug |

### 2.3 Browser-only (Cloudflare blocks scripts — keep as bookmarks)

jobs.mlops.community (claims 250+ AI roles), Welcome to the Jungle (FR + remote, AI filter),
Wellfound, startup.jobs, Himalayas, SEEK (AU), jobs.ch (296 *platform engineer* hits), aijobs.com,
aijobs.ai, aidevboard.com, foorilla.com/hiring (where ai-jobs.net now redirects),
berlinstartupjobs.com (`/skill-areas/ai/`, `/skill-areas/remote/` — 32 IT roles, small board).

### 2.4 Institutional (Switzerland lane)

EPFL `epfl.ch/about/working/job-openings/` ✅ live; CSCS and ETH run their own careers pages (paths move —
follow from the homepage). These are relationship targets first, applications second.

### 2.5 Web3 infrastructure sources (added 2026-09-29)

Scope widened by Vincent's instruction: Web3 infrastructure is an admitted track in every lane, ML/LLM stays preferred but non-blocking, and the return to work should be as early as achievable. Because Web3 sits on the deepest evidence on the CV (Kiln $8B+/40+ protocols), it is the **fastest-to-income** track.

**Employer boards, already polled** — 46 Web3 employers were resolved to public ATS endpoints and merged into the watchlist (157 boards total): Alchemy, Anchorage Digital, BitGo, Bitpanda, Bitvavo, Blockdaemon, Blockstream, Bybit, Circle, Coinbase, Compound Labs, Consensys, Dune, Elliptic, Espresso Systems, Fireblocks, Kraken (`ashby:kraken.com` — note dots are valid slugs, so resolve these from the careers **URL**), Ledger, Matter Labs, Mysten Labs, Nethermind, Nomic Foundation, OKX, OP Labs, OpenZeppelin, Parity Technologies, Polygon Labs, QuickNode, Ripple, SwissBorg, Tenderly, TRM Labs, Turnkey, Uniswap Labs, and others. Re-run the sweep with `jobradar discover --json <name>` / `jobradar import seed.yaml --write`.

**Aggregators** (live, verified 2026-09-29; no RSS except CryptoJobsList, so they are browser sweeps): `web3.career` (incl. `/remote-jobs`), `cryptocurrencyjobs.co`, `remote3.co`, `crypto.jobs`, `web3jobs.io`, `cryptojobs.com`. `cryptojobslist.com` is bot-blocked but its `/rss` endpoint is not — that feed is polled by the tool.

**Coverage gap, stated plainly:** the largest Web3 infra employers — Chainlink Labs, Lido, Kiln, Chorus One, DFINITY, StarkWare, Figment, P2P.org, Everstake — are **not** on the seven public ATS endpoints the tool can poll (checked by name sweep and explicit token probing). For those, the aggregators above plus the employer's own careers page are the only route. Kiln and Cometh matter twice here: prior employment means a warm route, which is the single highest-conversion channel available.

**Forums and communities** (relationship and visibility, not an application channel): EthResearch (`ethresear.ch`), Ethereum Magicians (`ethereum-magicians.org`), EthStaker and Ethereum R&D Discords, Flashbots forum, Lido Research forum, Optimism and Arbitrum governance forums, Developer DAO, BuidlGuidl. Practical use: answer one technical question a week in the infrastructure channels; that is the same 60%-outreach lane with a public evidence surface.

**Signal newsletters** (weekly, ~10 min total): Week in Ethereum, Bankless, The Defiant, Blockworks, EthStaker. They surface organisations before they post a requisition.

**Grants and bounties** — visibility and short-term income, not employment: Ethereum Foundation ESP, Optimism RetroPGF, Gitcoin rounds; Immunefi / Code4rena / Sherlock / Cantina for paid security and tooling work **[INFERENCE — not verified this session]**. Nothing here displaces an application; it is the "public evidence" lane applied to Web3.

### 2.6 Ranked by signal-to-noise

1. **ATS watchlist** — first-mover, feeds outreach, dedupes cleanly.
2. **HN Who-is-hiring** — highest density of directly contactable AI-infra roles.
3. **Niche RSS** (SwissDevJobs, GermanTechJobs, EU Remote, WWR, CryptoJobsList).
4. **Web3 aggregators** (§2.5) — the only route to the Web3 employers that hide their ATS.
5. **Broad boards** (Arbeitnow, RemoteOK) — volume, requires the scorer to be useful.
6. **Institutional career pages** — low volume, high fit for CH.
7. **LinkedIn alerts** — one input among several, restructured per §4.

### Marking an application is the trigger

Pressing `a` (applied) in the TUI writes the status locally **and** runs the configured hook,
`scripts/log_applied.py`. It finds an existing issue for the same posting (jobradar uid marker →
posting URL → company + role) and either comments on it and sets Stage **Contacted**, or writes
`docs/opportunities/<company>-<role>.md` and creates the labelled issue from the opportunity
template, already on the board at Contacted. One line reporting exactly what happened appears in the
TUI status bar; a failed hook (unauthenticated `gh`, rate limit) is surfaced there without losing the
status write. `python3 scripts/log_applied.py --dry-run` shows the plan and touches nothing;
`python3 scripts/test_log_applied.py` runs its self-checks.

Market and tier are **mechanical defaults** — lane → market label, ML-platform signals → tier b
otherwise c — and both are flagged for review in the issue body. The hard-filter verdict, JD
analysis, and application answers are deliberately left unwritten.

## 3. Operating the ATS watchlist

```bash
cd tools/jobradar
uv sync
uv run jobradar scan                 # ~75s for 164 sources
uv run jobradar tui                  # ranked, deduped queue
uv run jobradar discover "NewCo" --write      # name or any careers URL
uv run jobradar export --since 7d --decision high
```

- The watchlist currently holds **157 boards** (target research + AI-infra sweep + 46 Web3 employers).
  Re-validate a new list with `jobradar import seed.yaml --write`; batch-discover with
  `jobradar discover --json <name>` piped from `xargs -P 12`.
- **Auto-learning is on by default**: any job URL from a feed that points at a known ATS pattern adds that
  board permanently (`auto: true`) and polls it from the next scan. Feeding the tool a single HN link is
  enough to adopt a company.
- **Mute instead of deleting.** `enabled: false` on a row stops polling *and* stops auto-learning from
  re-adding it; the entry remains as a record of the find.
- Auto-learning can adopt a **group or subsidiary** board — a Hetzner feed item pointed at
  `xneelo.recruitee.com`, and Personio's public Recruitee board is a demo board ("API Job - Berlin -
  Musterstr"). Learned boards are labelled by their slug when the posting's employer name does not match
  it; mute or drop anything outside the lanes.
- Scan of 2026-09-29 (post-widening): 164 sources, **0 errors**, 231 postings stored — 6 `high`,
  225 `review`. The `high` bucket is deliberately small: in-lane, in-scope, strong title. Work `high`
  first, then `jobradar list --lane eu-remote --decision review`.
- **Budget: ≤1.5 h/week on discovery.** Run the scan, triage, and spend the rest of the 60% lane writing
  to hiring managers. More sources do not help if the outbound lane stays empty.
- **Scope gate (added 2026-09-29).** The scanner admits only postings that are **in the EU/EMEA/AU** and
  written in **English or French**. Everything else is stored with decision `out` and hidden from the
  default queue: on 2026-09-29 that was `249` stored postings — **`163` in scope, `86` out** — with
  `5,988` postings excluded at scan time (43 Americas, 15 APAC, 28 German-language JDs among the stored
  ones). Audit or re-tune with
  `jobradar list --decision out [--region americas] [--reason lang-de]`; the TUI's `f` key cycles
  high → review → out → all. Only the JD *language* is judged, never the country — English-language JDs at
  German employers stay in the Berlin lane.
- **Triage by track**: `jobradar list --reason blockchain` (or `mlops`, `k8s`, `web3`) isolates a lane;
  `jobradar rescore --prune` re-applies rule changes to already-stored rows.

### From posting to outreach (the actual point)

For each `high` posting: find the hiring manager on LinkedIn (company + `platform`/`infrastructure`/
`SRE` + manager titles), send the evidence-package message, then create the issue with
`channel:outreach` at Stage **Contacted** (Prospecting if the role is not yet posted). Applications via
the employer ATS follow as `channel:ats`, Stage **Contacted**, per `AGENTS.md`.

## 4. LinkedIn: filtering, and what to use it for

### 4.1 Saved searches

LinkedIn's keyword box accepts quoted phrases and `AND` / `OR` / `NOT` / parentheses **[INFERENCE]** —
verify once by running a query and checking the result count differs from an ungrouped one. If the
operators are rejected, fall back to one saved search per title in the §2 title list.

**Primary search (EU-remote lane):**

```
("ML Platform Engineer" OR "MLOps Engineer" OR "Machine Learning Platform Engineer"
 OR "ML Infrastructure Engineer" OR "AI Platform Engineer" OR "AI Infrastructure Engineer"
 OR "Inference Platform Engineer" OR "Training Platform Engineer" OR "SRE ML Platform")
NOT (intern OR Werkstudent OR "working student" OR Recruiter OR Sales OR "Head of" OR Director
 OR Staff OR Principal OR Lead OR "8+ years" OR "10+ years")
```

> **Amended 2026-09-29 — seniority exclusions added.** The original clause omitted them, and the rejection
> data showed that was a defect: both #6 Doctolib (`Staff`, 8+ years) and #16 Synthesia (`Senior or Staff`,
> 7+ years) were refused pre-screen on bars stated in the JD before applying. Neither produced a classified
> reason, so both were pure cost. Do **not** exclude `Senior` — that is the target band.
> Operational checklist: `docs/linkedin-saved-searches.md`.
>
> **Location is the higher-impact fix.** A keyword-only alert is what produced the tier-C pile; every alert
> needs its geography set.

**Variants to save separately:**

| Lane | Keywords | Filters |
|---|---|---|
| EU-remote / FR-compatible | query above | Workplace type = **Remote**; geography = European Union + France |
| Berlin | query above + `Kubernetes OR Kubernetes Platform` | Geography = Germany (Berlin metro) |
| Switzerland | query above | Geography = Switzerland (Zurich, Basel, Lausanne, Bern, Zug) |
| Secondary (≤¼ of EU-remote) | `"Forward Deployed Engineer" OR "Solutions Engineer" OR "Deployment Engineer"` + `Kubernetes OR "on-prem"` | Remote + EU; reject pre-sales/quota wording |
| Web3 infrastructure | `("Blockchain Infrastructure Engineer" OR "Protocol Engineer" OR "Node Operations" OR "Staking Infrastructure" OR "Platform Engineer Web3" OR "SRE Blockchain" OR "DevOps Blockchain")` | Remote + EU; add `NOT (sales OR marketing OR community OR partnerships)` |

Rules that matter more than the query:

- **Web3 roles surface on the aggregators (§2.5) and employer boards before LinkedIn**, so for that track the alert is a backstop, not the source. The 46 verified Web3 boards are already polled directly.
- **Alert frequency: daily**, not weekly. A posting found on day 9 is a posting found late.
- Location must be set per alert — a keyword-only alert is what produced the tier-C pile.
- Turn off the generic "job recommendations" digest; keep "jobs where you'd be a top applicant" only if it
  respects the same filters.
- **Deduplicate mentally**: LinkedIn reposts one requisition per city/region. `jobradar` keys on
  (company, title) for exactly this reason.
- **Never Easy Apply** at a target company — apply on the employer's ATS. It parses better, and the URL
  tells you the board token, which the watchlist adopts automatically.

### 4.2 What LinkedIn is actually for

1. **Hiring-manager discovery** — the input to the 60% lane. Saved people searches (company + platform/
   infrastructure/SRE + `Engineering Manager`/`Lead`/`Head of Platform`), not job alerts.
2. **Positioning vocabulary** — the headline/About must carry the same terms as the searches above, or
   recruiter-side search will not surface the profile.
3. **Company following** — follow every watchlist company to catch announcements before the ATS post.

It is not a channel for volume applications, and it is not a source of first-mover information.

## 5. APEC, France Travail, and the French lane

- **APEC** stays for France-salaried coverage *and* France Travail obligation compliance (actualité,
  convocations, offer-acceptance rules — see §10 of the strategy). It is not a targeting channel: the
  French AI-native employers post on Ashby/Greenhouse/Workable, and those are now polled directly.
- Add **Free-Work** (`free-work.com/fr/tech-it/jobs`) ✅ live and **Welcome to the Jungle** (browser) for
  FR tech; both index French remote roles that APEC misses.
- Agency recruiters remain inbound/opportunistic only, per ticket 08.

## 6. The tool

`tools/jobradar` is a **git submodule** of `alchimestre/jobradar` (private), pinned to a commit. The tool
owns source plumbing and ranking; this repo owns strategy, docs, and the pipeline tracker.

```bash
git clone --recurse-submodules git@github.com:alchimestre/jobsearch.git
git submodule update --init --recursive      # after a plain clone
git submodule update --remote tools/jobradar # pull newer jobradar commits
```

Contract between the two: `jobradar export` produces markdown rows with a stable `uid`; that uid goes in
the opportunity doc as the tracker cross-reference. Filtering logic lives in the tool
(`config.yaml` weights), role-admission policy lives here — when this document changes, update the tool's
rules to match.

## 7. Weekly cadence

| When | Action | Time |
|---|---|---|
| Mon | `jobradar scan` + triage new `high` | 20 min |
| Mon–Thu | Outreach to hiring managers (the 60%) | majority |
| Wed | ATS applications for filtered roles (the 25%) | 2–4 roles |
| Fri | Review: response rate by channel; log every contact as an issue | 1 h |
| Fri | Re-check browser-only boards (§2.3) | 15 min |

Instrumentation that must stay honest: **`channel:outreach` issue count per week**. It is currently 0 and
is the only number that measures the lane carrying most of the plan.

## 8. Adaptation

- If outreach response rate < 10% over weeks 2–4: change targeting *or* messaging, not both, and label the
  cohort (strategy §5, week 4 checkpoint).
- If the `high` bucket stays empty for two weeks: the ATS watchlist is too narrow, not the filters — add 20
  employers from the lane that is under-represented.
- If a source produces nothing usable in three consecutive weeks, delete it from `config.yaml`.
