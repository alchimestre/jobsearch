# jobsearch

Private repo for Vincent Loupmon's 12-week AI Infrastructure job search and training strategy (approved 2026-09-09). Live tracking uses GitHub Issues + Projects; the decision history is committed markdown.

## Layout

| Path | Contents |
|---|---|
| `docs/12-week-strategy.md` | **Approved operating plan.** Weekly allocations, milestones, funnel signals, adaptation thresholds. Read this first. |
| `docs/evidence-package.md` | CV restructure outline, LinkedIn narrative, GPU-operator README outline, outreach templates. |
| `research/` | Market and hiring-evidence research (Zurich/Berlin employers; 28-JD benchmark). |
| `.scratch/ai-infrastructure-job-search/` | Wayfinder decision log — `map.md` (status: complete) and decision tickets 01–10. History, not live tracking. |
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
| `market:` | `ch` · `de` · `eu-remote` · `fr-bridge` |
| `tier:` | `a` (owns AI infra) · `b` (SRE at AI-native) · `c` (bridge) |
| `channel:` | `outreach` · `ats` · `recruiter` |
| `reason:` | `relevance` · `readiness` · `compensation` · `location` · `unknown` (apply on rejection) |

`reason:*` labels feed the adaptation thresholds: filter `label:reason:compensation` etc. to tally mismatches per market.

### Suggested queries

- Due follow-ups: filter `label:channel:` + your tracker date in the issue body; the board keeps the stage.
- Rejection mix: `is:closed label:reason:*` grouped by label.
- Market split: `label:market:ch` vs `label:market:de` (response/screen rates kept in weekly reviews).

## Agent workflow conventions

- The harness reads GitHub issues natively as `issue://<owner>/<repo>/<N>`.
- Agents update issues via the `gh` CLI (`gh issue edit N --label ...`, `gh issue close N`).
- Board stage moves: `gh project item-edit` / `gh api graphql` `updateProjectV2ItemFieldValue`.
- Before a screen, ask the five recruiter-screen questions in the opportunity template and record answers in the issue.

## Execution starts

Week 1 tasks and allocations are in `docs/12-week-strategy.md` §5. Begin with: apply CV restructure + LinkedIn narrative (from `docs/evidence-package.md`), create the pipeline tracker issues, scaffold `gpu-fleet-operator`.
