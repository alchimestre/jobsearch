# Jimdo — Senior Infrastructure Engineer (Platform / Wonderland)

**Posting:** https://www.linkedin.com/jobs/view/4472485817/ (LinkedIn; canonical
`de.linkedin.com/jobs/view/senior-infrastructure-engineer-at-jimdo-4472485817`) · location listed as
**Germany**, "fully remote work set-up"
**Org:** **Jimdo** — website builder founded 2007 in a Northern German farmhouse, Hamburg HQ; **profitable**,
220+ people, 50+ nationalities across 15+ countries, 36M+ sites built. Self-description: *"an AI-powered
platform"* for websites, design and business tools.
**Market:** **de** (Berlin/Germany lane, 10% allocation) · **Tier:** **C** (platform/SRE bridge; AI is the
product direction, not the role's surface) · **Channel:** ATS (LinkedIn) · **Track:** `bridge`
**Applied:** ✅ date not recorded — the application was made before this row was opened; only the refusal was
reported · **Stage:** **Closed 2026-10-15** — negative answer, no reason given, never screened
**Follow-ups:** none owed — the refusal arrived before any window opened
**Posting at read time (2026-10-15):** live, **over 200 applicants**, Mid-Senior level, full-time

## Hard-filter checklist (§2 + lane filters)

| Filter | Result |
|---|---|
| JD language — English or French | ✅ **PASS** — JD body is English |
| Location — FR-based / FR-employable remote / on-site w/ relocation | ⚠️ **NOT VERIFIED — treated as a location long-shot.** The posting is listed for **Germany**; Jimdo is remote-first and employs across 15+ countries, but no French entity, EOR or France-eligible remote statement appeared in the posting. A Germany-only scope would fail the filter, so the honest read is unverified rather than pass |
| Role type — no software-engineering roles | ✅ **PASS** — internal platform engineering: AWS/EKS, Terraform, deployments, observability, developer workflows. The Go work is platform tooling, not application authorship |
| Not Staff/Principal | ⚠️ **marginal** — LinkedIn band **Mid-Senior**, but the JD asks **5+ years** in infrastructure/platform/DevOps/SRE against ~4 evidenced years |
| Compensation ≥ €80k (Germany floor) | ⚠️ **NOT STATED** — unverified, including whether the German band is set against Hamburg or Berlin |
| AI workload exposure AND architectural scope | ⚠️ **weak** — "explore and integrate AI tools that improve engineering productivity" is a productivity ask, not ML serving. AI is the company's product direction → **Tier C** |

**Verdict: admissible with two open caveats — location unverified and 5+ years against 4 evidenced.** Logged
and pursued as a Tier C bridge; the refusal closes it with neither caveat resolved.

## Craft read — requirements vs evidence

| Requirement | Evidence |
|---|---|
| 5+ years infrastructure / platform / DevOps / SRE | ⚠️ ~4 evidenced years — the standard gap |
| Production Kubernetes | ✅✅ multi-zone Kubernetes and bare-metal production clusters at Kiln/Cometh |
| Deep Terraform IaC | ✅✅ Terraform, Terragrunt, Ansible across hybrid-cloud estates |
| AWS, EKS preferred | ⚠️ GCP-primary evidence; AWS exposure partial |
| CI/CD and GitOps (GitHub Actions, ArgoCD) | ✅ GitLab CI in production evidence; GitHub Actions and ArgoCD on the evidence-project toolchain |
| Observability — Prometheus, Grafana, Loki, alerting, incident management | ✅✅ Prometheus/Grafana/Loki/OpenTelemetry deployed; incident response and post-incident reviews |
| Production-quality Go | ❌ excluded claim — Python and Shell evidenced; Go is a phase-2 toolchain item, not shipped code |
| Platform security, secrets management, compliance (Vault named) | ⚠️ security hardening evidenced; Vault and Cloudflare not evidenced |
| Partner with engineering teams on deployment reliability and DX | ✅✅ internal-platform and cross-team work at Kiln/Docaposte |

## Risks

1. **Location is the untested filter.** A German posting from a remote-first company that employs in 15+
   countries: the question is whether "remote" reaches France or stops at the German entity. It was never
   asked in writing — the refusal arrived first.
2. **5+ years against ~4 evidenced.** Same shape as the EYE Security row: not a Staff bar, but above the
   current evidence.
3. **Go is named as the platform language** and is an excluded claim today.
4. **No compensation band.** The German floor is €80,000 and remote-first German employers often anchor on a
   Hamburg band.

## Questions to put in writing (first follow-up)

**Never asked — the refusal of 2026-10-15 arrived before the window opened.**

1. Which entity or EOR would employ a France-based engineer, and does the remote scope include France?
2. Total compensation band and whether it is location-adjusted for Germany outside Hamburg?
3. How much of the platform is Go, and is production Go expected on day one?
4. Which team owns the on-call rotation for the platform, and how large is it?
5. Does the platform team touch any model-serving or GPU workload, or is AI entirely product-side?

## Timeline

- Contacted / applied: **date not recorded** (LinkedIn ATS) — the full row is in LinkedIn → My Jobs → Applied if
  the date ever matters for speed arithmetic
- Follow-up 1 due (5–7 business days): **never scheduled** — the refusal arrived before it
- Follow-up 2 due (10–14 business days): **never scheduled**
- Screen date: — · Interview dates: — · Outcome: **2026-10-15 — negative answer, no reason given**

## Outcome record

- Stage reached: **closed at Contacted, never screened**
- Board Stage: **Closed** (set 2026-10-15)
- Rejection reason: **`unknown`** — no reason given. Two candidate causes were on record before the refusal:
  the unverified location/entity question and the 5+ years bar against ~4 evidenced. A bare ATS refusal names
  neither, so the label stays `unknown` rather than a guess.
- Duration: **unknowable** — the application date was never recorded, so the response time carries no signal.
  This is the first row in the pipeline whose timeline cannot be reconstructed.
- Follow-ups: **none sent** — no window had opened.
- What would have changed the outcome: a written answer on the entity/remote scope before applying, which
  would have settled the location filter; and a published band to test.
- Next action: **closed.** No further contact. Issue closed with `reason:unknown`.

## Funnel delta

Applications sent +1 (date unrecorded) · **de lane (Berlin 10% allocation)** · `tier:c` · `track:bridge`.
Two filters left unverified at application time — location and the years bar. This row is logged
retroactively: the refusal was the first the pipeline saw of it.

Closed 2026-10-15 at Contacted, never screened, `reason:unknown` — the **15th closed row**, and the count of
unclassified closures is now **15 of 15, 14 of them pre-screen** (MarvelX #21 remains the only closure that
reached a live screening step). It adds nothing to the classified-rejection count, and it is the first
closure with no recorded application date, so it cannot be used in any speed-to-answer arithmetic.
