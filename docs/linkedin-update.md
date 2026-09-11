# LinkedIn update — copy blocks

Companion to `docs/resume-edits.md` and `docs/evidence-package.md` §2. Same honesty rules as the CV:
no completed Python/Go claim, no GPU-fleet ownership, **no project claim** (the operator project is
set aside), and nothing customer-facing until examples are supplied.

---

## 1. Headline (220 char limit)

```
Site Reliability Engineer → AI Infrastructure | Kubernetes · Observability · Cost-Aware Platform Operations
```

Alternative if you want the market visible:

```
Site Reliability Engineer → AI Infrastructure | Kubernetes · Terraform · Helm | Open to EU-remote & Berlin
```

The arrow signals the transition without claiming current AI expertise. Keep "Site Reliability
Engineer" first — it is the title recruiters search.

## 2. About

> I'm a production SRE specialising toward AI infrastructure. Over the past four years I've operated
> high-availability distributed systems in regulated healthcare (HDS), crypto infrastructure
> ($8B+ in digital assets secured), and multi-protocol environments — always making platforms more
> observable, resilient, and cost-aware. My next step is bringing that reliability discipline to the
> compute and serving layers AI workloads run on.
>
> I move fast across domains. From stabilising Kubernetes in a certified healthcare environment to
> securing $8B+ in digital assets at Kiln, I've repeatedly entered unfamiliar infrastructure domains
> and reached production-grade reliability within months. That transfer pattern is the thing I bring
> to AI infrastructure: Kubernetes at scale, Terraform and Helm, observability with Prometheus and
> OpenTelemetry, and cost-aware capacity decisions.
>
> Since January 2026 I've been working independently: product-idea proofs of concept in
> domain-specific AI assistance and orchestration, and research in history and linguistics that is
> largely AI-assisted prosopography. I'm now looking for SRE and platform roles at AI-native
> companies — EU-remote from France, or Berlin with relocation support — where the work has real
> architectural scope: owning failure modes, capacity, and the reliability of the platform that
> hosts models, rather than runbook-only operations.

**Changes from the prototype:** paragraph 3 no longer says "currently building a GPU fleet Kubernetes
operator" (the project is set aside, and the claim would be false). It now states what Vincent
actually did in 2026, in his own terms. Switzerland moved out of the live ask — it is a medium-term
destination, not a current application lane.

**Wording fixes to your blurb before it goes on the profile:**

| Yours | Use instead | Why |
|---|---|---|
| `IA` | `AI` | French abbreviation; on an English-language profile it reads as a typo to recruiters |
| `PoCs` | `proofs of concept (PoCs)` | spell it out once, then the short form is fine |
| `AI-assisted Prosopography` | `AI-assisted prosopography (structured study of historical people and their networks)` | "prosopography" is invisible to keyword search and unknown to most recruiters; the gloss costs nothing |

Do not expand any of it beyond what you wrote — no model names, no frameworks, no "built a RAG
pipeline" unless you actually did.

## 3. Experience (mirror the CV exactly)

- **Site Reliability Engineer — Kiln**, Jun 2024 – Jan 2026
- **Site Reliability Engineer — Cometh**, Feb 2023 – Oct 2023
- **DevOps Engineer — Docaposte**, Jun 2022 – Feb 2023
- **Junior DevOps Engineer — Bitgen**, Dec 2021 – Apr 2022

Bullets: copy from `resume/resume.md` verbatim. Consistency between CV, LinkedIn, and outreach is a
screening signal — do not let LinkedIn drift to stronger wording.

Add **Helm** to the Kiln and Cometh entries (same two bullets that changed on the CV).

## 4. Skills tags (endorsement-generating + search-discoverable)

Add these to the profile's Skills section, in this order:

```
Kubernetes · Terraform · Helm · Site Reliability Engineering · Distributed Systems · Prometheus · Grafana · OpenTelemetry · Linux · Docker · CI/CD · GitOps · Google Cloud Platform (GCP) · High Availability · Incident Response · ISO 27001
```

Do **not** add: Python, Go, GPU, CUDA, MLOps, PyTorch. None are evidenced.

## 5. Profile settings checklist

- [ ] Custom URL: `linkedin.com/in/vincent-loupmon` (matches `github.com/alchimestre` usage loosely — pick one handle style and stay consistent).
- [ ] Location: `Aix-en-Provence, France`; keep the open-to-work preference set to include Berlin (on-site/hybrid) and remote.
- [ ] Language: profile in **English** (target roles are English-first AI companies).
- [ ] Contact info: email `vincentloupmon+pro@protonmail.com`, GitHub `github.com/alchimestre`. Phone optional.
- [ ] Turn **off** "Share profile updates" around edits if you don't want a broadcast of every tweak.
- [ ] Featured section: leave empty until something exists to link. Do not feature the operator repo.
- [ ] Banner/photo: professional headshot is worth it; banner is optional.

## 6. Still blocked (unchanged)

| Item | Unblock |
|---|---|
| Any customer-facing wording (deployment, solutions, FDE framing) | Supply a concrete example: institutional clients at Kiln, client onboarding/escalations at Cometh, or audits (ISO 27001 / HDS) |
| Python / Go / GPU skills tags | A real artifact with the language actually in it |
| A "Featured" project link | A pushed public project (the operator repo has no remote and is set aside) |
| Lifting `Independent Work` from application-layer to infrastructure evidence | Confirm one fact: did any PoC run a **self-hosted model** (Ollama/llama.cpp/vLLM/TGI) or get **deployed** (containers, cloud, k8s)? If yes, that is inference-infrastructure evidence and it can be said plainly |

## 7. The Jan 2026 → now gap — answered

The gap is now filled by real activity, so it stops being a weakness and becomes evidence of
self-directed AI work. Use **one sentence everywhere** — LinkedIn About, the CV `Independent Work`
block, and any outreach message:

> Since January 2026 I've been working independently: product-idea proofs of concept in
> domain-specific AI assistance and orchestration, and AI-assisted research in history and
> linguistics.

Rules: never leave it unexplained in a first screen; never inflate it (no stack, no "shipped", no
"deployed" until true); keep the dates identical to the CV.

## 8. Projects and interests

LinkedIn → **Add section → Projects** (under Accomplishments). Two entries, no links until something
is public:

| Project | Description |
|---|---|
| Domain-specific AI assistance & orchestration (PoCs) | Product-idea proofs of concept exploring domain-specific AI assistance and orchestration. 2026 – present. |
| AI-assisted prosopography research | Independent research in history and linguistics, largely AI-assisted prosopography — the structured study of historical people and their networks. 2026 – present. |

**Music production:** LinkedIn only — under **Interests**, or one line in About. Keep it off the CV.

If a PoC ever gets a public repo or write-up, the link goes into **Featured** and onto the CV at the
same time — never one without the other.
