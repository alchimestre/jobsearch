# Figma CV — exact edit sheet

Apply these in the Figma file (`CV 3_white`). Left = current text, right = replacement.
Run `figma-apply.js` in the Scripter plugin to do all of it automatically, or edit by hand.

The `find` strings below were verified against the export's own text layer (`resume_v3.pdf`
`/ActualText` runs plus the extractor-readable bullets), and the script was executed against
those real node texts: 8 nodes change, and the Bitgen bullet, the 25% bullet, the date ranges,
and the name are deliberately untouched.

Script is two-step: run once as-is (`DRY_RUN = true`, reports only), then set
`DRY_RUN = false` and run again to apply. Undo is Cmd+Z.

Layer/page hints: the file is a 2-page layout (page 1 = CV, page 2 = the skills/core-competencies block). Text may be split across several nodes — if a `find` below does not match, select just that text block and re-run (the script scopes to the selection when something is selected).

---

## 1. Title

| Find | Replace |
|---|---|
| `Site Reliability & Platform Engineer` | `Site Reliability Engineer — moving into AI Infrastructure` |

## 2. Location line (under the name)

| Find | Replace |
|---|---|
| `Aix-en-Provence, France` | `Aix-en-Provence, France · Open to EU-remote, Berlin, Switzerland` |

## 3. Profile paragraph

**Replace the whole paragraph:**

> Infrastructure-focused SRE building scalable platforms for compute-intensive and GPU workloads. Combines deep expertise in distributed systems, multi-environment Kubernetes, and high-availability architecture. Driven by optimizing performance, reducing cloud costs, and hardening production systems.

with:

> Production SRE with 4 years operating high-availability distributed infrastructure across regulated healthcare, crypto, and multi-protocol systems. Moving into AI infrastructure — bringing Kubernetes reliability, observability, and cost-aware platform operations to the compute and serving layers AI workloads depend on.

Why: removes the "compute-intensive and GPU workloads" claim (unproven) and replaces it with the transition framing. Lead with the cross-domain transfer, which is the actual differentiator.

---

## 4. Kiln — Site Reliability Engineer (Jun 2024 – Jan 2026)

Add **Helm** to bullet 3 and rewrite bullet 6.

| Find | Replace |
|---|---|
| `Designed and maintained Infrastructure-as-Code (Terraform) across multi-environment Kubernetes clusters` | `Designed and maintained Terraform IaC and Helm charts across multi-environment Kubernetes clusters` |
| `Collaborated with engineering and product teams to translate infrastructure constraints into scalable architectural decisions.` | `Translated infrastructure constraints into scalable architectural decisions with engineering and product teams` |

Bullets 1, 2, 4, 5 unchanged (punctuation normalized, no trailing period).

## 5. Cometh — Site Reliability Engineer (Feb 2023 – **Oct 2023**)

Confirmed 2026-09-11: cost figure is **25%**, end date **Oct 2023**.

| Find | Replace |
|---|---|
| `Managed multi-zone Kubernetes clusters on GCP in a production environment` | `Managed multi-zone Kubernetes clusters on GCP in production, deploying services with Helm charts` |
| `Improved system observability (Prometheus, Grafana, OpenTelemetry, ELK) and reduced MTTR` | *(unchanged — already correct)* |
| `Optimized infrastructure architecture, reducing cloud costs by 25%` | *(unchanged — 25% confirmed, no longer truncated)* |
| `Reduced CI build times by 60% through pipeline optimization and container standardization` | *(unchanged)* |
| `Led ISO 27001 security implementation and incident response processes` | *(unchanged)* |

If the end date in the Figma file reads anything other than `OCT 2023`, set it to `OCT 2023`.

## 6. Docaposte / Bitgen

No changes. Docaposte supports the regulated-environment differentiator; Bitgen stays as entry-level Kubernetes evidence.

## 7. Skills & Technologies

The technical list is a **single text node** (`Kubernetes · Terraform · GCP · Linux · Distributed Systems · … · GPU Workloads · Ethereum`). Three changes in it:

| Find | Replace |
|---|---|
| `Kubernetes · Terraform · GCP` | `Kubernetes · Terraform · Helm · GCP` |
| `GPU Workloads · Ethereum` | `Python (in progress)` |

Result:

```
Kubernetes · Terraform · Helm · GCP · Linux · Distributed Systems · High Availability · Scalability · Docker · CI/CD · GitOps · Prometheus · Grafana · OpenTelemetry · ELK · PostgreSQL · Performance Tuning · Capacity Planning · SecOps · ISO 27001 · Python (in progress)
```

Net effect: **Helm** added (Cohere-class JDs screen on it), **Ethereum** and the **GPU Workloads ownership claim** removed, `GPU exposure` retained on the second line below the technical list, `Python (in progress)` added.

`Python (in progress)` is honest today: the operator package exists at `github.com/alchimestre/gpu-fleet-operator`. Drop the qualifier after the week-6 gate. Do **not** add Go until the week-7 conditional starts.

Keep the second line as-is — `… · SecOps · ISO 27001 · HDS · GPU exposure` — this is where the "GPU exposure" wording lives now.

## 8. Spelling

| Find | Replace |
|---|---|
| `Application Developper Degree` | `Application Developer Degree` |

## 9. Project block (optional — add only if the layout has room)

> **GPU Fleet Operator** — Kubernetes operator for GPU fleet health and workload placement (Python/Kopf · CRD · Prometheus). Implements a scheduling/health decision core, simulated and DCGM-style GPU health sources, and cordon/drain remediation against a custom `GpuNode` resource. Defines SLIs and error-budget burn for fleet health checks and scheduling latency.

The GitHub link goes in the contact line once the repo is pushed (it has no remote yet — pending owner action). Until then, either omit the link or omit this block.

---

## Held back deliberately

| Item | Why | Unblock |
|---|---|---|
| `Go (in progress)` | Port has not started | Week 7, only if the search is on track |
| `SLO / Error Budgets`, `GPU Fleet Operations` | Claims lag evidence | Week-6 Python milestone |
| Any customer-facing line (FDE/solutions framing) | No evidence exists; asked 2026-09-11, unanswered | Supply a concrete example: institutional clients at Kiln, client onboarding/escalations at Cometh, or external audits (ISO 27001 / HDS) |

## Note on the export itself

The current PDF is a 2-column Figma export, and its text extraction interleaves columns — extracted bullets from Cometh and Docaposte merge, and values split across table cells (`60%`, `25%`). That is the same reading an ATS parser gets. If applications go to an ATS rather than a human, submit a single-column version (`resume/resume.md` is written for that) rather than the Figma export.
