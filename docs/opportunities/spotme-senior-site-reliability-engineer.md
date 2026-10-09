# SpotMe — Senior Site Reliability Engineer (SRE), Europe (Remote)

**Posting:** https://job-boards.greenhouse.io/spotme/jobs/7927478003 (Greenhouse board `spotme`)
**Org:** **SpotMe** — enterprise B2B event platform, **founded 2000 in Lausanne, Switzerland**, US office
(Chicago) since 2007, **joined forces with Swiss Post in 2023**. Life-sciences arm **Onomi** (launched 2024):
HCP engagement for congresses, symposia, advisory boards and webinars. Claims **10M+ event relationships**,
**500K+ attendees/month**, **12,000+ event builders**, 4.7/5 on G2 and Capterra, and **15 of the top 20
life-science/pharma companies** as customers (J&J, Novartis, Roche, Sanofi, GSK, Takeda, Bayer, Boehringer,
Gilead), plus Deloitte/EY/KPMG, Workday, Mercedes-Benz, L'Oréal and BNP Paribas. VP Engineering: Marc Rochat
(ex-Kudelski, FIS). **A 26-year-old, Swiss Post-owned business — not a startup.**
**Market:** **EU-remote** ("Europe (Remote)") · **Tier:** **C** (bridge — no AI-infrastructure surface)
· **Channel:** ATS (Greenhouse) · **Track:** **`bridge`**
**Team:** reports to the Infrastructure Lead; works with engineering and product.
**Applied:** ✅ **2026-10-09** · **Stage:** Contacted · **Issue:** #33
**Compensation:** **not published.** EU-remote floor **€80,000** (§2). Established, Swiss Post-owned employer —
the floor is plausible but **unverified**. No equity framing in the ad.
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**
**jobradar:** board **added 2026-10-09** (`greenhouse:spotme`, `market: eu-remote`); scan verified row
`Senior Site Reliability Engineer (SRE)`, `location: Europe (Remote)`, `decision: review`, score 4.

## Tier and admission note

**Tier C, `track:bridge`** — a platform/SRE role with **no ML/AI-infrastructure surface** (the only AI element
is AI-assisted *development tooling*, which is a working practice, not platform ownership). Logged under the
2026-09-29 amendment to `CONTEXT.md`: ML is preferred but not a gate, and *"other platform/SRE roles case by
case"* when they clear the floor, the seniority band, the start-date constraint and offer architectural scope.
Labelled `track:bridge` so the conversion rate stays comparable with the AI-lane rows.

## Hard-filter checklist (§2)

- [ ] Not Staff/Principal / seniority band — ⚠️ **the honest miss.** The JD asks for **"around five or more
      years in a site reliability role, built on earlier experience as a system administrator or software
      developer"**. Vincent has **~4 years total**, and **no earlier sysadmin or developer career to stack
      underneath** (career began 2021–22). The §2 filter reads "3–6 yrs expected", so this is inside the
      letter of the band and at its **top edge**, not over it — but it is the first row where the stated floor
      sits above the evidence and there is no pre-SRE experience to offset it
- [ ] Compensation ≥ €80k (EU-remote) — ⚠️ **unverified**, not published. A 26-year-old Swiss Post-owned
      company is the profile most likely to pay it; ask
- [x] Geography — ✅ "Europe (Remote)" is a broad region containing France, in scope per Target Countries
      ⚠️ **but which entity employs is unverified**: founded in Lausanne, US office in Chicago, so "Europe
      remote" may mean a specific country list or contracting. **Ask before assuming the same answer Runware
      gave (#32)**
- [x] No day-one GPU / training / serving requirement — ✅ no ML infrastructure at all
- [x] Architectural scope — ✅ unusually explicit: own reliability end to end, set the Terraform/review
      standards others work from, own peak-traffic readiness, own a reliability metric against a baseline
      they establish

**Verdict: admissible case-by-case as a `bridge` row. Two genuine gaps — the 5+ years SRE band with no
pre-SRE career, and production AWS — plus the Python-essential requirement. Strong on infrastructure,
reliability, cost and security; weak on the code-authoring half of the JD.**

## Craft read

| JD requirement (weight) | Candidate evidence |
|---|---|
| **Terraform** + cloud-native AWS; IaC project from proposal to production (40% of the role) | ✅✅ Terraform/Terragrunt across multi-environment clusters, IaC change reviews. ⚠️ **AWS: not evidenced at all** — cloud depth is GCP (Cometh multi-zone) plus hybrid/on-prem. The JD asks for *"strong, production-grade experience with AWS"*; Azure is only a bonus. **This is the largest single gap** |
| Full-stack work spanning backend and infrastructure | ⚠️ infrastructure side yes; backend authorship is an excluded claim |
| CI/CD: **Jenkins** + GitHub Actions, **Packer**, Docker | ✅ Drone CI `deployed`, GitHub Actions `used`; Docker yes. ⚠️ **Jenkins `used` only** (Docaposte-era), **Packer not in the inventory** |
| **"You write real code to do it: Python is essential"**, ship a Python AWS Lambda at 3 months | ⚠️ **excluded claim** (operational scripting only). Explicitly targeted by `ml-platform-on-k8s` |
| Platform optimisation for **high availability and cost efficiency** (40%) | ✅✅ **the strongest section** — multi-zone HA on GCP, 40+ networks, $8B+ secured, **cloud spend −25%** |
| Peak-load scaling during high-traffic live events | ✅ capacity planning and scaling on production platforms ⚠️ but **Locust/Gatling load testing is not evidenced** |
| Security patches, hardening, firewall/network rules | ✅✅ Cilium network policy, Kyverno policy, Vault/SOPS/Teleport, **led ISO 27001**, HDS-regulated healthcare environment |
| On-call rotation, incident response and resolution (20%) | ✅✅ production SRE across two employers; incident response, triage, post-incident reviews |
| **Observability: Datadog, Pingdom, Elastic** | ✅ Datadog `used`, ELK and Loki, Prometheus/Grafana/Thanos, Jaeger tracing, OpenTelemetry, Alertmanager ⚠️ Pingdom not used |
| Relational **and** document databases | ✅✅ Postgres, MongoDB, Elasticsearch, Redis |
| **AI-assisted development with Claude**, concrete infra examples, push the team further | ✅✅ **the differentiator.** Concrete 2026 AI-assist/orchestration work exists, and this is the rare JD where *"you use AI coding tools in your infrastructure work"* is a stated requirement rather than a buzzword. This is the single strongest angle on the application |
| Persuading engineers outside your own team to prioritise reliability | ✅ architecture-translation bullet; cross-team risk mitigation |
| Own an observability service end to end; establish and improve a reliability metric (TtD/MTTR) against a baseline | ✅ observability ownership; MTTR reduction claimed at Cometh (⚠️ **no number on record** — the absent figure flagged in `docs/evidence-package.md`) |
| Migrate a complex on-premises build system to the cloud (6-month goal) | ✅ plausible: on-prem bare-metal at Docaposte into hybrid cloud at Kiln |
| Life-sciences / pharma customer base — regulated data | ✅ **relevant**: HDS-certified healthcare environment, ISO 27001 lead, GDPR |

## Risks, stated plainly

1. **AWS absence is the loudest gap**, and it is in the 40% infrastructure-development bucket, not a bonus.
   The honest framing is GCP multi-zone depth plus hybrid/on-prem and multi-cloud operations — not "AWS
   experience". Do not stretch this; it is the first filter a hiring manager will check.
2. **5+ years, no pre-SRE career.** The JD explicitly builds seniority on "earlier experience as a system
   administrator or software developer", which the profile does not have.
3. **Python-essential + Python Lambda at month three**, the excluded claim — the second JD today (with #32
   Runware) that makes Python authorship a requirement.
4. **"Europe (Remote)" does not name France.** Founded in Lausanne, US office in Chicago; the employment
   entity question is open.
5. **Live-event traffic is genuinely spiky** — the workload peaks are real, which is attractive, and the
   capacity/load-testing tooling (Locust, Gatling) is not evidenced.
6. **Compensation unpublished**, and no equity framing means the base carries the whole offer — which is
   good for the floor and bad if the base is set low for the market.

## What is genuinely attractive

- **Established, Swiss Post-owned, 26 years old** — the profile most likely to clear the €80k floor without
  an equity lottery, and the fastest-to-income shape (`CONTEXT.md` Earliest-Start Rule).
- **AI-assisted engineering is a hiring requirement, not a perk**: *"you'll have real latitude to use them"*,
  with 6- and 12-month objectives to embed them and measure reduced toil. Almost no SRE candidate can show
  concrete infra-tooling work here; Vincent can.
- **Explicit architectural ownership** — setting Terraform patterns and review practices as the default other
  engineers work from.
- **Cost efficiency is 40% of the role**, matching the −25% track record.
- **Pharma/life-sciences client base** aligns with the HDS + ISO 27001 + regulated-healthcare background —
  the same combination the Annapurna client (#31) wants.
- **The 1-month goal is unusually candid**: *"build a report on what surprised you: what looked fragile, and
  what was hard to find documented"* — a diagnostic-first culture, which suits an SRE who documents.

## Questions to put in writing (first follow-up)

1. Base salary band? (No band published; no equity framing.)
2. **Which country/entity** would employ for "Europe (Remote)" — France in scope?
3. Is **AWS production experience a hard gate**, or is GCP-plus-multi-cloud operations acceptable with a
   ramp? (Ask plainly; this is the decisive filter.)
4. Is the **"five or more years"** a firm bar?
5. On-call frequency and compensation, and how the rotation is shared.
6. What does *"full-stack work spanning the back end"* mean in practice for this role?
7. Is the current stack the target stack, or is there a cloud migration already planned (the 6-month goal
   hints at one)?

## Timeline

- Contacted / applied: **2026-10-09** (Greenhouse)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Salary: not stated in the application
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** if this one ends, the cause should be readable — **relevance** (AWS, Python authorship, 5+ years)
  or **compensation**, not location. Second `bridge` row in the DE/EU-remote set alongside #22 1GLOBAL.
- What would have changed the outcome: —

## Funnel delta

Applications sent +1 (2026-10-09) · **EU-remote lane** · `tier:c` · **`track:bridge`** · board gap closed
(SpotMe was not tracked by jobradar before this application). Third application logged today, and the first
in the `bridge` track since #22 1GLOBAL.
