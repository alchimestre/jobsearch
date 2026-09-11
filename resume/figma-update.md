# Figma CV — exact edit sheet

Apply these in the Figma file **"Resume"** (`figma.com/design/rETT9pR5zH0ehzPa8I184J`), frame
`CV 3_white` on `Page 1`. Left = current text, right = replacement.
Run `resume/figma-apply.js` in the Scripter plugin to do all of it automatically, or edit by hand.

The `find` strings were verified against the **live document** via the Figma API (read-only
`file_content:read` token at `~/.figma-token`), and the script was executed against those same
node texts. Helm is already present in the skills node, so the script no longer adds it.

The script now applies by default (`DRY_RUN = false`, `SCOPE = "document"`), prints a per-rule
report in the Scripter console plus a toast, and is idempotent — re-running reports 0 changes.
Undo is Cmd+Z.

### Node map (from the live file)

| Node | Layer | Content |
|---|---|---|
| `0:73` | Site Reliability & Platform Engineer | title line |
| `2:3` | Aix-en-Provence, France | location |
| `0:69` | Infrastructure-focused SRE… | profile paragraph |
| `0:41` | job description (Kiln) | 6 bullets, one text node |
| `0:47` | job description (Cometh) | bullets, one text node |
| `0:53` | job description (Docaposte) | bullets — untouched |
| `0:59` | job description (Bitgen) | bullets — untouched |
| `0:30` | skills | technical skills, one text node |
| `0:33` | skills | core competencies — untouched |
| `0:17` | degree description | AFPA degree (spelling) |
| `0:72` | name | `Vincent Loupmon` — correct, untouched |

Text may still be split across nodes if the file is edited again — if a `find` does not match,
select just that text block and re-run with `SCOPE = "selection"`.

---

## 1. Title

| Find | Replace |
|---|---|
| `Site Reliability & Platform Engineer` | `Site Reliability Engineer — moving into ML Platform / MLOps` |

## 2. Location line (under the name)

| Find | Replace |
|---|---|
| `Aix-en-Provence, France` | `Aix-en-Provence, France · Open to EU-remote, Berlin, Switzerland` |

## 3. Profile paragraph

**Replace the whole paragraph:**

> Infrastructure-focused SRE building scalable platforms for compute-intensive and GPU workloads. Combines deep expertise in distributed systems, multi-environment Kubernetes, and high-availability architecture. Driven by optimizing performance, reducing cloud costs, and hardening production systems.

with:

> Production SRE with 4 years operating high-availability distributed infrastructure across regulated healthcare, crypto, and multi-protocol systems. Moving into ML platform / MLOps — bringing Kubernetes reliability, observability, and cost-aware platform operations to the platform that builds, ships, and serves models.

Why: removes the "compute-intensive and GPU workloads" claim (unproven) and replaces it with the transition framing. Lead with the cross-domain transfer, which is the actual differentiator. Second amendment (2026-09-11): the target lane is ML platform / MLOps, not GPU fleet operations — see `docs/12-week-strategy.md` §1.

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

The technical list is a **single text node** (`0:30`), and it **already contains Helm** (added since the last export). Its tail is:

```
… · ISO 27001 · GPU Workloads · Ethereum
```

| Find | Replace |
|---|---|
| `GPU Workloads · Ethereum` | `GPU exposure` |

Result tail: `… · ISO 27001 · GPU exposure`.

Net effect: the crypto keyword `Ethereum` is dropped, and the `GPU Workloads` ownership claim is downgraded to the honest `GPU exposure`. Nothing else changes — in particular **no `Python` or `Go` entry**, since those were tied to the operator project, which is set aside.

## 8. Spelling

| Find | Replace |
|---|---|
| `Application Developper Degree` | `Application Developer Degree` |

## 9. Independent Work — new block (manual insert; the script cannot create nodes)

Add a section between **Experience** and **Skills & Technologies**, reusing the existing section-heading style:

**Heading:** `Independent Work`
**Date line:** `2026 – present`

```
Product-idea proofs of concept in domain-specific AI assistance and orchestration
Independent research in history and linguistics, largely AI-assisted prosopography
```

Source: Vincent's own LinkedIn blurb (2026-09-11). Wording cleaned only — `IA` → `AI`, `PoCs` → `proofs of concept`, nothing added. Do **not** add a stack, a deployment claim, or a link: none were confirmed.

Deliberately excluded: **music production** (it belongs on LinkedIn, not on an SRE CV).

`2026 – present` is an assumption — the out-of-work gap runs Jan 2026 → now. Correct the dates if they differ.

## Held back deliberately

| Item | Why | Unblock |
|---|---|---|
| `Go (in progress)` | No evidence | Only after a Go project actually exists |
| `SLO / Error Budgets`, ML-lifecycle items (pipelines, registry, serving, drift) | Claims lag evidence | The week-6 artifact (`docs/ml-platform-project.md`) |
| Any customer-facing line (FDE/solutions framing) | No evidence exists; asked 2026-09-11, unanswered | Supply a concrete example: institutional clients at Kiln, client onboarding/escalations at Cometh, or external audits (ISO 27001 / HDS) |
| Any project section / repo link | Nothing public exists yet; the old operator project is set aside | `ml-platform-on-k8s` spec: `docs/ml-platform-project.md`. Link at week 1–2 once the repo is public; add the CV project section at week 6, when the claims are provable |

## Note on the export itself

The current PDF is a 2-column Figma export, and its text extraction interleaves columns — extracted bullets from Cometh and Docaposte merge, and values split across table cells (`60%`, `25%`). That is the same reading an ATS parser gets. If applications go to an ATS rather than a human, submit a single-column version (`resume/resume.md` is written for that) rather than the Figma export.
