# vCluster Labs — AI Infrastructure Engineer

**Posting:** https://www.vcluster.com/careers?ashby_jid=19a7f22e-ee7d-419b-bc9e-e2fa61dff2d1#jobs
**Direct ATS link:** https://jobs.ashbyhq.com/vClusterLabs/19a7f22e-ee7d-419b-bc9e-e2fa61dff2d1
**Company:** vCluster Labs — Kubernetes tenant-isolation platform for AI clouds; 100k+ GPUs and 1M CPUs across 50+ AI clouds; $28M raised (Khosla Ventures); HQ San Francisco, remote-first, 40+ engineers
**Market:** EU-remote (locations: Remote / Australia / Germany / United States — remote-first) · **Tier:** b (AI-infrastructure vendor, customer-facing)
**Channel:** ATS (Ashby) · **Applied:** ✅ (date unrecorded)

## Compensation

| Location | Base band |
|---|---|
| Germany | **€90K – €105K** + equity + bonus |
| Australia | **A$150K – A$175K** + equity + bonus |
| United States | $140K – $165K + equity + bonus |
| Singapore | SGD 155K – SGD 175K + equity + bonus |

Clears the €80k floor for EU-remote and Berlin. **The Australia band is the reason this posting matters** —
it is an explicit Australia-eligible role at an AI-infrastructure company, which is the stated route into
that destination (`CONTEXT.md` Destination Hierarchy §4).

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — "AI Infrastructure Engineer", 5+ yrs stated
- [x] Compensation — Germany €90–105K, Australia A$150–175K
- [x] Remote-first; no relocation required to start
- [ ] No day-one GPU requirement — **FAILS**: GPU Operator, CUDA, RDMA/InfiniBand, GPU scheduling are core
- [x] AI workload exposure — direct: GPU neoclouds, AI factories, inference
- [x] Architectural scope — deployment architecture, playbook authoring, product feedback loop

## Fit assessment (written before applying)

**Strong matches**

- **Production Kubernetes at scale** — 4 years across three companies, multi-zone and multi-environment
- **Bare-metal networking** — MetalLB and Cilium on-premise at Docaposte (this JD asks for CNI, load
  balancing, connectivity diagnosis; that is the exact evidence)
- **Observability and incident response** — the "Operational Agility" requirement is evidenced
- **Customer-facing deployment at depth** — the role is pre-sales proof-of-value plus hands-on build;
  Vincent's infrastructure background is the right shape for it
- **Ceph exposure** — the JD names Ceph/Rook/Weka/Longhorn; `docs/tooling-inventory.md` records Ceph as
  used (unplaced employer)

**Hard gaps — do not claim these**

| Requirement | Evidence status |
|---|---|
| NVIDIA GPU Operators, CUDA tooling | ❌ none. CV says "GPU exposure" only |
| RDMA / InfiniBand | ❌ none |
| Bare-metal GPU node provisioning | ❌ none (bare-metal K8s yes, GPU nodes no) |
| CSI drivers / persistent volume depth | ❌ none recorded |
| Distributed storage (Ceph/Rook/Weka/Longhorn) | ⚠️ Ceph used, depth unknown |
| 5+ years production Kubernetes | ⚠️ 4 years (Dec 2021 – Jan 2026 continuous) |
| Inference serving, GPU scheduling, LLM deployment | ❌ none (the artifact targets serving, no GPU) |

**The honest read:** this is a GPU-infrastructure role, and the candidate's GPU evidence is one line on a
CV. `CONTEXT.md` explicitly excludes GPU fleet operations and the vendor tier from the primary lane for
this reason. The networking, Kubernetes, and customer-deployment halves are genuinely competitive; the
GPU half is not. Expect the GPU depth to be the first screen question.

**Also note:** this JD contradicts an assumption in ticket 06 / the second amendment — the benchmark's
GPU-vendor weighting was judged tier-specific noise, but here is a well-funded AI-infra vendor hiring
remotely with an Australia band. That does not un-demote the vendor tier, but it is the kind of role the
secondary lane was meant to catch.

## Recruiter-screen answers (ask before any screen)

1. Is this role open to candidates resident in France (EU-remote), or tied to the listed countries?
2. For the Australia option — does vCluster sponsor visas, or must the candidate already hold work rights?
3. How much GPU-depth is required on day one versus learned on the job?
4. Is the pre-sales / proof-of-value component customer-facing travel, and how often?
5. What is the on-call expectation for field deployments?

## Timeline

- Applied: ✅ (date unrecorded)
- Follow-up windows: not computable, the application date was not recorded
- Screen date: —
- Outcome: —

## Outcome record

- Stage reached: Contacted (project board #5)
- Rejection reason: —
- What would have changed the outcome: —

## Notes

- **Australia angle:** if pursued, ask question 2 early. An Australia-eligible remote role that requires
  pre-existing work rights is not a route into the country, and that is the whole point of applying.
- **Visa sponsorship is unverified [INFERENCE].** No Australian immigration research was done this
  session. Before investing, verify: which visa subclasses an employer can sponsor, and whether the role
  qualifies.
- Compare against the vCluster board for adjacent roles with lower GPU depth — the same company has five
  Engineering roles (Staff Software Engineer Germany €75–145K, Senior Backend €80–115K, Engineering Tech
  Lead vNode) that may fit the platform profile better than the GPU-facing one.
