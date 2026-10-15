# Camunda — Senior Site Reliability Engineer (Remote, France)

**Posting:** https://jobs.ashbyhq.com/camunda/ae101c99-ef04-4317-bf78-da18d61dcda4 (Ashby)
**Org:** **Camunda** — enterprise platform for **agentic orchestration** (coordinate AI agents, people and
systems across business processes; governance, auditability, human oversight). 700+ organisations, 9 of the top
10 US banks. **Fully remote and global**, and *"transforming into an AI-first organisation, built on our own
platform"*. GP Bullhound Top 100 Next Unicorn, Great Place to Work 2025, ranked 3rd in Flexa's 2026 Most
Flexible Companies.
**Market:** **eu-remote** · **Tier:** **B** · **Channel:** ATS · **Track:** `ai`
**Applied:** ✅ **2026-10-09** · **Stage:** Contacted · **Issue:** #39
**Quoted salary:** **€80,000 – €100,000** (entered on the form). See the note below — the range floor equals the
€80,000 floor, so it anchors low.
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — "Senior SRE", senior IC; "mentor others" is a duty, not a management role
- [x] JD language — English ✅
- [x] **Location** — fully remote, and Camunda hires France-based staff **through Remote.com, their global
      employer of record**. Remote.com employs in France, so this is a French employment contract, not a
      relocation and not a contractor arrangement. **Passes without a relocation question.**
- [x] Not a software role — platform, reliability and infrastructure work. Kubernetes, IaC, observability,
      incident response, automation. No product or application coding.
- [x] AI exposure — the employer is AI-first (agentic orchestration) and *"responsible use of AI tools"* is a
      stated **must-have**.

**Verdict: admissible, and one of the cleanest passes in the pipeline. No location gate, no language gate, no
software-role gate.**

## Compensation, and the Remote.com contract

Camunda publishes bands for four markets only, as total target cash from a Standard-market minimum to a
Major-market maximum:

| Market | Range |
|---|---|
| United States | $149,800 – $241,500 |
| United Kingdom | £94,100 – £154,700 |
| Singapore | S$186,100 – S$279,100 |
| Canada | C$159,100 – C$261,600 |

*"If you're based elsewhere, you'll be hired via Remote.com (our global employer partner), and your Talent
Acquisition Partner will provide a personalized Total Rewards Calculator after your first interview."* So
**no band exists for France**, and the number on the form is the only anchor. Camunda also states they
*"typically hire in the first half of the range"*.

**Contract mechanics to keep straight:**
1. Remote.com is an **employer of record**. The contract is employment with French payroll, not invoicing.
   So the quoted figure is a normal **gross annual salary** — no contractor premium.
2. Camunda pays the Remote.com markup **on top**. It does not come out of the salary.
3. Equity is separate (VSOP). Do not price equity into the number.
4. A UK *Standard-market minimum* of £94,100 (≈€108k `[INFERENCE — no FX source consulted]`) is well above
   €80k, so a French number in the €80–100k range is cheap for Camunda, not expensive.

**⚠️ Recorded honestly: the submitted range is €80,000 – €100,000, and its floor equals the binding floor.**
A range that starts at the floor invites an offer at the floor. For the next role, the pattern to use is a
floor roughly 10% above the binding floor, or a single number.

## Craft read — five must-haves, five matches

| Must-have | Evidence |
|---|---|
| **Deep hands-on Kubernetes in production** — workloads, networking, storage at scale | ✅✅ multi-zone production clusters (Cometh), multi-environment clusters with Terraform (Kiln), **bare-metal** clusters with MetalLB/Cilium/HAProxy (Docaposte) |
| **IaC expertise, Terraform or similar** — version, test, deploy safely | ✅✅ Terraform across multi-environment clusters; Terragrunt; Ansible at Docaposte |
| **Monitoring and observability** — Prometheus, Grafana or similar | ✅✅ Prometheus, Grafana, Loki, ELK, **OpenTelemetry**, Datadog, Jaeger, Thanos, Alertmanager |
| **3rd-level support and incident response** — diagnose under pressure, root cause, prevent recurrence | ✅✅ production SRE across two employers; incident response; post-incident reviews; the CV's Docaposte line is a recovery incident |
| **Automation, raising the quality bar** | ✅✅ GitOps (Flux, Argo CD), Drone CI, GitHub Actions, hardening, −60% CI build time |
| **Responsible use of AI tools** — research, review, docs, test generation; validate outputs; keep human accountability | ✅✅ the 2026 AI-assist/orchestration work — and this JD puts it in the **must-haves**, which is rare |

**Nice-to-haves:** major cloud providers (AWS/EKS, GCP/GKE) — ✅ GCP multi-zone, ⚠️ **AWS absent** (managed
K8s specifically unproven); **Argo CD / GitOps** — ✅ Argo CD `used`, **Flux `deployed`**; **Python, Go or
similar for scripts and automation** — ✅ operational scripting is in bounds (application authorship is not);
**SLOs and alerting frameworks** — ⚠️ **excluded claim**, targeted by `ml-platform-on-k8s`.

## Risks

1. **The quoted range anchors at the floor.** Expect an offer near €80–85k unless the interview changes the
   picture.
2. **AWS/EKS is a nice-to-have, not a gate**, but it is the fourth JD in a row to name AWS. It is the most
   repeated gap in the pipeline.
3. **"Mentor others"** and "help less experienced engineers" appear as duties. Formal mentoring is not on the
   CV — answer from cross-team platform work.
4. **SLOs** are a nice-to-have that the candidate cannot claim yet.
5. **AI is used in Camunda's own screening**, which they disclose. Expect automated keyword screening, so the
   CV must carry the JD's exact terms (Kubernetes, Terraform, Prometheus, Grafana, incident response).

## Why this is a strong row

- **No location work needed.** France employment through Remote.com, fully remote, no relocation and no
  entity question — the first role today where that is true from the start.
- **The must-haves are the CV's five strongest sections**, with production receipts at three employers.
- **AI-tool use is a must-have**, not a nice-to-have, and the 2026 work answers it directly.
- Large, funded, flexible employer (Flexa top-3 for flexibility), which matters against the income cliff.

## Questions to put in writing (first follow-up)

1. Is the France contract permanent, and who is the legal employer (Remote.com entity)?
2. What is the France salary band, and where does the quoted range sit inside it?
3. What is the on-call rotation and its compensation?
4. Which cloud providers are in production — EKS, GKE, both?
5. Are SLOs defined already, or would the role create them?

## Timeline

- Contacted / applied: **2026-10-09** (Ashby) · quoted €80,000–€100,000
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Screen date: — · Interview dates: — · Outcome: pending

## Outcome record

- Stage reached: Contacted
- Salary quoted: **€80,000 – €100,000** (floor equals the binding floor)
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** location cannot be the cause — France is employable through Remote.com. So a rejection would be
  **relevance** (AWS/EKS) or **compensation**. The elimination set is small and interpretable.
- What would have changed the outcome: —

## Funnel delta

Applications sent +1 (2026-10-09) · **EU-remote lane** · `tier:b` · `track:ai`. **Tenth application today**, and
the first whose location passes without any question.
