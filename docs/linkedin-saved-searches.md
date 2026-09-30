# LinkedIn saved-search configuration

**Purpose:** the exact, paste-ready configuration for Vincent's LinkedIn job alerts. Implements
`docs/channel-playbook.md` §4.1, with one correction (see §2) driven by the 2026-09-29 rejection data.

**Status:** companion to `docs/channel-playbook.md`. That document explains *why* LinkedIn is a backstop
rather than a source; this one is the operational checklist to click through.

---

## 1. Why this rewrite exists

`docs/channel-playbook.md` §1 diagnosed the feeding problem correctly:

> The tracker on 2026-09-29 held 13 issues: **12 `channel:ats`, 1 `channel:recruiter`, 0 `channel:outreach`**.
> Both live feeds — LinkedIn job notifications and APEC inbound — are *push* channels, so they can only ever
> fill the 25% lane. That is why the pipeline looked busy and produced tier-C bridge roles.

Two named failure modes drove this: **inbound-only intake** and **title alerts too broad**. This document
fixes the second.

**Scope honesty:** filter tuning does not fix the first. A perfectly-tuned alert still only feeds the 25%
ATS lane. The 60% outreach lane is where conversion comes from, and it is still at zero. Do this rewrite,
then stop tuning and go write to people.

---

## 2. Correction to the playbook query

`docs/channel-playbook.md` §4.1's exclusion clause is:

```
NOT (intern OR Werkstudent OR "working student" OR Recruiter OR Sales OR "Head of" OR Director)
```

**It is missing seniority exclusions, and the funnel data now shows that is a defect.** Two of the three
closed opportunities were rejected on a seniority bar that was stated in the JD *before* applying:

| Issue | Role | Seniority bar in the JD | Outcome |
|---|---|---|---|
| #6 | Doctolib — Staff SRE | "Staff" title + **8+ years** | Closed `reason:unknown`, 2 business days |
| #16 | Synthesia — Backend Engineer, AI tooling | "(Senior **or Staff**)", **7+ years** SWE | Closed `reason:unknown`, **same day** |

Both were logged as deliberate long-shots and both produced **zero information** — pre-screen refusals
cannot be classified, so neither taught the funnel anything. That is a measurable tax, and §7 rule 2's
response (narrow the role band) applies.

**Therefore add to every exclusion clause:**

```
OR Staff OR Principal OR Lead OR "8+ years" OR "10+ years"
```

`Lead` is included deliberately: it is the most common synonym for the bar Vincent fails. Do not exclude
`Senior` — the senior band is the target.

---

## 3. The saved searches

Create these in LinkedIn → Jobs → search → toggle **Set alert**, with **frequency = Daily**. Location must be
set on every alert; a keyword-only alert is what produced the tier-C pile.

### 3.1 Primary — EU-remote / France-compatible

**Keywords:**

```
("ML Platform Engineer" OR "MLOps Engineer" OR "Machine Learning Platform Engineer"
 OR "ML Infrastructure Engineer" OR "AI Platform Engineer" OR "AI Infrastructure Engineer"
 OR "Inference Platform Engineer" OR "Training Platform Engineer" OR "SRE ML Platform")
NOT (intern OR Werkstudent OR "working student" OR Recruiter OR Sales OR "Head of" OR Director
 OR Staff OR Principal OR Lead OR "8+ years" OR "10+ years")
```

**Filters:** Workplace type = **Remote** · Geography = **European Union** + **France**

### 3.2 Berlin

Same keywords. **Filters:** Geography = **Germany**, then narrow to **Berlin** metro.

Add to the keyword block: `AND (Kubernetes OR "platform")`

Signals to watch in the results: ML/LLM/AI-platform wording, Kubernetes ownership, platform or
infrastructure team, B2B AI product. **Bare `SRE` or `DevOps` in the title with no AI/ML wording is the
tier-C signal** — that is precisely what produced Sinch (#7), Doctolib (#6) and ablefy (#4).

### 3.3 Switzerland (relationships + selective applications, 15% lane)

Same keywords. **Filters:** Geography = **Switzerland** (Zurich, Basel, Lausanne, Bern, Zug).

### 3.4 Secondary — forward-deployed infrastructure (cap ≤¼ of EU-remote)

```
("Forward Deployed Engineer" OR "Solutions Engineer" OR "Deployment Engineer"
 OR "Deployment Infrastructure")
AND (Kubernetes OR "on-prem")
NOT (intern OR Recruiter OR Sales OR "Account Executive" OR "pre-sales" OR "quota"
 OR Staff OR Principal OR Director)
```

**Filters:** Remote + EU.

**Read the JD, not the title.** Per `CONTEXT.md`, admit only where engineering and product dogfooding stay
the foundation — planning, Kubernetes/Helm, private/on-prem deployment, troubleshooting. Quota-first account
sales and support-ticket work are out.

### 3.5 Web3 infrastructure (in scope in every lane, added 2026-09-29)

```
("Blockchain Infrastructure Engineer" OR "Protocol Engineer" OR "Node Operations"
 OR "Staking Infrastructure" OR "Platform Engineer Web3" OR "SRE Blockchain"
 OR "DevOps Blockchain")
NOT (sales OR marketing OR community OR partnerships OR Recruiter OR Staff OR Principal)
```

**Filters:** Remote + EU.

**This is a backstop, not the source.** Per §4.1, Web3 roles surface on the 46 verified employer boards and
the aggregators *before* LinkedIn. Tag these `track:web3` when logging.

---

## 4. Verify the operator syntax once — **RESOLVED 2026-09-29: operators do not work as assumed**

`docs/channel-playbook.md` §4.1 marked LinkedIn's `AND`/`OR`/`NOT`/parentheses support as **[INFERENCE]** and
flagged it for a one-time check. **The check was run and it failed.**

**Evidence (Vincent, 2026-09-29):**
- The unified grouped primary query returns **fewer** results locally than the single phrase `ML Platform Engineer`
- A superset query (9 titles OR'd) **cannot** return fewer results than one of its own terms

**Conclusion:** either the exclusions are silently dropped, or the query degrades to single-word/relevance
matching rather than phrase matching. In both cases the grouped query is *worse* than the plain phrase.
**Do not use it.**

### Therefore: one saved search per title

Paste each title **alone** into the LinkedIn search box, set **Location** in the UI filter, then toggle
**Set alert** → Daily.

```
ML Platform Engineer
MLOps Engineer
Machine Learning Platform Engineer
ML Infrastructure Engineer
AI Platform Engineer
AI Infrastructure Engineer
Inference Platform Engineer
Training Platform Engineer
SRE ML Platform
```

Nine clean phrase-match queues beat one muddy queue. LinkedIn's relevance ranking works *for* you on an exact
title and against you on a word soup.

### Where the exclusions went

The seniority and role exclusions below **cannot** be trusted as keyword operators. **Filter them at triage
instead** — skip any alert result whose title contains `Staff`, `Principal`, `Lead`, `Head of`, `Director`,
`Recruiter`, or `Sales`. That is a 5-second read per alert, versus a filter that silently fails.

Location likewise must be set in the **UI filter**, not the keyword string.

---

## 4b. The queries (reference only — see §4 for why not to use the grouped form)

Retained because the title list and the lane logic are still correct; only the operator syntax is
unreliable.

**Primary search (EU-remote lane):**

```
("ML Platform Engineer" OR "MLOps Engineer" OR "Machine Learning Platform Engineer"
 OR "ML Infrastructure Engineer" OR "AI Platform Engineer" OR "AI Infrastructure Engineer"
 OR "Inference Platform Engineer" OR "Training Platform Engineer" OR "SRE ML Platform")
NOT (intern OR Werkstudent OR "working student" OR Recruiter OR Sales OR "Head of" OR Director
 OR Staff OR Principal OR Lead OR "8+ years" OR "10+ years")
```

---

## 5. Filters to turn off

| Setting | Action |
|---|---|
| Generic "job recommendations" digest | **Turn off.** Unfiltered; it is volume noise. |
| "Jobs where you'd be a top applicant" | Keep **only** if it honours the same location + seniority filters |
| Recruiter InMail / "open to work" visibility | Leave as-is; `channel:recruiter` is live (#13 Bubblemaps) |
| Easy Apply | **Never use at a target company.** Apply on the employer's ATS — it parses better and the URL reveals the board token, which `jobradar` auto-adopts |

---

## 6. What LinkedIn is actually for

Per §4.2, the job alerts are the *fourth* priority use. In order:

1. **Hiring-manager discovery** — the input to the 60% outreach lane. Saved **people** searches
   (company + `platform` / `infrastructure` / `SRE` + `Engineering Manager` / `Lead` / `Head of Platform`),
   not job alerts.
2. **Positioning vocabulary** — the headline and About must carry the same terms as the queries above, or
   recruiter-side search will not surface the profile.
3. **Company following** — follow every watchlist company to catch announcements before the ATS post.
4. **Job alerts** — one input among several, restructured here.

---

## 7. Verification checklist

- [ ] Operator syntax checked once (§4)
- [ ] 5 alerts created: EU-remote primary, Berlin, Switzerland, FDE-secondary, Web3
- [ ] **Location set on every alert** (the single highest-impact change)
- [ ] Seniority exclusions (`Staff`, `Principal`, `Lead`, `8+ years`, `10+ years`) present in every keyword block
- [ ] Frequency = **Daily** on all five
- [ ] Generic recommendations digest turned off
- [ ] Easy Apply disabled as a habit at target companies
- [ ] Result sanity check: the first week's alerts should surface **AI/ML-platform-titled** roles. If they
      surface generic SRE/DevOps, the location filter is missing or the exclusions are not parsing

**Expected outcome:** fewer alerts, higher tier. If the alert volume drops sharply, that is the rewrite
working — the old volume was the tier-C pile.
