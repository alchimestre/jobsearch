# 1GLOBAL — Senior Site Reliability Engineer (SRE)

**Posting:** https://www.linkedin.com/jobs/view/4468498942/ · Berlin, Germany (posted ~1 week before applying)
**Org:** 1GLOBAL (1GLOBAL Holdings B.V., trading as 1GLOBAL) — global mobile communications provider. eSIM /
Remote SIM Provisioning, own mobile core network across 15 countries, regulated telecom operator in 43
countries, >80M connected people and devices. Founded 2022; 550+ staff in 16 countries; >US$200M revenue,
profitable. HQ Netherlands; R&D hubs Lisbon, **Berlin**, São Paulo. Customers: banks, multinationals,
retailers, PSPs.
**Apply route:** LinkedIn (this posting) → mirrored from 1GLOBAL's own careers site (`1global.com/vacancies`,
bespoke vacancy IDs), so there is **no jobradar-adoptable ATS board** — unlike Greenhouse/Workable employers.
**Market:** **DE (Berlin)** · **Tier:** **C** (non-AI, non-Web3 platform SRE — see verdict) · **Channel:** ATS ·
**Track:** `bridge`
**Applied:** ✅ **2026-09-30** · **Stage:** **Closed** (refused 2026-10-05; no screen reported)
**Follow-ups:** 1st due **2026-10-07 → 2026-10-09** · final **2026-10-14 → 2026-10-20**
**Compensation:** **undisclosed** ("competitive compensation packages… performance-driven bonuses") →
**Berlin floor €80,000 must be confirmed at first contact.**

## Hard-filter verdict — deliberate long-shot, with two hard filters unverified

| §2 filter | Result |
|---|---|
| Not Staff/Principal | ✅ "Senior SRE", "senior individual contributor", 5+ yrs. No staff/principal title, no 8+ years |
| Experience band | ⚠️ **5+ years demanded (incl. 2+ dedicated SRE) against ~4 years of continuous infra roles (Dec 2021 → Jan 2026)**; the dedicated-SRE clock is closer to 2 (Kiln 2024–2026). Gap, not fatal — lead with scope, never with tenure |
| Compensation ≥ €80k (Berlin) | ⚠️ **undisclosed.** No number in the JD, no band published. Unverified hard filter |
| On-site DE allows 8–12 week remote start / relocation assistance | ⚠️ **unverified and binding.** The JD says only *"we are open to hiring this role in Berlin, Germany"* — **no remote or hybrid statement anywhere**. Per `CONTEXT.md`, relocation happens only on a signed offer, funded by assistance or an 8–12 week remote start |
| No day-one direct GPU/training/serving expertise | ✅ none mentioned |
| AI/Web3 surface + architectural scope | ❌ **no AI/ML and no Web3 surface** (telecom/eSIM/mobile core) — but ✅ **architectural scope is real**: SLIs/SLOs/error budgets, redundancy and DR validation, chaos/fault injection, capacity planning, cost optimisation. Not a runbook role |
| Tier gate | ⚠️ **Fires.** §2 Admit 5 admits non-AI, non-Web3 TIER C bridges *"only in the last-resort window from ~Apr 2027"*. The 2026-09-29 ML-preference amendment admits "any other platform/SRE role with architectural scope … if it clears compensation, seniority, and start-date filters". **The two clauses conflict for this role.** Recorded as a **deliberate long-shot**; flag at the next Friday review |
| Country / JD language | ✅ DE is a target country; the JD is in English (the German-language-JD exclusion does not apply) |
| Start date ≤ 2027-06-15 | ✅ no stated bar |

## JD-to-evidence map

| JD requirement (must-haves) | Candidate evidence |
|---|---|
| 5+ yrs SRE/systems/infra, 2+ dedicated SRE | ⚠️ ~4 yrs continuous infra; ~2 dedicated SRE (Kiln) |
| Linux systems engineering, distributed systems, networking | ✅ Linux + distributed; networking **partial** — load balancing and DNS are evidenced (HAProxy, MetalLB, Traefik, Kong), **BGP/VXLAN are not** (Cilium CNI/VXLAN encapsulation is the closest indirect evidence) |
| High-availability, mission-critical production | ✅ Kiln: distributed infrastructure securing $8B+ across 40+ protocol networks, multi-zone, sustained protocol traffic |
| Redundancy / failover testing, DR, HA validation | ✅ Multi-zone and multi-environment Kubernetes; Velero backup/restore deployed at Kiln; bare-metal on-prem K8s at Docaposte |
| Monitoring, observability, incident management | ✅ **Named-match list** — Prometheus, Grafana, Loki, **Thanos** (used, long-term storage), OpenTelemetry; ELK, Datadog, Jaeger also in `docs/tooling-inventory.md` |
| **Proficiency in Python, Go, and Bash** | ❌ **the sharpest gap in the JD.** Bash ✅; Python is operational scripting only and Go is not evidenced at all — `CONTEXT.md` Evidence Boundaries explicitly exclude production Python/Go claims |
| Kubernetes, orchestration, service mesh | ✅ Kubernetes production ownership; ⚠️ service mesh — Cilium (CNI/network policy) is the evidence, no Istio/Linkerd |
| AWS (EKS, EC2, VPC) + on-prem integration | ⚠️ **not in the tooling inventory** — the estate is GCP-first hybrid cloud. On-prem integration ✅ (Docaposte bare-metal K8s). EKS↔GKE transfers, but this is untested evidence |
| Terraform / IaC | ✅ Terraform, Ansible, multi-environment |
| Networking fundamentals (routing, LB, BGP, DNS, VXLAN) | ⚠️ partial, as above |

**Nice-to-haves:** telecom/carrier-grade ❌ new domain · chaos engineering ⚠️ fault injection not yet evidenced
(the artifact drills are the closest) · capacity planning and traffic engineering ✅ · reliability
dashboards ✅ · **ISO 27001 / NIST SP 800-53 ✅** — Vincent led the ISO 27001 implementation at Cometh.

## Why it was worth applying despite the verdict

1. **Berlin is destination #2 and the preferred first physical move.** A Berlin employer with real relocation
   logistics is how the move gets funded, and 1GLOBAL has offices in 12 countries with a Berlin R&D hub.
2. **The SRE core is exactly what the plan's artifact targets** — SLIs/SLOs/error budgets, HA/DR validation,
   chaos/fault injection, capacity planning. Interviewing here is rehearsal for the primary lane.
3. **Carrier-grade at 80M+ connected devices is genuine architectural scope**, which is the filter that a
   Tier C bridge has to clear. It clears it — the missing piece is the AI/Web3 surface, not the depth.
4. **Earliest-start rule:** a role requiring physical relocation is *not* the fastest route to income. It
   ranks below every EU-remote/France-compatible option regardless of how it goes.

## Pre-screen questions (ask before any screen)

1. **Compensation band** for senior SRE in Berlin and the variable/bonus split. (Hard filter, unverified.)
2. **Work mode**: how many days in office, and is an **8–12 week remote start from France** possible while
   relocating — or is relocation assistance provided? (Hard filter, unverified.)
3. Is the *"Python, Go, and Bash"* line about **automation glue or product services**? This frames the honest
   answer and decides whether the gap is disqualifying.
4. **Service mesh** in use — Cilium is the candidate's evidence; is Istio/Linkerd in the stack?
5. **On-prem vs cloud ratio** (AWS EKS/EC2/VPC is named) and the **on-call model / team size**.

## Stack overlap and gaps

**Overlap:** Kubernetes production ownership · Terraform/IaC · Prometheus, Grafana, Loki, Thanos,
OpenTelemetry · incident management and MTTR reduction · Velero backup/restore · multi-zone HA ·
capacity planning and cloud cost reduction · ISO 27001 (candidate *led* the implementation).

**Gaps — state plainly:** production **Python/Go** (Bash and operational scripting only) · **AWS** (GCP-first
estate) · **BGP/VXLAN** at the carrier-networking layer · **service mesh** beyond Cilium CNI · telecom domain
(new) · chaos engineering as a named practice (artifact drills pending).

## Timeline

- Contacted / applied: **2026-09-30** (LinkedIn)
- Follow-up 1 due (5–7 business days): **2026-10-07 → 2026-10-09**
- Follow-up 2 due (10–14 business days): **2026-10-14 → 2026-10-20** (final)
- Screen date: —
- Interview dates: —
- Outcome: **refused 2026-10-05** (email; received/reported in this audit 2026-11-05)

## Outcome record

- Stage reached: **closed at Contacted; no screen reported** (applied 2026-09-30 → refusal email 2026-10-05)
- Board Stage: **Closed** (set 2026-11-05)
- Rejection reason: **`unknown`** — email says the team will not proceed and offers no individual feedback.
- Follow-ups cancelled.
- **Long-shot flag:** Tier C bridge ahead of the last-resort window, ~4 years against a 5+ years ask, and a
  Python/Go proficiency line the evidence boundaries forbid claiming. Logged so the funnel stays
  interpretable — **do not pool with the AI/ML primary lane** (#9 SAP Fioneer, #11 Workist, #12 Langdock).
- **Watch:** compensation and work mode are both unverified hard filters. If either fails, nothing else
  matters — and both are cheap to establish in the first exchange.
- What would have changed the outcome: an ML/AI or Web3 surface, or a stated relocation/remote-start policy.
