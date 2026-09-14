# Resume / profile edit list

Running list of fixes to apply to the CV and LinkedIn before/during outreach.
Sources: `docs/evidence-package.md` (§1 CV restructure, §6 open questions),
`research/ai-infrastructure-hiring-evidence.md` (§4 gaps), and confirmed
corrections from Vincent.

Status legend: [ ] open · [x] done

Apply path: the CV lives in Figma (`CV 3_white`, 2-column export). Content now exists in
`resume/resume.md` (canonical, ATS-shaped); exact Figma edits are specified in
`resume/figma-update.md` and can be applied in one run by `resume/figma-apply.js`
(Scripter plugin).

## Positioning

- [x] Title line → "Site Reliability Engineer — moving into **ML Platform / MLOps**" (drop the "GPU workloads" claim; second amendment 2026-09-11 re-centred the lane from GPU-fleet to ML platform / MLOps).
- [x] Profile paragraph → transition framing, lead with the cross-domain reliability transfer; no "compute-intensive and GPU workloads" claim.
- [x] Delete "GPU Workloads" from skills; use "GPU exposure". Remove "Ethereum".

## Second amendment — positioning (2026-09-11)

- [x] Strategy, CONTEXT, CV, Figma sheet, and LinkedIn re-centred on **ML platform / MLOps**; `AI infrastructure` kept as the umbrella keyword; GPU/vendor tier demoted to a secondary lane. Rationale: ticket 02's market map, not the GPU-vendor-sampled benchmark.
- [x] Evidence project replaced: `ml-platform-on-k8s` (spec: `docs/ml-platform-project.md`), superseding `gpu-fleet-operator`.
- [ ] Add `Python (in progress)` / ML-lifecycle claims only when the week-6 artifact proves them.

## Factual corrections (verify against source of truth)

- [x] **Cometh cost reduction figure** — confirmed 2026-09-11: **25%**.
- [x] **Cometh end date** — confirmed 2026-09-11: **October 2023**.
- [x] **Helm** — confirmed used at **Kiln and Cometh** (2026-09-11). Added to skills and to one bullet per role (deployment templating).
- [x] **Name** — confirmed 2026-09-11: `Vincent Loupmon` (v2's "Loupmont-Peyrat" was the older variant). No header change needed.
- [ ] **Kiln deployment tooling** — supplied by Vincent 2026-09-11, **not yet on the CV**. Split confirmed 2026-09-11:
  - **Deployed / operated:** `nginx`, `Traefik` (ingress/reverse proxy), `Velero` (backup/restore), `Teleport` (access management, identity-aware proxy), `cert-manager` (TLS automation), `Flux` (GitOps delivery).
  - **Used, not deployed:** `Loki` (log aggregation), `Argo CD`, `Vault` (secrets). Do not write "deployed" for these.
  - `Flux` is the GitOps tool actually operated at Kiln; `Argo CD` was used, not deployed. Both close the gap where the CV claims "GitOps practices" without naming a tool.

## Independent work (2026)

- [x] `Independent Work` block added to `resume/resume.md`, `resume/ats/resume.html`, and the Figma sheet, from Vincent's own LinkedIn blurb — no stack, deployment, or link claims.
- [ ] Confirm the date range (`2026 – present` is an assumption on the Jan-2026 gap).
- [ ] Optional upgrade: if a PoC ran a self-hosted model or was deployed, say so — that converts application-layer prototyping into inference-infrastructure evidence.
- [ ] Music production stays off the CV (LinkedIn Interests only).

## To add once evidence exists (claims lag evidence)

- [ ] `Python (in progress)` from week 1; drop the qualifier after the ML-platform artifact is complete (~week 6).
- [ ] `Go (in progress, from week 7)`; drop the qualifier after the Go component is complete (~week 12).
- [ ] `SLO / Error Budgets` and ML-lifecycle items (pipelines, registry, serving, drift) after week-6 proof from `ml-platform-on-k8s`.
- [ ] Link `github.com/alchimestre/ml-platform-on-k8s` from the CV header/contact once the first meaningful public commit exists (week 1–2).

## Channel

- [ ] Re-check every claim against what the repository actually proves before publishing; keep the CV/LinkedIn/outreach story consistent.

## Customer-facing evidence — OPEN INPUT

- [ ] **No customer-facing claim may be added until real examples are supplied.** Nothing on the CV, GitHub, or the research material evidences external customers. Asked twice (2026-09-11), not yet answered.
- [ ] Needed: institutional client work at Kiln, escalations/onboarding at Cometh, incident bridges with external partners, or external audits (ISO 27001 / HDS). Any of these, with a concrete situation, converts the weakest part of an FDE application into a strength.
- [ ] Until this is resolved: forward-deployed / FDE applications (`docs/12-week-strategy.md` §2, secondary lane ≤ ~¼ of the EU-remote/FR lane) stay capped, because their central screening question — direct customer work — cannot yet be answered truthfully at strength.

