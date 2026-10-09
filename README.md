# jobsearch

Private repo for Vincent Loupmon's 12-week AI Infrastructure job search and training strategy (approved 2026-09-09). Live tracking uses GitHub Issues + Projects; the decision history is committed markdown.

## Layout

| Path | Contents |
|---|---|
| `docs/12-week-strategy.md` | **Approved operating plan** (amended 2026-09-11: income cliff, lane allocation, conditional Go, late-cliff/last-resort modes — see §10). Weekly allocations, milestones, funnel signals, adaptation thresholds. Read this first. |
| `docs/channel-playbook.md` | How the pipeline gets fed: source stack, ATS watchlist, LinkedIn filtering (§4), weekly cadence. |
| `docs/linkedin-saved-searches.md` | Operational checklist for the LinkedIn alerts: paste-ready queries, location filters, seniority exclusions, verification list. |
| `docs/outreach/` | Draft outreach messages for hiring managers, stashed for review before sending. |
| `docs/evidence-package.md` | CV restructure outline, LinkedIn narrative, GPU-operator README outline, outreach templates. |
| `docs/resume-edits.md` | Running CV/profile fix list, incl. confirmed Helm usage and the open customer-facing evidence input. |
| `research/` | Market and hiring-evidence research (Zurich/Berlin employers; 28-JD benchmark). |
| `.scratch/ai-infrastructure-job-search/` | Wayfinder decision log — `map.md` (status: complete) and decision tickets 01–10. History, not live tracking. |
| `docs/channel-playbook.md` | How the pipeline gets fed: source stack (ATS + machine-readable feeds), LinkedIn saved-search config, weekly discovery cadence. **Read before sourcing roles.** |
| `tools/jobradar` | Submodule → `alchimestre/jobradar` (private). Aggregates ~110 employer ATS boards + 7 feeds into one ranked SQLite/TUI queue. `jobradar export` feeds this repo's tracker. |
| `CONTEXT.md` | Canonical terms: positioning thesis, differentiators, evidence boundaries, compensation floors. |
| `.github/ISSUE_TEMPLATE/` | Templates: `opportunity` (per-role), `weekly-review`. |

## Live pipeline (GitHub Issues + Projects)

One issue per live opportunity; move it through the board as it progresses.

- **Board:** [AI Infra Job Search Pipeline](https://github.com/users/alchimestre/projects/1) — Stage columns: `Prospecting → Contacted → Screening → Interview → Offer → Closed`.
- **Create:** Issues → New → template **Pipeline opportunity**. One issue per role or outreach contact.
- **Stage:** set via the board's Stage field (one manual UI click needed once: group the board by **Stage**).
- **Weekly review:** Issues → New → template **Weekly review**, assigned to the matching **Week N** milestone. Milestones W1–W12 exist with due dates (start 2026-09-14).

### Labels

| Prefix | Values |
|---|---|
| `market:` | `ch` · `de` · `nl` · `eu-remote` · `fr-bridge` |
| `tier:` | `a` (owns AI infra) · `b` (SRE at AI-native) · `c` (bridge) |
| `channel:` | `outreach` · `ats` · `recruiter` |
| `track:` | `ai` (ML/LLM platform, preferred) · `web3` (blockchain infrastructure, admitted, fastest to income) · `bridge` (non-AI platform role) |
| `reason:` | `relevance` · `readiness` · `compensation` · `location` · `unknown` (apply on rejection) |

`reason:*` labels feed the adaptation thresholds: filter `label:reason:compensation` etc. to tally mismatches per market.

### Suggested queries

- Due follow-ups: filter `label:channel:` + your tracker date in the issue body; the board keeps the stage.
- Rejection mix: `is:closed label:reason:*` grouped by label.
- Market split: `label:market:ch` vs `label:market:de` vs `label:market:nl` vs `label:market:eu-remote` vs `label:market:fr-bridge` (lane allocation **from 2026-10-09: France-anchored 70% · Web3 infrastructure 20% · Berlin 10%** — Switzerland is opportunistic only; NL has no allocation. Response/screen rates kept per lane in weekly reviews).

## Agent workflow conventions

- **Every application Vincent reports is logged by default** — repo note + issue (`Contacted` on the board),
  no need to ask. Procedure, template, and board IDs are in `AGENTS.md` → "Default: log every application".
- The harness reads GitHub issues natively as `issue://<owner>/<repo>/<N>`.
- Agents update issues via the `gh` CLI (`gh issue edit N --label ...`, `gh issue close N`).
- Board stage moves: `gh project item-edit` / `gh api graphql` `updateProjectV2ItemFieldValue`.
- Before a screen, ask the five recruiter-screen questions in the opportunity template and record answers in the issue.

## Execution starts

Week 1 tasks and allocations are in `docs/12-week-strategy.md` §5; the income-cliff deadlines and mode timeline are in §10. Begin with: apply CV restructure + LinkedIn narrative (from `docs/evidence-package.md`, fix list in `docs/resume-edits.md`), create the pipeline tracker issues, scaffold `ml-platform-on-k8s` (spec: `docs/ml-platform-project.md`).
