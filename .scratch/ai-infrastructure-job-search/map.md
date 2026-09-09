# Build an AI Infrastructure Job Search and Training Strategy

Label: wayfinder:map

Status: complete

## Destination

A decision-complete 12-week system that generates qualified interviews for AI Infrastructure Engineer roles and closes the highest-value capability gaps with employer-relevant evidence. Switzerland and Berlin are the primary relocation markets; selective France and EU-remote roles may serve as bridge opportunities.

## Notes

Domain: career strategy for an experienced SRE moving into AI infrastructure. Consult `/grilling` and `/domain-modeling` for human decisions and `/research` for external market facts. Planning only: the map specifies the search and training system but does not execute applications, networking, asset production, or coursework.

Standing decisions: target AI Infrastructure Engineer roles; allocate primary-market effort Switzerland 60% / Berlin 40%; use a tiered employer thesis—AI infrastructure vendors first, model labs selectively, and AI product companies only when the role owns substantive AI infrastructure.

Source profile: `~/Documents/resume_v3.pdf`. Canonical terms: `CONTEXT.md`.

## Decisions so far

<!-- Closed ticket pointers are appended here. -->

- [Map the Switzerland and Berlin AI Infrastructure Market](issues/02-map-target-market.md) — Use a Zurich-centered infrastructure/global-compute funnel and a Berlin-centered internal ML-platform funnel, searched through responsibility-based title aliases.
- [Benchmark AI Infrastructure Hiring Evidence](issues/03-benchmark-role-evidence.md) — Lead with proven SRE/Kubernetes strengths; the largest visible gaps are programming evidence, demonstrated GPU operations, AI workload stacks, and explicit SRE mechanisms.
- [Diagnose the No-Response Pipeline](issues/01-diagnose-no-response-pipeline.md) — The funnel reaches recruiter screens; the failure is qualification across relevance, immediate-readiness evidence, and compensation—not application response volume.
- [Choose the Candidate Positioning Thesis](issues/04-choose-positioning-thesis.md) — Production SRE moving into AI infrastructure, entering through reliable AI platform operations; lead with Kubernetes, reliability, observability, and cost evidence; exclude GPU, programming, training, and serving claims until evidence closes those gaps.
- [Choose Employer Selection and Tiering Rules](issues/05-choose-employer-criteria.md) — Three-tier admissibility (AI-infra > SRE at AI-native > high-quality bridge); hard filters on seniority, compensation floors, day-one expertise requirements, and remote-start-or-relocation-support; five mandatory recruiter-screen questions.
- [Choose Capability and Training Priorities](issues/06-choose-training-priorities.md) — One coherent GPU fleet K8s operator project closes programming (Python then Go), GPU operations, and SLO/error-budget gaps; distributed training and datacenter fabric positioned away with light conceptual study only.
- [Prototype the Candidate Evidence Package](issues/07-prototype-evidence-package.md) — CV restructure with transition framing, LinkedIn narrative with “currently building” project, GitHub README outline for GPU fleet operator, and three outreach templates embedding the recruiter-screen questions.
- [Choose Application and Relationship-Building Channels](issues/08-choose-acquisition-channels.md) — Outreach-first (60%), applications second (25%), recruiters inbound+proactive (10%), GitHub+follow-up (5%); email-first for Switzerland, LinkedIn-first for Berlin; three follow-up rules; rules out agency recruiters, job boards, and networking events as primary channels.
- [Choose the Weekly Operating Cadence and Adaptation Rules](issues/09-choose-operating-cadence.md) — ~35 hrs/week split 40% search / 50% training / 10% management; phase-adjusted ramp from 20/70/10 in weeks 1–2 to 55/35/10 in weeks 10–12; eight funnel signals; seven adaptation thresholds including response-rate, screen-to-rejection, zero-interviews-by-week-6, comp-mismatch, project-slip, market-rebalance, and bridge-opportunity; Friday weekly review ritual.
- [Approve the Integrated 12-Week Strategy](issues/10-approve-integrated-strategy.md) — Candidate-approved 35-hour weekly plan with role filters, market split, outreach-led acquisition, week-by-week Python and Go evidence milestones, cohort-aware pipeline tracking, and explicit adaptation rules. Prototype: branch `prototype/integrated-strategy`, commit `d2fd804`.

## Out of scope

- Executing applications, outreach, courses, projects, or profile rewrites during wayfinding.
- Interview-loop preparation, offer negotiation, visa processing, and the physical relocation itself; this map ends at a system designed to generate qualified interviews.
- A general machine-learning curriculum unrelated to evidence required for the target role.
