# Approve the Integrated 12-Week Strategy

Type: prototype
Status: resolved
Blocked by: 05, 06, 07, 08, 09

## Question

Does the integrated 12-week search and self-training strategy form a realistic, internally consistent operating plan that Vincent can commit to, with clear priorities, trade-offs, checkpoints, and adaptation rules?

## Answer

Approved by Vincent on 2026-09-09.

The nine upstream decisions form a realistic and internally consistent 12-week operating plan. The integrated strategy prototype is captured on branch `prototype/integrated-strategy` at commit `d2fd804`, file `prototype/integrated-12-week-strategy.md`.

### Approved operating model

- Approximately 35 hours/week for 12 weeks.
- Weeks 1–2: 20% search / 70% training / 10% management.
- Weeks 3–6: 45% search / 45% training / 10% management.
- Weeks 7–9: 50% search / 40% training / 10% management.
- Weeks 10–12: 55% search / 35% training / 10% management.

### Approved priorities

- Switzerland 60% / Berlin 40%, with a data-triggered rebalancing rule.
- Outreach-first acquisition; filtered ATS applications; proactive in-house recruiter relationships; external agencies inbound/opportunistic only.
- Complete Python GPU fleet operator with bounded real-GPU/DCGM validation, SLOs, alerts, and runbook by week 6.
- Complete Go/controller-runtime port by week 12; protect Python evidence if milestones slip.
- Update claims only after the repository provides observable evidence.
- Preserve hard compensation and remote-start/relocation filters under funnel pressure.

### Verification

- All 12 weekly allocations sum to 35 hours.
- Every map issue link resolves.
- Tickets 01–09 were resolved before integration.
- Search/channel, market, evidence-version, and rejection-reason cohorts remain separable in the pipeline tracker.
- The recruiter-channel contradiction was resolved: cultivate 3–5 in-house talent contacts; do not cultivate external agencies.

This resolves the final decision ticket. The wayfinder map is decision-complete; execution remains outside wayfinding scope.
