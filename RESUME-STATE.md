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
| Pipeline | 9 open issues: #1 Cohere, #4 ablefy, #5 vCluster, #7 Sinch, #8 Lity, #9 SAP Fioneer, #10 Otera, #11 Workist, #12 Langdock. Closed: #3 vivenu (2026-09-25, `reason:unknown`), **#6 Doctolib (2026-09-29, `reason:unknown` — 2-day screen-out)**. #2 is the duplicate vivenu row |

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

Remaining open: **9 issues**. Primary-lane cohort unchanged: #12 Langdock > #11 Workist > #9 SAP Fioneer.

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
