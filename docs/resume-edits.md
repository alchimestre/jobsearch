# Resume / profile edit list

Running list of fixes to apply to the CV and LinkedIn before/during outreach.
Sources: `docs/evidence-package.md` (§1 CV restructure, §6 open questions),
`research/ai-infrastructure-hiring-evidence.md` (§4 gaps), and confirmed
corrections from Vincent.

Status legend: [ ] open · [x] done

## Positioning

- [ ] Title line → "Site Reliability Engineer — moving into AI Infrastructure" (drop the "GPU workloads" claim).
- [ ] Profile paragraph → transition framing, lead with the cross-domain reliability transfer; no "compute-intensive and GPU workloads" claim.
- [ ] Delete "GPU Workloads" from skills; use "GPU exposure". Remove "Ethereum".

## Factual corrections (verify against source of truth)

- [ ] **Cometh cost reduction figure** — PDF extraction is truncated ("reducing cloud costs by 2…%"); confirm whether it is 25%.
- [ ] **Cometh end date** — extraction shows "OCT 202…"; confirm month/year.
- [ ] **Helm** — confirmed 2026-09-11 that Helm has been used. Add it explicitly to skills and to at least one experience bullet (deployment templating), since Cohere-class FDE JDs screen on it. Resume currently lists GitOps but never Helm.

## To add once evidence exists (claims lag evidence)

- [ ] `Python (in progress)` from week 1; drop the qualifier after the Python operator package is complete (~week 6).
- [ ] `Go (in progress, from week 7)`; drop the qualifier after the Go port is complete (~week 12).
- [ ] `SLO / Error Budgets` and `GPU Fleet Operations` after week-6 proof.
- [ ] Link `github.com/alchimestre/gpu-fleet-operator` from the CV header/contact once the first meaningful public commit exists (week 2).

## Channel

- [ ] Re-check every claim against what the repository actually proves before publishing; keep the CV/LinkedIn/outreach story consistent.

## Customer-facing evidence — OPEN INPUT

- [ ] **No customer-facing claim may be added until real examples are supplied.** Nothing on the CV, GitHub, or the research material evidences external customers. Asked twice (2026-09-11), not yet answered.
- [ ] Needed: institutional client work at Kiln, escalations/onboarding at Cometh, incident bridges with external partners, or external audits (ISO 27001 / HDS). Any of these, with a concrete situation, converts the weakest part of an FDE application into a strength.
- [ ] Until this is resolved: forward-deployed / FDE applications (`docs/12-week-strategy.md` §2, secondary lane ≤ ~¼ of the EU-remote/FR lane) stay capped, because their central screening question — direct customer work — cannot yet be answered truthfully at strength.

