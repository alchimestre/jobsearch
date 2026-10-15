# Agent instructions — jobsearch

## Writing style (binding)

Any text written in **Vincent's applicant voice** — application answers, recruiter messages, cover
letters, LinkedIn copy, CV bullets — MUST follow `docs/writing-style.md`.

**Agent replies in this repo MUST use the `plain-english` skill** (ASD-STE100 Simplified Technical English):
short sentences, one idea per sentence, active voice, common words, acronym defined on first use, exact
numbers, no jargon. Lead with the answer, then the evidence, then the steps. This rule is set by Vincent on
2026-10-09 and applies to every chat reply, status report and explanation in this repo, not only to
applicant-voice text.

Non-negotiable for application answers: ≤ 100 words each, one paragraph, flat lists, no rhetorical
contrasts, no em-dashes, no narrative openings, every figure verifiable or bracketed as `⟨placeholder⟩`.
If a draft is over budget, cut whole sentences — do not compress words.

Do not paste a long version "for context" and a short version "for use". Deliver the short one.

Internal notes and strategy docs are a separate register and may be explanatory.

**Free-text application fields** (cover letters, "why you" boxes, motivation questions) are read by a
human who already has the CV. Write them as prose: outcomes, ownership, the one or two things only
Vincent can say. Never enumerate tools — `docs/writing-style.md` has the before/after table.

## Personas (binding)

Load the matching persona with `skill://<name>` before the task. They live in `~/.omp/agent/skills/`.

**Search side**

| Task | Persona |
|---|---|
| CV edit, ATS keyword pass, gap framing | `agency-resume-tailor` |
| The recruiter's read of the CV and the screen | `agency-recruitment-specialist` |
| Outreach message, sequencing, the ask | `agency-sales-outreach` |
| Funnel conversion, cohort arithmetic (§6, §7) | `agency-pipeline-analyst` |

**Interview side**

| Task | Persona |
|---|---|
| SRE round | `agency-sre-site-reliability-engineer` |
| Platform round | `agency-platform-engineer` |
| Incident stories (`docs/interview-incident-stories.md`) | `agency-incident-responder` |
| Cost, capacity, unit economics | `agency-finops-engineer` |
| LLM serving, pipelines, model operations | `agency-llm-post-training-engineer`, `agency-rag-pipeline-engineer` |

**Destination side**

| Task | Persona |
|---|---|
| French contract norms, ESN names, local bands | `agency-french-consulting-market-navigator` |
| Outcome negotiation, offer terms | `agency-deal-strategist` |

No persona covers the candidate-side application funnel — boards, ATS rejection rates and lane arithmetic
stay this repo's own (`docs/channel-playbook.md`, plan §6 and §7).

## Repo conventions

- Read `CONTEXT.md` first (canonical terms, evidence boundaries, compensation floors).
- **No timeline on Vincent's own work (2026-10-15).** Self-study and the evidence project carry **no dates, no
  milestones, no slip rules** — he drives them at his own pace. Never add week numbers, deadlines, milestone
  rows, or "by week N" gates to plans, docs, issue bodies, or comments. Search-side cadence (weekly review,
  active-week thresholds) is unaffected. Evidence order: `docs/search-plan.md` §5.
- **Issues and tickets stay terse.** Obey the `ticket-brevity` rule: title verb-first ≤ 8 words, body ≤ 60 words,
  acceptance criteria ≤ 5, resolution comment ≤ 150 words. No context, background, or summary sections.
- One GitHub issue per live opportunity, moved across the `AI Infra Job Search Pipeline` project board.
- Market/tier/channel labels are defined in `README.md`.

## Sourcing roles

`docs/channel-playbook.md` is the source stack. `tools/jobradar` is the polling tool, part of this repo:
167 employer ATS boards across 12 platforms plus 20 multi-employer feeds — 174 sources polled, the rest
muted. One ranked SQLite/TUI queue.

- Discovery runs through it: `cd tools/jobradar && uv run jobradar scan`, then `jobradar tui`, or
  `jobradar list --decision high`. It auto-adopts any ATS board it sees in a feed's job URL.
- There is **one** checkout of the tool: `tools/jobradar`, in this repo. `~/projects/jobradar` is a symlink
  to it (2026-09-30) — same code, same `.jobradar/state.db`. Do not copy or clone it elsewhere; a second
  copy silently means a second store and "my changes didn't apply". It was a separate repository until
  2026-10-15, when it was merged in with its history intact.
- **Scope (2026-09-29): Web3 infrastructure is in scope in every lane; ML/LLM is preferred but
  non-blocking; the return to work targets the earliest achievable start.** Tag each application with a
  `track:` label — `track:ai`, `track:web3`, `track:bridge` — so conversion stays comparable across the
  widened scope. `scripts/log_applied.py` assigns it from the jobradar signals.
- **Priority (2026-10-09): France first, Web3 close behind.** Allocation is **France-anchored 70% · Web3
  infrastructure 20% · Berlin 10%**; Switzerland is opportunistic only. Vincent needs income fast and needs to
  stay in France, so a French contract beats a better-titled role that needs a move. See `CONTEXT.md` →
  Search Lanes.
- **Hard filter — JD language (2026-10-09).** The job description **MUST** be written in **English or French**.
  Read the JD and confirm this before logging an application; a posting in German, or any other language, is
  out of scope even when the title and stack look perfect (Vesterling, 2026-10-09). This is a hard filter, not
  a preference. Enforced in the tool as `allowed_languages: [en, fr]`.
- **Hard filter — location (2026-10-09).** The role **MUST** be one of: based in France; remote and able to
  employ in France; or on-site with **funded** relocation or a remote start from France. A posting that assumes
  residence in another country without relocation support fails, and is logged as a deliberate long-shot at
  most — do not count it as a real application. Ask the location question **in writing before applying** where
  the posting does not answer it.
- **Hard filter — role type (2026-10-09): no software-engineering roles.** Vincent is not a developer. Work
  that is writing application, backend or product code — Software Engineer, Backend/Fullstack/Frontend
  Engineer, SDE — is out even at a strong employer, however good the salary is (Alan `Fullstack Software
  Engineer`, 2026-10-09). The target stays platform, SRE, infrastructure, reliability, and Web3
  infrastructure work. Enforced in the tool as a `-6 software-role` negative rule.
- `jobradar export --since 7d` emits ready-to-paste rows carrying the stable `uid`; quote that uid in the
  opportunity doc so the store and the issue stay reconcilable.
- Marking a posting `applied` in the TUI (`a`) runs `scripts/log_applied.py`, which logs the application
  end-to-end — doc, issue, labels, Stage `Contacted` — with no agent involved, and is idempotent (it
  matches an existing issue by jobradar uid, then posting URL, then company + role). Its market and tier
  are mechanical defaults flagged for review in the issue body; check them when you next touch the issue.
- Lane allocation is 60% outreach / 25% ATS / 10% recruiter / 5% evidence. **`channel:outreach` is the lane
  to watch.** Log every hiring-manager contact as an issue — Stage `Prospecting` if the role is unposted,
  `Contacted` once sent.
- Agency recruiters, mass job-board applications, and job-alert scraping stay out (ruled out in wayfinder
  ticket 08).

## Default: log every application

When Vincent reports applying to a role — a posting URL, a link, or "I applied to X" — **do it without
being asked**:

1. Read the posting and assess it against the §2 hard-filter checklist.
2. Write `docs/opportunities/<company>-<role-slug>.md` (model: `docs/opportunities/vivenu-senior-platform-engineer.md`).
3. Create the issue from the `opportunity` template, title `[MARKET] Company — Role`.
4. Label `market:*` · `tier:*` · `channel:*`.
5. Add it to the `AI Infra Job Search Pipeline` board with **Stage = Contacted**.
6. Set follow-up dates from the application date: **+5–7 business days** (1st), **+10–14** (final).

Board IDs (project `PVT_kwHOAGop3M4Bi8S3`, owner `alchimestre`, number `1`):

- Stage field `PVTSSF_lAHOAGop3M4Bi8S3zhhygD8` — Prospecting `df1e7ce3` · Contacted `832d8f86` ·
  Screening `d7467944` · Interview `43babd55` · Offer `e9e238dc` · Closed `361c9503`

```bash
gh issue create --title "[DE] Company — Role" --body-file /tmp/note.md \
  --label market:de --label tier:c --label channel:ats
ITEM=$(gh project item-add 1 --owner alchimestre --url <issue-url> --format json --jq .id)
gh project item-edit --id "$ITEM" --project-id PVT_kwHOAGop3M4Bi8S3 \
  --field-id PVTSSF_lAHOAGop3M4Bi8S3zhhygD8 --single-select-option-id 832d8f86
```

Report the hard-filter verdict in chat too — including when it fails. A role that fails a hard filter still
gets an issue, recorded as a **deliberate long-shot**, so the funnel data stays interpretable.
