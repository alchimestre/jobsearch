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
| Pipeline | **22 issues: 18 open, 4 closed.** Open: #1 Cohere (FR), #4 ablefy, #5 vCluster, #7 Sinch, #8 Lity, #9 SAP Fioneer, #10 Otera, #11 Workist, #12 Langdock, #13 Bubblemaps (`Interview`), #14 Cohere (EU), #15 Dialectic, #17 ClickHouse, #18 Nebius ML Infra, #19 Nebius Token Factory, #20 Peak3, #21 MarvelX (NL, `Screening`), #22 1GLOBAL (DE). Closed: #3 vivenu, #6 Doctolib, #16 Synthesia (all `reason:unknown`) |

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
