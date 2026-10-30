# Rockstar Recruiting AG — AI Platform Engineer (Portugal-based)

**Posting:** https://swissdevjobs.ch/jobs/Rockstar-Recruiting-AG-AI-Platform-Engineer-AI-Start-up-Portugal-based-role · Portugal
**Market:** CH as logged (mislabelled — the feed is Swiss, the role is not) · **Tier:** B · **Channel:** ATS · **Track:** `track:ai`
**Applied:** ✅ 2026-10-29 · **Closed:** ❌ 2026-10-30 (refusal, reason **stated**)
**Evidence version used:** pre-project
**Source:** jobradar `7d2839c9d0012873` · swissdevjobs.ch RSS feed

## What the role was

An unnamed AI start-up hiring through Rockstar Recruiting AG, an agency advertising on the Swiss job
board. The role was AI platform engineering (the jobradar signals were `ai-platform`, `platform`), based
in **Portugal**, band CHF 100,000–140,000. The employer was withheld.

Two problems were visible at application time and not recorded then:

1. **Location.** Portugal is not one of the four target countries (France, Germany, Switzerland, the
   Netherlands). Under the §2 location filter this posting failed unless it was remote and open to
   France, which the ad did not state. Logged anyway, which was the correct call for funnel data, but the
   market label CH made it look admissible in the tracker when it was not.
2. **Employer identity.** Agency, client unnamed. No hiring manager, no team, no way to read the JD against
   real infrastructure.

## The refusal

> Rejected because there is no AI production experience on the resume.

This is the first **explicit, named** rejection reason in the pipeline. Everything else closed as
`unknown`. It is also the only rejection that confirms something already recorded as an evidence boundary
rather than a guess: `CONTEXT.md` → Evidence Boundaries lists "ML lifecycle tooling — pipelines, model
registry, serving platforms, drift monitoring" as excluded from current positioning. The employer said the
same thing.

Timing: applied 2026-10-29, refused 2026-10-30. One business day. That is a CV screen, not a process —
nobody was weighing the candidate against another finalist.

## Normalised reason

`readiness` — immediate-readiness evidence gap. Not relevance (the profile translates), not compensation
(the band was never discussed), not location (never raised).

## What this changes

- The readiness gap is now **employer-confirmed** for the AI lane at tier B. It is no longer an inference
  from the absence of keywords on the CV.
- The fix is the evidence artifact, not the CV wording: `ml-platform-on-k8s` (`docs/ml-platform-project.md`)
  produces the ML-lifecycle evidence a screen looks for. Rewriting bullets cannot close it.
- Until that artifact exists, AI-lane applications to roles whose JD asks for production AI/ML must be
  treated as low-yield. The 70% France-anchored infrastructure weight and the 20% Web3 weight are where the
  effort should sit; AI applications stay in the mix but are not the volume.
- Do not re-apply to this agency without the artifact.

## Outcome

- Stage reached: **Closed at Contacted**, never screened
- Rejection reason: **`reason:readiness`**
- Follow-ups: none owed — the refusal arrived before the first follow-up window opened (due 2026-11-05)
- Feedback request: **not sent.** §3 prescribes the feedback request after a *recruiter-screen* rejection;
  this never reached a screen. The refusal already named the reason, so a request would add nothing.
- What would have changed the outcome: a completed `ml-platform-on-k8s` artifact, with serving, registry
  and SLO evidence in it. Nothing in the application text could have substituted for it.
