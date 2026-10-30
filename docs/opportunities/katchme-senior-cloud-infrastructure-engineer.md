# KatchMe (agency) — Senior Cloud Infrastructure Engineer, HealthTech B2B

**Posting:** https://www.linkedin.com/jobs/view/4484924882/ · France, full remote
**Market:** FR · **Tier:** C (SRE/platform bridge; no ML surface) · **Channel:** recruiter (external agency, inbound) · **Track:** `track:bridge`
**Applied:** ✅ 2026-10-30 (LinkedIn, agency ad) · **Stage:** Contacted
**Follow-ups:** 1st due 2026-11-06 → 2026-11-10 · final 2026-11-13 → 2026-11-19
**Evidence version used:** pre-project
**Source:** LinkedIn job `4484924882` · not present in the jobradar store (agency ad, no ATS URL to adopt)
**Recruiter:** Thomas Cabanès — https://fr.linkedin.com/in/thomas-cabanes

## What the role is

An external recruitment agency (KatchMe) advertising on behalf of an unnamed **HealthTech scaleup** with an
AI-powered platform, an in-house tech team of ~20, and an international patient base. The employer is
withheld, so there is no employer-side ATS, no hiring manager, and no company page to research before a
screen. Everything below comes from the agency's copy.

Role: sole owner of infrastructure maintainability and scalability, reporting to the CTO, "creating the
infra function" rather than filling a defined box. Stack stated: **GCP, GKE, Cloud Run, Terraform, GitHub
Actions, OpenTelemetry, Axiom**. Full remote with an optional Paris office and a stated quarterly on-site.

External agency recruiters are "inbound/opportunistic only" (`docs/search-plan.md` §3), which is exactly
how this arrived. Logged as a real application, not a long-shot: it clears the location, language, role-type
and scope filters. The one unresolved filter is compensation.

## Hard-filter verdict (§2, as amended 2026-10-09)

- [x] **Role type** — infrastructure/platform ownership, not software engineering. Responsibilities
      override title, and the responsibilities are IaC, scaling, ops ownership, coaching.
- [x] **Location** — full remote from France, optional Paris office → France-based, no permit, no move.
- [x] **JD language** — French. Allowed (`allowed_languages: [en, fr]`).
- [ ] **Compensation** — "salaire fixe hyper attractif" with **no figure**. France-compatible floor is
      €80,000; tier C bridge floor €70,000. **Unverified — ask at the first call.**
- [x] **Not Staff/Principal** — stated bar is 5+ years, no 8+ years demand.
- [x] **Architectural scope** — owns infra strategy, prioritisation, and cross-team coaching. This is the
      strongest part of the posting against the role-selection criterion.
- [ ] **AI workload exposure** — none. A HealthTech product "propelled by AI" is the only mention. Preferred,
      not required (§2, amended 2026-09-29), so this does not block; it is why the track is `bridge`.

**Verdict: admissible, applied. One filter unresolved — compensation. AI is absent by design, not by failure.**

Two notes against the CV, to handle rather than hide:

1. **5+ years** asked, CV shows four years of continuous infra roles (Dec 2021 → Jan 2026). Lead with scope
   ($8B+ secured, 40+ networks, HDS-certified healthcare), never with tenure.
2. **No GKE/GCP-first claim needed** — GCP is already the strongest cloud evidence (Cometh multi-zone
   Kubernetes on GCP). Terraform, GitHub Actions, OpenTelemetry all sit inside the evidence boundary.

The domain fit is real: the candidate's regulated-healthcare work at Docaposte (HDS) matches a HealthTech
employer handling patient data, and the "build the function, coach the team" shape matches the
architecture-and-communication criterion.

## Questions for the agency call

1. Who is the client, and at which stage is the hiring process — direct with the CTO or through the agency?
2. Total compensation range, and the BSPCE split. Does the base alone clear €80k?
3. Is there an existing infrastructure team, or is this the first infra hire? What runs the platform today?
4. Remote contract shape: French CDI full remote, or a contractor arrangement?
5. Why was the role opened externally rather than filled in-house?

## Application answers, if asked

Prepared on request; nothing was submitted beyond the LinkedIn application. The standard answers from
`docs/opportunities/vivenu-senior-platform-engineer.md` apply unchanged (stack list, salary range
€90,000–€100,000, high-traffic paragraph). Do not reuse them blind: this employer is masked and HealthTech,
so the Docaposte/HDS line is the one to lead with.

## Outcome

- Stage reached: **Contacted** (LinkedIn application, 2026-10-30)
- Next action: follow-up 1 to Thomas Cabanès on 2026-11-06, one message, asking for the client name and the
  compensation range.
- Board Stage: **Contacted**
