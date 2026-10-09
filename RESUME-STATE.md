# Resume state — read this first

**Paused 2026-09-14 → 2026-09-23 inclusive. Resume 2026-09-24 (Thursday).**

No outreach, applications, follow-ups, or project work during the pause. Nothing is waiting on Vincent
that cannot wait until 09-24; this file exists so the next session starts cold with correct state.

## Where the plan is

| Item | State |
|---|---|
| 12-week plan | Week 1 complete; **Week 2 starts 2026-09-24** (whole plan shifted +10 days, 2026-09-14) |
| Mode | Normal — late-cliff (~Feb 2027) and last-resort (~Apr 2027) did **not** shift; they are cliff-anchored |
| Evidence project | `~/projects/ml-platform-on-k8s` — Week 1 exit check passes on the cluster; no remote yet |
| CV / LinkedIn | Applied and committed (2026-09-13). Story is consistent |
| Pipeline | **29 issues: 18 open, 11 closed.** Open: #1 Cohere (FR), #4 ablefy, #5 vCluster, #7 Sinch, #9 SAP Fioneer, #13 Bubblemaps (`Interview`), #14 Cohere (EU), #15 Dialectic, #17 ClickHouse, #18 Nebius ML Infra, #20 Peak3, #22 1GLOBAL (DE), #25 Blockstream (CH), #26 Anagram, #27 360Learning (FR), #28 Filigran (FR), #29 idnow (DE), **#30 Atlantic venture (DE, Tier A)**. Closed: #3 vivenu, #6 Doctolib, #8 Lity, #10 Otera, #11 Workist, #12 Langdock, #16 Synthesia, #19 Nebius Token Factory, #21 MarvelX, #23 n8n (Agentic), #24 n8n (DevX) — **all eleven `reason:unknown`** |

### HN "Who is hiring? (October 2026)" sweep — 232 top-level posts, in-scope shortlist (2026-10-07)

Thread: https://news.ycombinator.com/item?id=49922569 (341 comments, 232 top-level job posts). `jobradar scan`
was run to absorb it (2026-10-07).

**⚠️ The queue silently drops this thread's most relevant roles — verified defect, details at the end of this
section.** The 23 rows the store does hold from the thread are almost all `out`/`review` rows with low
relevance (VLM Run, Loft Orbital, Chronograph, Odin, Axmed, ML6, ChainSecurity…): the feed parsed 210
postings, then `min_score: 3` pruned the rest.

**Tier 1 — worth applying or preparing for**

| Company | Role | Where | Verdict |
|---|---|---|---|
| **Kraken Tech** (Octopus Energy) | **Senior SWE, AI Foundations** — Ashby `krakentech` | **Paris, Berlin**, London, Manchester · hybrid | **Best in-scope find of the thread.** The team owns *secure cloud development environments for AI-assisted engineering, internal model access and guardrails, agent orchestration with Slack/GitHub/Notion, evals*. That is agentic-AI platform engineering, and it matches the 2026 AI-assist/orchestration PoCs plus the platform evidence. Paris is a listed location → France-compatible. Costs: hybrid (relocation to Paris or Berlin), Python/Django-leaning stack |
| **Namespace** | Infrastructure Software Engineer | **Switzerland · Germany** · UK · US, remote or hybrid | Control planes for their own fleet — K8s/Terraform/Ansible and bare-metal match. Gate: *"writing the software that runs fleets"* in **Go**, plus datacenter/network depth — both inside the current evidence gaps |
| **Prior Labs** (now part of **SAP**) | ML Engineer, Infrastructure | Berlin · Freiburg · NYC, on-site (remote exceptional) | The **exact primary-lane role** — multi-cluster GPU infra, Slurm on GCP, cost-per-FLOP ownership, ~€10M+/yr compute. Gates are the excluded ones: 3+ yrs production **GPU fleet** + distributed-training depth, PyTorch internals. Long-shot now; the clearest statement of what the lane demands |
| **Rentman** | DevOps Engineer | Utrecht (NL), hybrid | IaC migration ownership (Terraform/Pulumi/CDK), unify Fargate + K8s, observability, cost, IAM. First serious **NL-lane** role since the 2026-09-30 admission. Gates: *"personally led"* an AWS IaC migration; AWS-primary estate |

**Tier 2 — flagged, reachable, or track-dependent**

- **Tether** (100% remote worldwide, Web3+AI): *AI Inference Engineer (QVAC)*, *AI Harness Engineer* (JS/TS,
  agent harness + local inference + P2P), *Technical Lead — GPU Infrastructure*. Verified **`DevOps Engineer
  (QVAC)` is release/build engineering** (GitHub Actions, CMake, NPM/mobile signing) — not platform/SRE.
  The rest are engineering/research-track, not SRE.
- **JUPUS** — Engineering Manager, Applied AI, REMOTE (CET±2), **up to €160k**: best comp/geography match in
  the thread, but a **management** role (5 reports). A career-track decision, not an evidence question.
- **Reef Technologies** — Senior Python Backend Engineer, REMOTE EMEA, B2B 45–70 USD/h: GPU-enabled
  sandboxed container runners, decentralized scheduling. Contract + Python authoring.
- **EggAI** — IT Operations Lead / platform engineers, REMOTE (EU): boutique enterprise-AI consultancy.
- **Quobyte** (Berlin, on-site): storage for AI/HPC at exabyte scale — superb craft, but the published bands
  (**60–100k** SWE, **50–90k** infra) breach the €80k Berlin floor. Same disqualifier class as Lity #8.
- Also noted: **Open Education Applications / Neon** (Utrecht) is the first NL row to demand **Dutch**;
  **Charly** (Berlin) 60–100k and **PAGNOS** (remote DE) €75–80k breach the floor; **Anthropic** (CH) and
  **Google Munich** are Staff+ → §2 seniority fail; **Mattermost** is US/Canada-only; **PostHog**'s SRE roles
  are Americas-only; **ClickHouse Labs** wants research scientists; **Modash** (remote EU, €75–110k) and
  **Better Stack** are product-engineering, not platform.

### jobradar defect — the HN feed drops the thread's best infra roles (2026-10-07, verified)

Found while sweeping: the six most in-scope postings scored **≤ 0** and were pruned by `min_score: 3`
(`store`/`scan` deletes rows with `score < 3 AND status='new' AND decision IN ('low','out')`), so they never
reach the TUI. Scores below come from the tool's own scorer (`_scorer(cfg).match(job)` on the fetched feed):

| Post | `parts[1]` → title | location → | score | cause |
|---|---|---|---|---|
| Namespace | `San Francisco, CA / New York, NY / Zurich, Switzerland / Remote` | `Full-time` | **0** | post leads with locations; no keyword in the title field |
| QUOBYTE | `Santa Clara, CA and Berlin, Germany` | `Full-time / Remote` | **0** | same |
| Prior Labs | `Berlin, Freiburg, NYC` | `ONSITE` | **0** | same |
| Tether | `AI Harness Engineer` | `REMOTE (Worldwide)` | **0** | "AI Harness" matches no `title_rules` entry |
| Kraken Tech | `Senior Software Engineer - AI Foundations` | `London, Paris, Berlin, Tokyo, New York, Remote` | **0** | "AI Foundations" matches no `title_rules` entry |
| Rentman | `DevOps Engineer, Senior Frontend Developer` | `Utrecht, NL` | **−3** | a second role in the title hits the **`frontend` hard negative** (−5); NL is a target country and was not the problem |

Two distinct bugs, both in the pipeline rather than in the thread:

1. **`fetch_hn_whoishiring` takes `parts[1]` as the title** (`src/jobradar/sources/feeds.py:187`) on the
   thread's `Company | Role | Location` convention. Posts that lead with *locations* (a common HN style)
   yield a location string as the title and `Full-time` as the location — the role is lost entirely.
2. **`title_rules` has no coverage for agentic-AI platform titles** (`AI Foundations`, `AI Harness`,
   agent platform, AI enablement) — the fastest-growing category in this thread — and a multi-role title can
   trip a hard negative meant for a *different* role in the same post.

Cheap fixes, in increasing cost: (a) add `ai foundations|ai harness|agentic|ai enablement|ai tooling` to
`title_rules`; (b) prefer the *first* pipe part that looks like a role rather than blindly taking index 1, and
score hard negatives against a single matched role instead of the whole title; (c) exempt the HN feed from
`min_score` (or lower its floor) so comments are reviewable in the TUI. Not applied — the submodule is
Vincent's call.

### idnow #29 applied — DE-lane bridge, and the first salary target actually specified (2026-10-07)

**AI Platform Engineer (f/m/d)**, Berlin/Munich **or Rennes (FR)**, on-site, posted the same day. `market:de` ·
`tier:c` · `channel:ats` · `track:bridge` · jobradar uid `07a91d9debeb76db` (score 9, `high`). Board
`Contacted`; follow-ups 2026-10-14 → 10-16, final 2026-10-21 → 10-27.

- **The title outruns the job.** Department is **Internal IT**: enterprise integration and middleware (GitLab
  CI/CD, Terraform on AWS, Node/Python middleware, MCP servers). Kubernetes is only "a plus"; no cluster,
  fleet or ML-lifecycle ownership appears. Tagged bridge on purpose despite the score of 9.
- **The clean half and the dirty half:** the DevOps side matches (Terraform, CI/CD, IAM/security, Docker/K8s);
  the job also wants shipped **Node.js/Python middleware**, which is the excluded claim. Not evidenced:
  GitLab, MCP servers, Node.js, AWS-as-home-cloud.
- **⚠️ Third AWS-primary row this week** (#11, #27, #29) — now the most repeated gap in the DE/FR lanes.

### Compensation anchors — first target numbers on record (2026-10-07)

Set for idnow (Berlin/Munich), reusable for every DE row:

| Source | Figure |
|---|---|
| §2 floor (binding) | Berlin **€80,000** |
| Workist #11, employer-disclosed, Berlin senior platform | **€80,000–100,000** |
| Berlin rows seen this week | Charly 60–100k · Quobyte 60–100k (SWE) / 50–90k (infra) · PAGNOS (remote) 75–80k |
| ERI/SalaryExpert, Germany DevOps, Sept 2026 | entry **€59k** · average **€85k** · senior **€104k** |
| Levels.fyi Munich SWE median *total* comp | ≈ **$98.7k** — big-tech-weighted, ceiling signal only |

**Rule adopted:** quote a **band whose bottom is above the §2 floor** — Berlin **€85,000–95,000**, Munich
**€90,000–100,000**; single-number forms get the upper-middle (**€90k Berlin / €95k Munich**). Munich prices
5–10% above Berlin. Never quote the floor; never quote above ~€100k at a 4-years-evidenced senior bar.
Equity at PE-owned employers should be discounted, so weight base.

**New trap recorded — Rennes.** The JD offers Rennes, France as a third location. The §2 France-compatible
floor is also €80k and French regional platform pay sits well below the German bands, so a recruiter steering
to Rennes *and* French compensation breaches the floor. Rennes is acceptable only at a German-level base.

**First real quote, for calibration (2026-10-07):** idnow #29 → **€95,000 as a single figure, no base/variable
split**. Within the Munich guidance, at the top of the Berlin band. Calibrate the guidance against the outcome
when it lands — if idnow screens on level, €95k was too high for a 4-years-evidenced senior bar in Berlin; if
it proceeds, the band was right. **Note the open ambiguity:** whether that figure is read as base or total
(if total with a ~10% variable, base ≈€86k).

---

## Updated 2026-10-09

### Atlantic AI Efficiency Venture (#30) applied — Tier A returns to the pipeline (2026-10-09)

**Platform Engineer (gn)**, one of the first platform hires at an **unnamed Atlantic portfolio venture at
pre-seed** (Berlin, on-site five days a week). `market:de` · **`tier:a`** · `channel:ats` · `track:ai`.
Recruitee offer id **2776762**; no jobradar row. Board `Contacted`; follow-ups 2026-10-16 → 10-20, final
2026-10-23 → 10-29.

- **Tier A on the strongest reading in the pipeline.** The JD names *"the GPU capacity used to serve
  open-weight models"*, evals, embeddings and open-weight serving alongside the LLM gateway/router and
  token-cost accounting — ML-serving surface **with** infrastructure ownership, not adjacent to it.
- **Best seniority fit logged:** *"typically three to six"* years, so ~4 evidenced sits in the *middle* of the
  band rather than under it — the first row where that is true.
- **Two binding unknowns, both answerable in one message:** (1) the **base band** — pre-seed with "meaningful
  equity" is exactly where the base lands under the €80k floor, and equity is not income on the cliff; (2)
  **relocation** — five days a week in Berlin, no relocation support mentioned, so a move is self-funded.
- **The gate is Python authorship.** The entire backend is Python/FastAPI/Pydantic with async, typing and
  testing; that is the excluded claim. Also not evidenced: production LLMs/evals/serving, GPU-workload
  operation (adjacent only), Scaleway, LiteLLM, Langfuse, TypeScript.
- **Genuinely attractive:** the only row where the AI-infrastructure claim *is* the job; **cost optimisation
  with measured savings** is a first-class responsibility and the CV's cost evidence (cloud spend −25% at
  Cometh) maps onto the product's own thesis; and **"practical agentic engineering"** is an explicit hiring
  criterion, which the 2026 harness/orchestration work genuinely answers.

**Pipeline consequence:** with Workist #11 closed on 2026-10-06, **#30 is now the only live Tier A row** — and
the only application this week whose track label is `ai`. It is also the first application logged with **no
salary figure stated**, so the follow-up (not the form) carries the compensation question.

### Otera (#10) closed — refused, `reason:unknown`, pre-screen

Applied 2026-09-26, refused ~10 business days later, no reason given. Board Stage → Closed. No follow-ups were
owed (first was due 2026-10-05; the refusal arrived the day before the final window opened).

- **It was the best remote-geography fit in the pipeline** — *"Remote Europe / work from anywhere"*,
  mid-senior, real multi-cloud abstraction design (GCP/Azure/AWS, Terraform, Helm, GKE/AKS/EKS) matching the
  architectural-scope criterion. Tier C and admissible only from the last-resort window, so nothing in the
  primary lane is lost.
- **Two qualifying questions died with it, because they were never asked:** (1) **is France eligible** under
  "Remote Europe" — Otera is Austrian-hosted with a German posting, and "work from anywhere" usually means
  "anywhere the entity can payroll"; (2) the band behind *"Competitive Salary Package"*. The ask was **€90,000**.
- **Unverifiable suspicion, labelled as one:** a Series A at ~80 staff with an undisclosed band is where the
  €90k ask most likely sat above range. With no reason given, that is `[INFERENCE]`, not a finding.
- **Volume signal held:** 141 applicants within a week — the highest-volume posting reviewed to date. Day-one
  application did not buy a screen.

### The funnel has now closed eleven rows and classified none

**11 closed · 11 `unknown` · 10 pre-screen.** MarvelX (#21) is still the only row that ever reached a live
screening step. Consequences:

1. **§7's adaptation rules cannot fire.** Every threshold keys on `reason:*` labels, and there are no
   classified rejections to count. The pipeline is accumulating volume without learning anything from it.
2. **The screen never comes — so stop holding the qualifying questions for one.** On this evidence, band and
   location eligibility must be asked **in writing, at application time or in the first follow-up**, not saved
   for a recruiter call that mostly does not happen. Otera needed no follow-up at all if that rule had held.
3. **The follow-up lane is still at zero** — no follow-up has been sent for any closed row and
   `docs/outreach/sent/` is empty. Combined with (2), the first follow-up email should now carry the two
   qualifying questions rather than a restatement of interest.
4. **Only two live levers can still classify a rejection:** the **MarvelX feedback request** (§3 permits
   exactly one; drafted in `docs/outreach/`, still unsent) and **Bubblemaps #13**, live at `Interview` and
   awaiting the post-interview return.

### Lane tally

| Lane | Open | Closed (all `unknown`, all pre-screen) |
|---|---|---|
| EU-remote | #1, #5, #14, #17, #18, #20, #26 | #10 Otera, #19 Nebius TF, #21 MarvelX (screened) |
| DE | #4 ablefy, #9 SAP Fioneer, #22 1GLOBAL, #29 idnow | #6 Doctolib, #11 Workist, #16 Synthesia, #23/#24 n8n |
| FR-bridge | #7 Sinch, #27 360Learning, #28 Filigran | #8 Lity, #12 Langdock |
| CH | #25 Blockstream | — |

**Today is the Friday review (2026-10-09).** The item list from 2026-10-06/07 still stands and now has one more
entry: the 11-for-11 unclassified funnel, and the rule change in (2) above.

---

## Updated 2026-10-07

### Two France-lane applications, both posted the day before

| Issue | Role | Market / tier / track | Applied | Follow-ups |
|---|---|---|---|---|
| **#28** | **Filigran — Senior Platform Engineer** | `fr-bridge` / **B** / `ai` | 2026-10-07 (Ashby) | 10-14 → 10-16 · final 10-21 → 10-27 |
| **#27** | **360Learning — Senior DevSecOps Engineer** | `fr-bridge` / **C** / `bridge` | 2026-10-07 (Lever) | 10-14 → 10-16 · final 10-21 → 10-27 |

Both remote-in-France with no relocation question, both posted 2026-10-06 (applied day 1), both with
**unpublished compensation** against the €80k France-compatible floor. Neither has a jobradar store row;
reconcile by ATS id.

- **Filigran (#28) is now the best craft match in the pipeline** on the evidence base as written — bare-metal
  Kubernetes (Docaposte MetalLB/Cilium), Helm, Ansible/Terraform, GitHub Actions, Prometheus/Grafana/Loki,
  secrets/access (Vault, Teleport, Kyverno, Cilium), **ISO 27001 lead at Cometh** mapping onto their
  FedRAMP/SecNumCloud hardening nice-to-have, French native, remote-first. Costs: **5+ years asked (~4
  evidenced)**, unpublished band, and heavier-than-usual on-call (~1 day + 1 night shift per 2 weeks, one
  weekend per ~6 weeks, compensated). Filigran is **open source** (OpenCTI, OpenBAS) — a small upstream
  contribution is visible to the team that reads the application.
- **360Learning (#27) is a deliberate bridge row**: a security-engineering role (detection content, SIEM
  coverage, honeypots, vulnerability management, audit-evidence automation) with **no ML surface**, admitted
  for income in lane #1 plus the regulated/compliance evidence that keeps recurring in this pipeline. The
  anchor is the ISO 27001 lead; the risk is that the process tests **security operations depth**, including a
  live exercise in either incident investigation (weak) or insecure-configuration review (winnable). Azure/AKS
  is the same conversion gap as #11.

### Bubblemaps #13 — technical interview done, awaiting return

Round took place **2026-10-06** (data engineer); no outcome yet. Stage stays `Interview`; no result, stage
change or follow-up date recorded until the debrief. Prep notes committed in `8b2a8b4`.

### Flags for the Friday review (2026-10-09)

1. **The France lane is drifting toward security/compliance infrastructure** — two of this week's three
   France-lane rows (#27, #28) are security-flavoured. Filigran is the one that also does platform work;
   360Learning is a pivot that builds no ML-platform evidence. Is that drift deliberate or accidental?
2. **Filigran's `track:ai` label is a judgement call.** The team owns the K8s substrate behind an agentic
   product and has an explicit agent-guardrail/agent-enablement responsibility, but the workload has no ML/GPU
   surface. Moving it to `bridge` would drop it out of the ML-platform conversion cohort.
3. **Compensation is unpublished on all three France-lane rows logged this week** (#27, #28, and the earlier
   #25-style pattern) — the €80k floor is being applied blind. Ask in the first exchange every time.
4. Carried over from yesterday: the three-instance Web3 clause conflict (#22/#25/#26), the still-empty
   outreach lane (`sent/` empty; Workist's named-recipient draft went unused), the 10-for-10 `unknown` funnel,
   the customer-facing evidence gap, and the MarvelX feedback request that is still unsent.

---

## Updated 2026-10-06

**Workist (#11) closed — refused, `reason:unknown`, pre-screen.** Applied 2026-09-26, refused ~7 business
days later; no reason given. Board Stage → Closed.

- **The strongest application in the pipeline is gone, and it was the last Tier A role we had.** The JD named
  the platform Workist's AI agents run on (Kubernetes for ML workloads, LLM gateway with region failover, GPU
  capacity planning), and the **employer-disclosed band €80,000–100,000** cleared the floor. Closest seniority
  match and closest role shape (quarterly-theme ownership, reports to the CTO).
- **The refusal carries no information.** Pre-screen, no reason: the two honest gaps (GCP-first cloud depth;
  Python read-and-debug rather than author) cannot be attributed as causes. §3's feedback request is gated on
  a recruiter screen, so it does not apply.
- ⚠️ **The outreach was never sent — and this one hurt most.** `docs/outreach/workist-senior-platform-engineer.md`
  was the **only draft addressed to a named recipient** (Fabian Brosig, CTO — the person this role reports
  to), judged sendable as written on 2026-09-29, and it sat unused. `docs/outreach/sent/` is **still empty**.

### The pipeline after Workist

- **No open Tier A role.** Primary lane is now **#9 SAP Fioneer (Tier B)** alone; #11 is closed.
- **Live process: #13 Bubblemaps** — technical interview **2026-10-06**, recruiter lane, Tier C, €70k floor
  exception (labelled). Prep notes added to `docs/opportunities/bubblemaps-sre-data-engineer.md`.
- **§7 rule 3 (zero technical interviews by week 6) is not at risk** — Bubblemaps reaches a technical round in
  week 3. Rule 2 needs four active weeks and classified reasons, so it stays inert.
- **Ten closed rows, ten `unknown`, nine pre-screen** (MarvelX the only one that reached a screening step).

### Friday review (2026-10-09) — items accumulated, one ruling each

1. **Web3 clause conflict, three instances** — #22 1GLOBAL, #25 Blockstream, #26 Anagram admitted by the
   2026-09-29 amendment while §2's reject list still bans crypto-continuity roles. Decide once how Tier C
   Web3 rows are counted.
2. **Outreach lane still 0 sent against a 60% allocation**, and three of this week's losses (#11, #12, #21)
   had no message reach a human. The Workist draft was the most sendable asset in the repo.
3. **The funnel is 10-for-10 `unknown`.** MarvelX's §3 feedback request (`docs/outreach/marvelx-feedback-request.md`)
   is the only live route to a classified rejection — send it.
4. **Customer-facing evidence gap** (open since 2026-09-11) now blocks three lanes: FDE/Solutions, MarvelX and
   Blockstream client delivery.
5. **France-remote band pressure** (#8 Lity, #4 ablefy) and the **seniority/screen-out tax** (#6, #16) remain
   unaddressed targeting questions.

---

## Updated 2026-10-05

**Three more refusals: MarvelX #21, Langdock #12, n8n DevX (#24). All `reason:unknown`, Stage → Closed.**

| Issue | Role | Applied | Refused | Stage reached | Note |
|---|---|---|---|---|---|
| #21 | MarvelX — DevOps (Amsterdam) | 2026-09-29 | 2026-10-05 | **Screening** (questionnaire) | Best evidence match in the pipeline |
| #12 | Langdock — Platform Engineer | 2026-09-26 | 2026-10-05 | Contacted (pre-screen) | **Only Tier A loss**; best-fit JD |
| #24 | n8n — Senior SWE, DevX | ~2026-09-28/30 | 2026-10-05 | Contacted (pre-screen) | **Logged retroactively** — never in the tracker |

**#24 is a process failure, not just a lost application.** The DevX application was never in jobradar and
never became an issue, so it could not be reviewed, counted, or used to catch the double application to the
same n8n team (see below). The row now exists for accounting only.

### ⚠️ Nine closed, nine `unknown`, eight pre-screen

Every closed opportunity is `unknown`. **§7 rules 2 and 4 remain inert**, and §3's one feedback request was
unavailable in eight of nine cases because they never reached a screen.

**Exception, and the only live fix: #21 MarvelX.** It reached **Screening** (questionnaire sent and returned
2026-09-30, refused 2026-10-05), and §3 explicitly permits one feedback request after a screened rejection.
Draft at `docs/outreach/marvelx-feedback-request.md` — **send it.** If MarvelX classifies the cause, it is the
first classified rejection the funnel has ever produced; if they do not, record the silence and stop.

### ⚠️ The outreach lane is still at zero, and it is now visibly the constraint

- **`docs/outreach/sent/` is empty.** Not one outreach message has been sent against a 60% lane allocation.
- **Langdock's draft was never sent** — the role was the pipeline's best fit and its largest single loss. Its
  refusal rests on the LinkedIn ATS application alone. The named-recipient search was never completed.
- Two of the three roles closed today (#12, #21) were applied to cold, with no human of record. Per the
  Cohere lesson already in this file (*"find the human you would follow up with before applying"*), neither
  had a recovery path once the ATS queue moved.
- The ATS lane is now **9 applications, 9 silences**. The only row that produced a human response in the last
  week is **#13 Bubblemaps (`Interview`, `channel:recruiter`)**.

### ⚠️ Third double-application: n8n #23 + #24

Two n8n reqs on the **same Developer Experience team**, near-identical JDs, applied within days, both refused
within three days (2026-10-02 and 2026-10-05). Both were pre-screen and silent, so they are **one** data
point, not two: n8n triages engineering applications fast.

This is the third double-application after Nebius #18/#19 and Cohere #1/#14 — and the first that was **not**
flagged before sending, because the first application was never logged. **Do not apply to a third n8n req.**

### Where the pipeline now stands

- **Primary lane survivors: #11 Workist (Tier A), #9 SAP Fioneer (Tier B).** Both cold ATS, both previously
  flagged as the only rows that can generate signal. #11 has a named recipient (Fabian Brosig, CTO) and a
  sendable draft.
- **Active process: #13 Bubblemaps (`Interview`, recruiter lane) — the only live technical process.**
- **#5 vCluster is still the only logged role never applied to.**
- Everything closed today was lost *before* a human conversation except MarvelX, which was lost *at the first
  written step*.

### Blockstream #25 applied — CH lane, Web3 bridge (2026-10-05)

**DevOps Engineer, Zurich** (Enterprise Products → Service & Enterprise Solutions), applied via cryptojobslist
→ Blockstream's Ashby board (id `4bd6e458-a98f-4f3d-8c0e-a50e4735e32f`). `market:ch` · `tier:c` ·
`channel:ats` · **`track:web3`**. Board Stage `Contacted`; follow-ups 2026-10-12 → 10-14 (1st) and
2026-10-19 → 10-23 (final).

- **Deliberate long-shot, and recorded as one.** Two hard filters **unverified** — compensation (no band
  published; CH floor CHF 110k) and relocation (on-site Zurich/Lugano, no relocation assistance or
  remote-start language) — and one **explicit failure**: no AI-workload surface at all. It is blockchain,
  custody and payments infrastructure for banks.
- **Admitted under the 2026-09-29 amendment** ("Web3 infrastructure is in scope in every lane") as a Tier C
  Web3 bridge. This is the **same §2 clause conflict** already flagged for 1GLOBAL #22: the reject list still
  bans crypto-continuity roles that do not strengthen AI-infra positioning. **Both need one ruling at the
  Friday review** so Tier C Web3 rows are counted consistently.
- **Craft match is unusually direct** for a Swiss-lane role: Kubernetes (incl. on-prem bare metal), Terraform,
  CI/CD, Prometheus/Grafana/ELK, Vault/SOPS secrets, incident response, and **regulated environments**
  (HDS healthcare, ISO 27001, $8B+ crypto assets). **French is a plus** in Lugano/Zurich delivery work.
- **Three real risks:** the posting is **8 months old** (2026-02-10) and still listed; the JD prefers **AWS**
  against a GCP-first CV; and the role is **client-facing delivery**, which the unresolved customer-facing
  evidence gap gates (open since 2026-09-11, now blocking two lanes).

### Anagram #26 applied — EU-remote Web3 bridge (2026-10-05)

**Site Reliability Engineer (Web3 Infrastructure)**, Ashby, location **"Anywhere"** (remote/hybrid/office
flexible). `market:eu-remote` · `tier:c` · `channel:ats` · **`track:web3`**. Board Stage `Contacted`;
follow-ups 2026-10-12 → 10-14 and 2026-10-19 → 10-23.

- **Cheap long-shot.** One hard filter unchecked (compensation — no band published, €80k EU-remote floor) and
  one explicit failure (no AI surface), but **no relocation gate, no seniority stretch, and a direct craft
  match**: Terraform/Kubernetes, observability, CI/CD, key management and network security, plus real
  **blockchain node infrastructure** evidence from Kiln/Cometh.
- **⚠️ Anonymous employer.** Anagram is a **digital-assets holding company** and the posting sits under
  **"Portfolio Company Hiring"**. The actual venture, team, product and contract entity are unknown. That is
  the first thing a screen must resolve, before any prep is worth doing.
- **⚠️ 20 months old** (published 2025-02-04) — almost certainly a standing pipeline rather than an open req.
  Silence would be uninformative.
- **⚠️ Third instance of the same §2 clause conflict** (#22 1GLOBAL, #25 Blockstream, #26 Anagram). Three
  Tier C Web3 rows in one week, each admitted by the 2026-09-29 amendment while the §2 reject list still bans
  crypto-continuity roles. **One ruling at the Friday review, not three separate judgements.**

---

## Updated 2026-10-02

**Three refusals in one turn: Lity #8, Nebius #19, n8n #23 — all pre-screen, all `reason:unknown`.**
Board Stage → Closed on all three; `reason:unknown` labelled; jobradar store marked `rejected` for the two
rows it holds (#23 `13bee0033717209a`, #19 `83286da899f9b790` — Lity was never in the store, applied via
Marvin ATS before adoption). No follow-ups owed, no feedback requests (none reached a screen).

| Issue | Applied | Refused by | Speed | Note |
|---|---|---|---|---|
| #8 Lity | 2026-09-26 | 2026-10-02 | ≤6 cal / ~5 bus days | Already ruled out pre-application on the disclosed 60–80 K€ band |
| #19 Nebius Token Factory | 2026-09-29 | 2026-10-02 | ~3 bus days | **Closed `unassessed`** — stub was never promoted to a doc |
| #23 n8n | 2026-09-30 | 2026-10-02 | ≤2 cal / ~2 bus days | **Fastest refusal in the pipeline**; recruiter/ATS triage, not a judged rejection |

- **#23 n8n was the pipeline's only published-band role** (€91.4K–€171.7K; WE/NE €114.3K–€149.3K + equity)
  and a genuinely AI-native employer. Losing it at triage removes the **compensation anchor for the €85k
  ask** until another published-band role appears. The agent-platform gap it was going to test was never
  tested.
- **#19 closed before anyone read the JD** — first row to do so. Its market/tier labels (`de`/`b`) are
  mechanical jobradar heuristics, not findings; the §2 checklist is deliberately left unfilled.
- **Nebius double-application is now live.** #18 (ML Infra) was applied the same day through the same
  Greenhouse board and is still open. Do **not** read the #19 refusal as a verdict on #18, but treat #18 as
  at elevated risk of the same fast silent triage. Let it reach its own window (2026-10-06 → 10-08) — one
  follow-up only, no chasing.

### ⚠️ Six closed, six `unknown` — §7's diagnostic rules are now fully inert

Every closed row (#3, #6, #8, #16, #19, #23) is `reason:unknown` and pre-screen. This is no longer a
watch-item; it is a standing property of the funnel:

- §7 rules 2 and 4 depend on classified rejection reasons; §3's one feedback request is available **only
  after a recruiter screen**. **No pre-screen refusal can ever be classified.**
- Six applications have produced **zero** diagnostic information. The only rows that can generate signal are
  the ones that reach a human: **#13 Bubblemaps (`Interview`)** and **#21 MarvelX (`Screening`)**.
- **n8n is the counter-example worth reading:** a fast no from a company with a published band is not
  evidence about fit. Response *speed* is triage, not assessment — stop reading fast refusals as verdicts
  on the thesis.

### Targeting signals to carry into the Friday review

1. **Seniority/screen-out tax:** #6 and #16 fired explicit seniority bars visible in the JD before applying.
   #8 and #23 fired filters that were visible (disclosed band) or structural (ATS triage).
2. **France-remote band pressure confirmed as a pattern, not a one-off:** #8 was the second France-remote
   role clearing geography and craft yet under €80k (cf. ablefy #4). The role is now closed on it. Research
   the France-remote band before touching the floor at the next FR-remote target (§7 rule 4 in spirit).
3. **ATS lane yield is 0-for-6 on information.** The lever is `channel:outreach` — still **0 issues sent**,
   against a 60% lane allocation.

---

## Updated 2026-09-30

**MarvelX (#21) → `Screening`.** MarvelX replied to the 2026-09-29 Typeform application with a
**questionnaire**, completed and returned **2026-09-30**. Board Stage moved Contacted → Screening.

- **1 business day** from application to a human response, on a route with no ATS to batch-screen from.
  Fastest response in the pipeline (Doctolib took 2 business days to refuse); the day-1–2 application timing
  produced its first payoff.
- **Screening, not interview.** A written questionnaire costs MarvelX no human hour yet.
- ⚠️ **Questionnaire content not captured.** Questions and answers must go into the opportunity doc. A
  questionnaire normally asks exactly the three open items: relocation support, 8–12 week in-office
  flexibility, and salary expectation (€85,000 would then be on record twice).
- **The relocation gate is unmoved** — no sponsorship, no relocation budget, no remote start in the posting.
  #21 still fails the §2 relocation filter on the letter of the JD, and relocation funding is still the whole
  outcome.
- Follow-ups: **2026-10-07** (1st), **2026-10-16** (final).

Primary-lane order: **#21 MarvelX (Screening) > #12 Langdock > #11 Workist > #9 SAP Fioneer.**

---

**Bubblemaps (#13) → `Interview`.** The CTO call happened **2026-09-30** and the process **advanced to the
technical interview** — the pipeline's first active technical process, and the first payoff from the
`channel:recruiter` lane.

- ⚠️ **CTO call outcome not captured:** the SRE-vs-Data-Engineer split, the round format, whether €70k landed,
  remote policy, and which entity pays. All four change the prep.
- **The floor exception is unchanged.** €70k is still below the €80k floor, still admissible only in late-cliff
  (~Feb 2027) or last-resort (~Apr 2027), and **neither is active**. Advancing does not move the floor; the
  exception stays labelled and unpooled with the primary lane.
- **Prep is time-boxed** until the split and comp are known. Receipts and the honest gap answers are written
  up in `docs/opportunities/bubblemaps-sre-data-engineer.md` → *Technical interview — prep*.
- Rankings unchanged: French, Tier C, €70k → below #21 MarvelX and the AI lane.

---

**1GLOBAL (#22) logged — Senior SRE, Berlin (applied 2026-09-30).** `market:de` · `tier:c` · `channel:ats` ·
`track:bridge`.

- **Deliberate long-shot**, on three counts: the **Tier C gate** (non-AI, non-Web3 bridges are formally
  admissible only from the last-resort window ~Apr 2027, while the 2026-09-29 ML-preference amendment admits
  them case by case — **the clauses conflict; flag at the next Friday review**); the **5+ years (incl. 2+
  dedicated SRE)** ask against ~4 years continuous; and *"proficiency in Python, Go, and Bash"* against
  Evidence Boundaries that exclude production Python/Go claims.
- **Two hard filters unverified:** compensation (undisclosed, Berlin floor €80k) and work mode — the JD says
  only *"we are open to hiring this role in Berlin, Germany"*, with no remote or hybrid statement, so the
  relocation/remote-start filter is unverified.
- It clears everything else that matters: Berlin (destination #2, the preferred first physical move),
  architectural scope (SLIs/SLOs/error budgets, HA/DR validation, chaos, capacity, cost), English JD, no
  staff/8-year bar.
- Follow-ups: **2026-10-07 → 10-09** (1st), **2026-10-14 → 10-20** (final). Ask comp and work mode in the
  first exchange — both are cheap and both are binding.

---

**n8n (#23) logged — Agentic Engineering Platform Engineer, Berlin (applied 2026-09-30).** `market:de` ·
`tier:b` · `channel:ats` · `track:ai` · jobradar uid `13bee0033717209a`.

- **The only application with a published band:** Ashby posts **€91.4K–€171.7K**; Western/Northern Europe tier
  **€114.3K–€149.3K + equity**. Clears the €80k floor with room, so **no floor-exception accounting** — unlike
  #13. It also validates the €85k ask used at MarvelX as mid-band, not aggressive.
- **Tier B caveat, recorded in the doc and the issue:** the role owns the paved road for **autonomous coding
  agents inside n8n's own engineering organisation** — sandboxed execution environments, secrets/permissions
  boundaries, CI/Linear integration, agent-quality benchmarks. That is AI *systems* work but **not** the ML
  serving/pipeline platform: ranked below a true ML-platform role, above any Tier C bridge.
- **Work mode unverified and ranking-relevant:** Ashby marks the posting **remote** with "Berlin Office" as the
  location. Remote-in-EU from France → primary lane, no relocation filter applies. Berlin hybrid → the funding
  rule applies. Confirm first.
- **Honest gap:** the first must-have is production autonomous-agent / agent-orchestration platform ownership;
  Evidence Boundaries allow only application-layer PoC work. Also no TypeScript/Node, no monorepo experience.
  Everything else maps, including a strong safety match (Vault, SOPS, External Secrets, Teleport, Kyverno,
  Cilium isolation).
- The posting asks for a **screenshot of a first n8n workflow** — send it with the first follow-up if it was
  not in the application.
- Follow-ups: **2026-10-07 → 10-09** (1st), **2026-10-14 → 10-20** (final).

**Tooling — two live bugs fixed in the applied-logging path** (`scripts/log_applied.py` and
`.github/ISSUE_TEMPLATE/opportunity.md`):

1. **Template front matter leaked into every auto-created issue body** — the skip only caught the first `---`
   line, so `name: / about: / title: / labels:` YAML sat at the top of the issue (visible on #19 and others).
2. **The market line never substituted** — the script's lookup key expects `Market (CH / DE / NL / EU-remote /
   FR)` while the template still read `Market (CH / DE / EU-remote / FR)`, so every auto-logged issue had a
   blank market field. The template now carries NL.

Issues created before the fix were left as written; **#23 is the first logged with both fixed.** Verification
note: `gh project item-list` did not show the new item (#23) minutes after creation while the item itself
resolved correctly via GraphQL — trust the `node(id)` readback, which `log_applied.py` already uses.

## Updated 2026-09-29

**Doctolib (#6) closed** — rejection, no reason given → `reason:unknown`. Board Stage → Closed.

- **3 calendar days / 2 business days** from application to refusal. Fastest decision in the pipeline
  (vivenu took 14/10). This is a screen-out, not a silence-close.
- **Expected outcome, not a signal.** Both hard-reject filters were explicit in the JD *before* applying:
  Staff title + 8 years demanded against four evidenced, and no ML-platform surface. Logged as a deliberate
  long-shot on 2026-09-26. The refusal is the cost of the long-shot.
- **§7 rules 1–3 NOT triggered.** Rule 1 covers outreach, not ATS, and needs three active weeks; rule 2
  requires a screen (never reached); rule 3 needs week 6. No strategy change warranted.
- Follow-ups: none owed (refusal arrived 9 days before the first window).
- Doctolib SRE/Platform postings: **do not re-apply** for the primary lane — low-yield read now reinforced.
- **Rejection tally: 2 of 2 closed opportunities are `unknown`** (Doctolib + vivenu). Watch this: if every
  rejection is `unknown`, §7's diagnosis rules have nothing to work with and the funnel stays uninterpretable.

Remaining open: **10 issues**. Primary-lane cohort unchanged: #12 Langdock > #11 Workist > #9 SAP Fioneer.

### Bubblemaps (#13) — new, Screening, via recruiter Yofy

- SRE / Data Engineer at **Bubblemaps** (bubblemaps.io), **French** Web3 company — onchain forensics/analytics
- Recruiter call completed 2026-09-29. Quoted **€60–80k**; asked **€70,000 minimum**. **Awaiting CTO decision**
- **Tier C** — no ML-platform surface, and §2's crypto-continuity rejection fires (Kiln is already crypto)
- ⚠️ **FLOOR EXCEPTION.** €70k is below the €80k floor. Late-cliff (~Feb 2027) and last-resort (~Apr 2027)
  modes are **not active**, so this runs outside the plan on compensation. Recorded as a **conscious labelled
  exception**: income continuity, live recruiter, low investment. **Do not pool with the primary lane, and do
  not let the floor read as having moved.**
- Does not count toward ML-platform conversion
- Follow-up: ping Yofy **2026-10-06** if no CTO answer

**First real recruiter channel activity** — this is the `channel:recruiter` lane becoming live for the first
time (previously 0 conversations against a 1–2/week target).

### Peak3 (#20) and MarvelX (#21) — one strong apply, one structural risk

Both applied 2026-09-29. Both are **Tier A/B** with real AI-platform surfaces, which makes them the
strongest additions to the primary lane alongside #12 Langdock, #11 Workist, #9 SAP Fioneer.

| Issue | Role | Market | Notes |
|---|---|---|---|
| #20 | Peak3 — AI Platform Engineer | Madrid `[INFERENCE]` | **Recruiter contactable: Zoey Zhang (HR)** via direct-message link on the posting. Second actionable outreach target after Workist |
| #21 | MarvelX — DevOps Engineer | **NL (Amsterdam)** | Best evidence match in the pipeline. **Relocation is the whole risk** |

**#20 Peak3 — the surface matches the entry wedge exactly:** *"build and operate the infrastructure that keeps
our agentic AI systems fast, reliable, and cost-effective in production... vector databases, model gateways,
and inference pipelines."* Strong overlap on production ownership, on-call, incident response, observability,
cost. **Two open risks:** (a) **Madrid comp `[INFERENCE]` €45–65k, which would breach the €80k floor** — no
exception recorded because the breach is unconfirmed; do not state a number until the band is known; Spain
pays 14 months, so clarify the basis. (b) 200+ applicants on a month-old posting — oversubscribed and stale.

**#21 MarvelX — cleanest evidence match logged.** Every "looking for" bullet met or met-adjacent: Kubernetes
production ownership, Terraform, observability named individually (Prometheus, Grafana, ELK, OpenTelemetry),
multi-cloud, Linux/**scripting** (not production software), and **ISO 27001 exposure — Vincent led an ISO 27001
implementation at Cometh.** GPU is explicitly nice-to-have. Applied day 1–2 of a freshly posted role.

**⚠️ #21 fails the relocation hard filter on the letter of the posting:** Amsterdam, **3 days/week in office**,
*"work eligibility in the Netherlands required; we are not able to sponsor visas."* EU citizenship covers the
right to work, but the physical move must precede the start date, and the JD offers **no relocation support and
no remote-start ramp** — against `CONTEXT.md`'s rule that relocation happens only when funded. **Relocation
support was named directly in the salary answer** rather than deferred. This is the one thing to resolve at
screen.

**New market: `market:nl` created.** No Netherlands floor exists in `CONTEXT.md`; €80k applied **by analogy**
(Amsterdam is comparable-tier, unlike Madrid). Salary stated **€85,000** for #21, consistent with #20.

### Synthesia (#16) closed — `reason:unknown`, same-day screen-out

Applied and refused **the same day** (2026-09-29). No reason given → `unknown`.

**Predicted before applying, so not new information:** the note flagged this as a deliberate long-shot with
**two hard filters firing explicitly in the JD** — `(Senior or Staff)` asking **7+ years as a software
engineer** against ~4 evidenced, and a **Python implementation stage** against an evidence boundary that
excludes production Python claims. Comp (€130k base + RSUs) and remote-from-France both passed.

**§7 rules 1–3 not triggered** (no screen; week 2; ATS not outreach). No strategy change.

### ⚠️ Three closed, three `unknown` — the funnel is now uninformative

**#3 vivenu, #6 Doctolib, #16 Synthesia: all closed `reason:unknown`, all pre-screen.** This is a
measurement problem, not just bad luck:

- §7 rules 2 and 4 (screen-to-rejection, compensation mismatch) depend on **classified** rejection reasons
- §3's one feedback request is available **only after a recruiter screen**
- Therefore **no pre-screen refusal can ever be classified.** Every closed row teaches nothing

Two implications for the Friday review:

1. **Pre-screen volume generates no learning.** Volume only pays if some applications reach screens. Signal
   can only come from the primary-lane roles: **#12 Langdock, #11 Workist, #9 SAP Fioneer**.
2. **Deliberate long-shots are now a measurable tax.** Doctolib and Synthesia both failed on seniority bars
   visible in the JD *before* applying; neither produced information. **Consider tightening the seniority
   filter rather than spending applications on roles that state `Staff` / `8+ years` outright.**

**Also flagged:** two of the three closed rows (#6, #16) failed the seniority filter explicitly. If a fourth
appears, that is a targeting pattern, not a per-role result — and per §7 rule 2 the response is to narrow
the role band.

### Issues #15–19 logged in other sessions (first seen 2026-09-29)

Not created this session; discovered when the board read refreshed. #15 Dialectic (CH, Prospecting),
#17 ClickHouse (EU-remote, Contacted), #18 Nebius ML Infrastructure (EU-remote, Contacted),
#19 Nebius Token Factory SRE (DE, Contacted). **#18 and #19 are both Nebius** — check for the same
double-application risk flagged on Cohere (#1/#14).

### Cohere (#14) — second Cohere requisition, applied 2026-09-29

- **FDE, Infrastructure Specialist (Europe)** — `69a9ab2e…`, vs the open **#1** which is France-scoped
  (`24cdb030…`). **Distinct requisitions, same team.**
- **Tier B-secondary** (forward-deployed infrastructure, the capped option). Remote-friendly, Paris/Berlin
  offices, travel 20–40%. GPU orchestration is an explicit *bonus*, not day-one.
- ⚠️ **Same team twice in 18 days while #1 is unresolved and its follow-ups were never sent.** Cohere may
  read this as duplicate contact.
  - **DO NOT run parallel follow-up sequences.** Consolidate into one, or let the overdue #1 final follow-up
    cover both requisitions
  - If a recruiter replies on either, **disclose the other application immediately**
- **Customer-facing evidence gap stays open** — `docs/resume-edits.md` carries it unanswered since
  2026-09-11, and it gates this B-secondary tier (≤ ~¼ of EU-remote/FR effort). Now the single most valuable
  unblock, because two live Cohere applications depend on it.
- ⛔ **Follow-up BLOCKED 2026-09-29 — no reachable Cohere human.** No recruiter InMail, no ATS confirmation
  reply address, no named contact. The consolidated draft (covering both requisitions) is held at
  `docs/outreach/cohere-follow-up-two-requisitions.md` and is not actionable.
  - **Unblock:** a named contact appears via an ATS reply, recruiter InMail, or an inbound reply on either requisition
  - **Do NOT apply a third time to Cohere to create a contact** — worse than silence
  - Both rows stay silent ATS applications at Stage `Contacted`, no outreach owed
  - **Generalisable lesson: find the human you would follow up with *before* applying.** An application with no
    contact route is a one-shot with no recovery path — that is the 25% ATS lane, not the 60% outreach lane.

## Updated 2026-09-26

Three applications logged from the 09-26 session (details in `docs/opportunities/`, board Stage `Contacted`):

| Issue | Role | Verdict |
|---|---|---|
| #6 | Doctolib — Staff SRE (DE) | **Deliberate long-shot.** Staff title + 8+ yrs = hard-reject; no ML surface. Doctolib SRE postings are low-yield for the primary lane |
| #7 | Sinch / Mailjet — SRE (FR, full remote) | **Strongest bridge candidate.** Mid-Senior band, residency already satisfied, craft match is direct. Tier C pending the AI-stack screen question |
| #8 | Lity — DataOps/Infra (FR, full remote) | **Disclosed floor breach** (60–80 K€ + BSPCE). No screen warranted |
| #9 | SAP Fioneer — AI Platform Engineer (DE) | **Primary-lane (Tier A/B).** Real generative-AI platform surface. Salary stated **€90k** |
| #10 | Otera — Platform Engineer (EU-remote) | **Tier C.** AI is the product, not the platform surface. Best remote fit so far; France eligibility unconfirmed |
| #11 | Workist — Senior Platform Engineer (DE) | **Tier A.** Disclosed **€80–100k** band, clears the floor |
| #12 | Langdock — (Senior) Platform Engineer (DE) | **Tier A — HIGHEST PRIORITY.** Disclosed **€90–140k + equity**, 3–6 yr band, JD describes the target role. **Risk: in-office in Berlin, no remote start** |

Follow-ups owed: **#7 Sinch**, **#9 SAP Fioneer**, **#10 Otera**, **#11 Workist**, **#12 Langdock** — all
2026-10-05 (1st) and 2026-10-14 (final). None for #6 or #8.

**Primary-lane cohort (counts toward ML-platform conversion):** #9 SAP Fioneer, #11 Workist, #12 Langdock.
**Priority order on any response: #12 Langdock > #11 Workist > #9 SAP Fioneer** — Langdock has the best band,
the closest seniority match (4 vs 3–6 yrs), and a JD that names inference-boundary and agent-runtime
ownership outright.

**Langdock open item:** the two free-text answers were submitted before the grilling session completed
(Q2 "proudest work" was never resolved; Q1 depended on it). **Recover the submitted text** from the LinkedIn
confirmation email and store it in the opportunity note so interview claims stay consistent.

**Outreach lane (`channel:outreach`) — still 0 issues.** Four drafts exist in `docs/outreach/`; none sent.
Cohere is **blocked** (no reachable human). The three live candidates all have a resolvable target, though
Langdock and SAP Fioneer still need a **named recipient** found on LinkedIn before sending.

**Everything else logged today is Tier C bridge** — excluded from primary-lane conversion rates.

**Salary consistency:** €90,000 stated for #9, #10, and vivenu (#3). Hold this number at the same tier so
the cohort stays interpretable.

**Watch:** two France-remote roles this session cleared geography and craft but landed under the €80k floor
(Lity; ablefy's German-only residency question still open). If a third appears, research the France-remote
band before touching the floor (§7 rule 4 in spirit).

## Updated 2026-09-25

- **vivenu (#3) closed** — refusal, no reason given. Closed as `reason:unknown`; board Stage → Closed.
  Recorded in `docs/opportunities/vivenu-senior-platform-engineer.md`.
- **Follow-up 1 (#1, #3, #4) was missed** during the pause and was not retroactively sent. Owed now:
  **#1 Cohere** and **#4 ablefy**, both past the final window (10–14 business days from 2026-09-11) —
  send `Follow-up 2` as the last contact. #3 vivenu owes nothing.
- Does **not** trigger §7 rules 1–3: the rejection is `unknown`, so it is not chargeable to targeting,
  messaging, or readiness.

## Next actions

1. **Send the two remaining final follow-ups** — issues #1 and #4 (see above).
2. **Publish the evidence repo** — `gh repo create alchimestre/ml-platform-on-k8s --public --source . --push`
   from `~/projects/ml-platform-on-k8s`, then link it from CV header and LinkedIn Featured.
   Week 2 expects "first meaningful commit public and linked from the assets".
3. **Start Week 2 build** — `brew install helm` (still missing), then MLflow registry + FastAPI serving
   per `~/projects/ml-platform-on-k8s/ROADMAP.md`.

## Open inputs carried into the pause

- **Customer-facing evidence** — asked 2026-09-11, still unanswered. Now gates the Solutions Engineer /
  FDE option (`CONTEXT.md`) as well as the capped FDE lane. Highest-value thing to unblock at leisure.
- **France Travail obligations** — confirm actualité/convocations/offer-acceptance rules so the
  2027-07-15 cliff cannot move. `[INFERENCE]` on the general rules.
- **Independent Work date range** on the CV — `2026 – present` assumes a Jan-2026 start.
- **vCluster #5 not yet applied** — it is the Australia-remote example and clears the €80k floor;
  check the GPU-depth hard filter (currently marked FAILS) before applying. It is now the only
  open pipeline row with no contact made.

## What did not change

Lane split (EU-remote/FR 50 · Berlin 35 · CH 15), compensation floors, the income cliff deadlines
(employment start ≤ 2027-06-01 target / 2027-06-15 absolute), and every hard filter in §2 of
`docs/12-week-strategy.md`. The pause costs 10 days of pipeline time, not a change of strategy.
