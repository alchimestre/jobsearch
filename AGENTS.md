# Agent instructions — jobsearch

## Writing style (binding)

Any text written in **Vincent's applicant voice** — application answers, recruiter messages, cover
letters, LinkedIn copy, CV bullets — MUST follow `docs/writing-style.md`.

Non-negotiable for application answers: ≤ 100 words each, one paragraph, flat lists, no rhetorical
contrasts, no em-dashes, no narrative openings, every figure verifiable or bracketed as `⟨placeholder⟩`.
If a draft is over budget, cut whole sentences — do not compress words.

Do not paste a long version "for context" and a short version "for use". Deliver the short one.

Internal notes and strategy docs are a separate register and may be explanatory.

**Free-text application fields** (cover letters, "why you" boxes, motivation questions) are read by a
human who already has the CV. Write them as prose: outcomes, ownership, the one or two things only
Vincent can say. Never enumerate tools — `docs/writing-style.md` has the before/after table.

## Repo conventions

- Read `CONTEXT.md` first (canonical terms, evidence boundaries, compensation floors).
- One GitHub issue per live opportunity, moved across the `AI Infra Job Search Pipeline` project board.
- Market/tier/channel labels are defined in `README.md`.

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
