# Blockstream — DevOps Engineer (Zurich)

**Posting (source):** https://cryptojobslist.com/jobs/devops-engineer-zurich-switzerland-at-blockstream
**Posting (employer ATS):** https://jobs.ashbyhq.com/blockstream/4bd6e458-a98f-4f3d-8c0e-a50e4735e32f · Ashby id
`4bd6e458-a98f-4f3d-8c0e-a50e4735e32f` · **Zurich** (JD: "Location: Switzerland, with focus on Zurich and Lugano")
**Org:** Blockstream — founded 2014 by Dr. Adam Back; the leading Bitcoin infrastructure company. Products:
self-custody (Jade), Bitcoin-based financial products (Liquid/Layer-2), enterprise blockchain infrastructure.
**Team:** Enterprise Products → Service & Enterprise Solutions. Works with Solution Architects, Delivery,
Product and Engineering; **client-facing delivery** ("high-touch customer engagement", "client technical
stakeholders").
**Market:** **CH** · **Tier:** **C** (Web3 infrastructure bridge — see the tier note) · **Channel:** ATS
(cryptojobslist → Blockstream Ashby) · **Track:** `web3`
**Posted:** **2026-02-10** (≈8 months old at application — see staleness note)
**Compensation:** **not published.** CH floor is **CHF 110,000** (§2). Zurich DevOps/platform at this scope
[INFERENCE] CHF 110–135k; **unverified**.
**Applied:** ✅ **2026-10-05** · **Stage:** Contacted · **Issue:** #25
**Follow-ups:** 1st due **2026-10-12 → 2026-10-14** · final **2026-10-19 → 2026-10-23**
**jobradar:** no store row — the Zurich DevOps req is absent from the local store (it holds only Blockstream's
Lugano and APAC rows). Reconcile by the Ashby id above.

## Tier note — Layer 1/2 Web3 infrastructure, `track:web3, tier:c`

Two §2 clauses disagree, exactly as recorded for 1GLOBAL (#22):

- **§2 reject list:** "Crypto-continuity roles that do not strengthen AI-infrastructure positioning." Kiln is
  already crypto; this is more crypto, and it has **no ML/AI surface** — no model serving, no pipeline, no
  registry.
- **2026-09-29 amendment:** *"Web3 infrastructure is in scope in every lane; ML/LLM is preferred but
  non-blocking."* Blockstream is a genuine Web3 **infrastructure** employer, not an application-layer crypto
  product, so the amendment admits it.

**Resolution used here:** admitted under the amendment as a **Tier C Web3 bridge**, tagged `track:web3` so
conversion stays comparable, and **not** counted toward ML-platform conversion. The clause conflict is the
same standing flag as #22 — raise it at the Friday review.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — ✅ **"3–6 years of experience in DevOps, platform engineering, SRE, or
      infrastructure operations"**; ~4 evidenced years sit inside the band
- [ ] Compensation ≥ CHF 110k (CH) — **unverified**, no band published
- [ ] On-site CH allows 8–12 week remote start from France or provides relocation assistance — **unverified and
      fails on the letter of the JD**: on-site Zurich/Lugano, **no relocation assistance and no remote-start
      language mentioned**. The role is client-facing, which makes a remote start less likely, not more
- [x] No day-one direct GPU / training / serving expertise requirement — ✅ none asked
- [ ] Has AI workload exposure AND architectural scope — ❌ **FAILS on AI exposure**: blockchain/custody/
      payment infrastructure, no ML surface at all. Architectural scope ✅ (owns infrastructure patterns,
      automation frameworks, security/compliance requirements)

**Verdict: a deliberate long-shot on two unchecked hard filters (compensation, relocation) and one explicit
failure (AI exposure).** It is logged because the craft match is unusually direct and because the Web3 lane is
in scope by amendment — not because the process is expected to convert.

## Craft read — the strongest pure-infrastructure match in the Swiss lane

| JD requirement | Candidate evidence |
|---|---|
| 3–6 yrs DevOps/platform/SRE | ✅ ~4 years continuous |
| Infra in **fintech / financial services / regulated** environments | ✅ **regulated healthcare (HDS-certified, Docaposte) and crypto infrastructure securing $8B+ assets (Kiln)**; plus ISO 27001 implementation led at Cometh |
| Cloud: **AWS preferred**, Azure/GCP a plus | ⚠️ **GCP-first**; AWS adjacent (multi-cloud work); Azure adjacent. Not an AWS-primary CV |
| CI/CD: Jenkins, GitLab CI, GitHub Actions, ArgoCD | ✅ **GitHub Actions + Drone CI**, GitOps (Flux, Argo CD) |
| IaC: Terraform, Ansible, Pulumi | ✅ **Terraform** (multi-environment), Helm |
| Scripting: Python, Bash, Go | ⚠️ Bash strong; **Python/Go remain operational, not production claims** (`CONTEXT.md` Evidence Boundaries, artifact pending) |
| Docker / Kubernetes / orchestration | ✅ core claim, incl. on-prem bare metal |
| Security hardening, secrets, encryption, access controls | ✅ **strong match** — Vault, SOPS, External Secrets, Teleport, Kyverno, Cilium |
| Monitoring/logging/alerting: Prometheus, Grafana, ELK, CloudWatch | ✅ **named-match list** incl. OpenTelemetry, Loki, Jaeger, Thanos |
| Production deployments, go-live, incident response | ✅ on-call across 40+ live networks |
| Client technical stakeholders / high-touch delivery | ⚠️ **the open customer-facing evidence gap** (unresolved since 2026-09-11, already gates the FDE/Solutions lane) |
| *Nice-to-have:* Bitcoin nodes / Lightning / blockchain ops | ✅ crypto-infrastructure operations at Kiln/Cometh (protocol networks); ⚠️ **Bitcoin nodes and Lightning specifically not evidenced** |
| Languages: English; Swiss German/German/French/Italian a plus | ✅ **French** (native) — a real plus in Lugano/Zurich delivery work |

## Risks, stated plainly

1. **Staleness.** Published 2026-02-10 and still listed. Either an evergreen requisition or a posting nobody
   closed. Application 8 months after publication is near the back of any queue.
2. **AWS-primary expectation vs a GCP-first CV.** The one technical gap that is not a language-evidence issue.
3. **Customer-facing delivery.** The role is inside a Solutions/Delivery organisation with client technical
   stakeholders in banking. The customer-facing evidence gap is currently unanswered on the CV.
4. **Relocation is unfunded on the letter of the JD**, and Switzerland is destination #3 — a *destination*
   lane, not a job-#1 market. Applying cannot start a move; only a funded offer can.
5. **Crypto continuity.** This is a third consecutive crypto-domain role on the CV trajectory and does not
   build ML-platform evidence.

## Recruiter-screen questions (ask before any screen)

1. Total compensation range for the Zurich/Lugano focus (CH floor CHF 110k)?
2. Is an 8–12 week remote start from France possible while relocating, or is relocation assistance provided?
3. Is the requisition active at 8 months old, or is this a rolling pipeline?
4. How much of the role is client-facing delivery versus internal platform ownership?
5. AWS depth: is AWS required for the estate, or is GCP/multi-cloud experience accepted?

## Timeline

- Contacted / applied: **2026-10-05** (cryptojobslist → Ashby)
- Follow-up 1 due (5–7 business days): **2026-10-12 → 2026-10-14**
- Follow-up 2 due (10–14 business days): **2026-10-19 → 2026-10-23** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** compensation and relocation are both unverified and both binding. Ask both in the first exchange;
  they are cheap questions and either one can end the process.
- What would have changed the outcome: a published band clearing CHF 110k and a funded relocation or remote
  start
