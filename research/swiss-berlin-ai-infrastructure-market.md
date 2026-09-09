# Switzerland + Berlin AI Infrastructure Engineer Market

Research note for ticket `02-map-target-market` (Wayfinder map: AI Infrastructure job search).
Scope: employer segments, named companies, role-title aliases, hiring locations, language expectations, recurring requirements — Switzerland 60% / Berlin 40%, under the tiered employer thesis (AI-infra vendors first → model labs selectively → AI product companies only where the role owns substantive AI infrastructure).

- **Author/date:** SwissBerlinMarket worker agent, 2026-09-09.
- **Method:** primary-source reads of employer/government pages; one secondary job board (AI Dev Jobs) read directly for live-posting discovery; bounded web search (engine walled mid-session — see Limitations).
- **Legend:** **[VERIFIED]** = directly read from the cited primary source on 2026-09-09. **[OBSERVED]** = seen in a cited live listing/aggregator on 2026-09-09 (secondary). **[INFERENCE]** = reasoned from context, not directly verified. Source URLs accompany every material claim.

---

## 1. Candidate profile driving the "realistic" filter (from `resume_v3.pdf`)

- SRE / platform engineer, Aix-en-Provence, France; EU (French) national → **no work permit needed in either Switzerland or Germany** (see §5, §8).
- ~3.5 y total: SRE @ Kiln (crypto staking, multi-network distributed infra, Terraform/K8s multi-env, hardening) 2024–2026; SRE @ Cometh (GCP multi-zone K8s, observability, cost reduction) 2023; DevOps @ Docaposte (regulated healthcare/HDS) and @ Bitgen (Ethereum on K8s) 2021–2023.
- Stack: Kubernetes, Terraform, GCP, Linux, Docker, CI/CD, GitOps, Prometheus/Grafana/OpenTelemetry/ELK, PostgreSQL; resume claims "GPU workloads" and compute-intensive-platform focus.
- Resume shows no German language line and no formal ML/LLM training-stack credentials. Implication used below: French + professional English assumed; German level unknown; PyTorch/training-orchestration/inference-serving depth unproven on paper.

---

## 2. Headline findings

1. **Zurich is the Swiss AI-infrastructure center of gravity.** The named AI-infra employers verified live in Switzerland cluster in Zurich (Google SRE/ML roles, Anthropic Zurich, Skydio Zurich, IBM Research Zurich-Rüschlikon) plus the national compute estate (CSCS/Swiss AI Initiative "Alps", Lugano + Zurich). Geneva/Lausanne are secondary; Lausanne matters via EPFL/ETH-domain AI (Swiss AI Initiative, SDSC lineage). **[VERIFIED sources §3]**
2. **The Swiss market is thinner in pure "AI-infra vendor" headquarters than the thesis implies.** Global R&D outposts of hyperscalers/labs + national AI supercomputing + a handful of young GPU/cloud-infra startups carry most of the load. **[INFERENCE** synthesized from §3 sources**]**
3. **Berlin's AI-infrastructure demand is mostly *in-house ML platform / MLOps* inside product companies and AI scale-ups** (Inceptive, Zeta Global observed live; Zalando/Delivery Hero/HelloFresh class by market convention), with a defense-AI cluster (Helsing) that skews research-heavy. Berlin has no Alps-scale national compute anchor and fewer AI-infra vendor HQs than Zurich. **[OBSERVED §7]** **[INFERENCE** for the market-shape conclusion**]**
4. **EU freedom of movement makes relocation logistics trivial for this candidate in both markets**: no visa or work permit; register locally after arrival. **[VERIFIED §5, §8]**
5. **English is the working language at every employer verified** (CSCS: "our working language is English"; Google/Anthropic/IBM postings are English-language). German appears where domestic/SME employers are involved, which is a *smaller* share of the realistic AI-infra target list in Zurich and Berlin. **[VERIFIED]** + **[INFERENCE** for the general claim**]**
6. Role-title aliases are numerous; title matching alone is a weak filter — responsibility matching per CONTEXT.md is the operative rule. **[INFERENCE]**

---

## 3. Switzerland — employer segments and named employers (60% effort)

### 3.1 National AI compute / research-domain engineering (public, ETH-domain)

- **CSCS (Swiss National Supercomputing Centre)** — operates **Alps**, one of the world's leading AI supercomputers, "over 10'000 GH200 GPUs" (NVIDIA Grace Hopper), built/run "in collaboration with engineers at CSCS". **[VERIFIED]** https://www.swiss-ai.org/ and https://www.cscs.ch/about/working-at-cscs
  - Hiring reality (read directly): ~140 employees, 25+ nationalities, **working language English** (local language Italian; Lugano site); live openings at read time: *Systems Engineer – Platform Automation* (2026-05-29), *DevOps Engineer* (2026-05-28), Facility Manager (2026-09-01); applications via jobs.ethz.ch. A **Zurich** presence page exists (ETH Zurich domain jobs portal; ETH AI Center partnership). **[VERIFIED]** https://www.cscs.ch/about/working-at-cscs, https://www.cscs.ch/about/working-at-cscs/working-in-zurich
  - Fit note: platform-automation/DevOps titles map cleanly onto an SRE profile; salary is public-sector, below Zurich market. Realistic target.
- **Swiss AI Initiative (ETH Zurich + EPFL)** — the Swiss National AI Institute; Alps compute grants; >800 researchers incl. 70 AI professors across 10+ institutions; **Swisscom listed as strategic partner**. Hires platform/ML engineers through ETH/EPFL channels (ETH AI Center, EPFL AI Center). **[VERIFIED]** https://www.swiss-ai.org/ (4th Large Project Call window observed: 2026-08-03 → 2026-09-14)
- **IBM Research Europe – Zurich (Rüschlikon/Zurich)** — AI + quantum research lab with ETH collaboration. Live postings observed (read directly): *Research Engineers / Research Scientists – Next-Generation Data Systems* (systems engineering + systems research focus), GPU-focused internships (*GPU Accelerated Data Structures and Algorithms*; *cuDF/Velox on GPUs* thesis). **[VERIFIED]** https://www.zurich.ibm.com/careers/ and https://www.zurich.ibm.com/careers/2025_016.html
  - Fit note: overwhelmingly research/thesis/internship postings; few classic SRE lines. Low-yield for a senior infra profile unless a systems-engineering research staff role opens — treat as selective.

### 3.2 Model labs / AI frontier companies with Zurich engineering presence (selective tier)

- **Anthropic Zurich** — live posting observed: *Research Engineer, Production Model Post-Training*, Zurich, hybrid, ~6 months old at read time, tagged distributed-systems / fine-tuning / RL. **[OBSERVED]** https://aidevboard.com/job/research-engineer-production-model-post-training-d9e4edfe ; company hiring policy verified directly: values engineering backgrounds ("apply as an engineer"), engineers co-author research, visa sponsorship offered, mostly Bay Area with periodic in-office cadence. **[VERIFIED]** https://www.anthropic.com/careers
  - Fit note: ambitious but legitimate "model lab selectively" target — production training/post-training infrastructure is exactly AI-infrastructure work; competition is global and PhD-adjacent. Expect strong training-stack evidence required. **[INFERENCE]**
- **Google Zurich** — Zurich is a major Google engineering office (careers location page live; frequently described as Google's largest engineering site outside the US **[INFERENCE**, unverified directly this session**]**). Live SRE postings for Switzerland observed via official-role mirrors on ch.linkedin.com at search time: *Senior Staff Systems Engineer, Site Reliability Engineering* requiring "Experience with Machine Learning Infrastructure"; *Software Engineer, SRE – YouTube ML*; *Staff SWE, SRE*. **[OBSERVED]** https://ch.linkedin.com/jobs/view/senior-staff-systems-engineer-site-reliability-engineering-at-google-4296077987 ; https://ch.linkedin.com/jobs/view/software-engineer-site-reliability-engineering-youtube-ml-at-google-4380469874 ; canonical channels: https://www.google.com/about/careers/applications/locations/zurich/ , https://sre.google/careers/
  - Fit note: SRE-on-ML-infrastructure is a direct translation of the candidate's SRE core + a genuine AI-infra role. High bar (Staff/Senior-Staff observed); expect ML-infra depth questions. Realistic target at the senior end, not entry.
- **NVIDIA / Meta Zurich presence: NOT verified this session** (queries blocked by search wall). **[INFERENCE]**: NVIDIA runs a Zurich site and Meta has Zurich AI research — do not rely on this without re-verification at application time.

### 3.3 AI-infra / deep-tech vendors and startups, Zurich area (tier-1 vendors)

Live postings observed on AI Dev Jobs (aggregator, Zurich filter, accessed 2026-09-09 — 5 AI-infrastructure postings at 4 employers; board crawl ≠ market size): **[OBSERVED]** https://aidevboard.com/location/zurich/ai-infrastructure

- **Skydio Zurich** — *Autonomy Engineer – ML & DL Infrastructure*; *Deep Learning Infrastructure*; *Deep Learning Model Acceleration* (mid-level, ~3 months old; board tags remote). Drone-autonomy company with a Zurich engineering hub. Deep-learning-infrastructure team = AI-infra ownership inside an AI product company → tier 3 under the thesis. Requires computer-vision/training-pipeline depth. **[OBSERVED]** same board URL.
- **Anthropic Zurich** — see §3.2 (counted there).
- **Loki Robotics (Zurich)** — *Senior AI Infrastructure Engineer* posting surfaced at search time: "build and operate the training infrastructure … containerized deployments and cloud GPU." **[OBSERVED, secondary]** https://www.linkedin.com/jobs/view/4436766256/ (LinkedIn listing; company page not verified)
- **Lyceum (Zurich)** — *GPU Platform Engineer*, described as "EU-sovereign cloud GPU platform… develop our software stack for GPU workloads" (customer-facing + hands-on). **[OBSERVED, secondary]** https://www.learn4good.com/jobs/zurich/switzerland/info_technology/5296242706/e/
  - Fit note: Lyceum/Loki-class GPU-cloud startups are the closest thing to "AI infrastructure vendor first" in Switzerland; small teams, broad scope — candidate's IaC/K8s/SRE background fits, but expect GPU-stack hands-on expectations (CUDA-adjacent tooling, cluster schedulers). **[INFERENCE]**
- **Swiss enterprise cloud/telecom (Swisscom as Swiss AI Initiative strategic partner)** — plausible *enterprise platform* lane for AI infra (AI cloud, GPU capacity, sovereign compute). **No verified job postings this session**; Swisscom-class roles may require German. **[INFERENCE]** https://www.swiss-ai.org/ (partner list)

### 3.4 Hiring locations — Switzerland

- Zurich (dominant: Google, Anthropic, Skydio, IBM Rüschlikon suburb, ETH-domain Zurich office) **[VERIFIED §3]**; Lugano (CSCS) **[VERIFIED]**; Lausanne/EPFL domain (Swiss AI Initiative) **[VERIFIED partner org]**; Geneva secondary (UN/ICAIN hub, less AI-infra engineering observed). **[INFERENCE]**

### 3.5 Language expectations — Switzerland

- English is the verified working language at CSCS and the de facto language of every English-language posting observed (Google, Anthropic, IBM, Skydio). **[VERIFIED/OBSERVED]**
- German (Swiss-German region) will matter at domestic SMEs/enterprise and possibly Swisscom; French in Romandie (Lausanne/Geneva) — candidate's French is an asset there. Resume shows no German → filter for English-first employers or German-not-required postings. **[INFERENCE]**

### 3.6 Swiss immigration for this candidate

- France is an EU/EFTA country covered by the Agreement on the Free Movement of Persons; residence/employment permits are issued by the cantons. **[VERIFIED]** https://www.sem.admin.ch/sem/en/home/themen/fza_schweiz-eu-efta/eu-efta_buerger_schweiz.html (SEM, page "last modified 13.01.2026"; cantonal procedures on SEM factsheets/FAQ — registration mechanics not re-read this session **[INFERENCE** that it is registration-level paperwork for EU nationals**]**)

---

## 4. Switzerland — recurring requirement patterns

Synthesized from §3 sources (observed postings + employer pages); attribute per claim there.

- **Always present:** Kubernetes/containers, Linux, IaC (Terraform-class), CI/CD, observability; distributed-systems fundamentals.
- **AI-infra specifics in the AI-heavy postings (Anthropic, Skydio, Loki, Lyceum):** cloud-GPU fleets, training-infrastructure ownership, model training/fine-tuning pipelines, distributed training, model serving/acceleration; containerized GPU workloads.
- **Public compute estate (CSCS):** platform automation, DevOps on HPC/AI systems, Slurm-class scheduling implied by role family. **[INFERENCE]**
- **Gap vs candidate resume:** no demonstrated PyTorch/training-orchestration or inference-serving (vLLM/TensorRT-class) evidence; GPU story on paper is thin beyond "GPU workloads". **[INFERENCE** judged from resume_v3.pdf**]**

---

## 5. Switzerland — decision-relevant summary (60%)

| Tier (thesis) | Realistic named targets | Evidence | Fit/effort |
|---|---|---|---|
| 1 – AI-infra vendors | Lyceum, Loki Robotics (Zurich startups, GPU cloud/training infra) | [OBSERVED] live postings | Good skill fit; small-team breadth; verify GPU depth |
| 1 – global infra | Google Zurich SRE – ML/YouTube-ML | [OBSERVED] postings via official mirrors | Direct SRE↔AI-infra match; very high bar |
| 2 – model labs (selective) | Anthropic Zurich (production post-training infra) | [OBSERVED] + careers page [VERIFIED] | Ambitious; needs training-stack evidence |
| 3 – AI product w/ infra ownership | Skydio Zurich (DL infra/acceleration) | [OBSERVED] | Requires CV/DL-pipeline depth; mid roles |
| research/public (adjacent) | CSCS/Swiss AI Initiative platform & DevOps roles; IBM Research Zurich systems postings | [VERIFIED] | Strong SRE fit (CSCS); lower pay; IBM mostly research |

**Net read:** Switzerland rewards (a) English-first international/ETH-domain employers, (b) a GPU/training-story upgrade. Pure German-speaking SME infra roles are mostly out of the realistic AI-infra funnel for this resume. **[INFERENCE]**

---

## 6. Berlin — employer segments and named employers (40% effort)

### 6.1 Live AI-infrastructure demand (aggregator, Berlin filter, accessed 2026-09-09)

29 AI-infrastructure postings at 9 employers on AI Dev Jobs — largest named clusters: **[OBSERVED]** https://aidevboard.com/location/berlin/ai-infrastructure

- **Inceptive (Berlin)** — *Secure Data Infrastructure for AI*; senior, **on-site**, $200k–275k band shown by board; biology/RNA AI company running serious training infrastructure. Tier 3-adjacent but infrastructure-owning. **[OBSERVED]**
- **Helsing (Berlin + Munich)** — multiple *AI Research Engineer* roles tagged GPU/distributed-systems/RL/ML engineering, plus deployed-AI and staff-SWE roles; defense-AI. Several listings remote/on-site; research-heavy job shapes. **[OBSERVED]**
- **Zeta Global (Berlin)** — *ML Ops Engineer* (on-site, mid). **[OBSERVED]**
- **Perplexity (Berlin)** — ML research engineering *internship* (not a senior target). **[OBSERVED]**
- Others in board (Parloa, Flatiron Health, Cresta) skew agent/frontend/platform-SWE rather than core AI infra — thin fit. **[OBSERVED]**

### 6.2 In-house ML-platform / MLOps segment (Berlin's structural signature)

- **Zalando (Berlin)** runs a large in-house ML platform organization with ML Platform/MLOps engineering roles. **Employer not directly verified this session** (careers site is JS-rendered; blocked by search wall). Long-standing, publicly documented engineering org — **[INFERENCE]** flagged for re-verification at application time. Channel: https://jobs.zalando.com/
- Same class: **Delivery Hero, HelloFresh, N26** Berlin ML/data-platform teams **[INFERENCE**, not verified**]**.
- Why this segment matters: it is where an SRE-with-GPU-flavor profile converts best in Berlin — platform reliability, cost/GPU-economics, serving infrastructure inside companies that own real AI workloads (recommendation, logistics forecasting, content). **[INFERENCE]**

### 6.3 AI scale-ups with compute ownership (selective)

- Inceptive (§6.1) and Helsing (§6.1) are the strongest observed; both post senior infra-flavored ML roles but expect deep-training-stack evidence. **[OBSERVED + INFERENCE]**
- DeepL, ElevenLabs, Black Forest Labs etc. run real GPU infrastructure but are HQ'd outside Berlin (Cologne, London/Freiburg…) — treat as Germany-wide/remote extensions of the Berlin funnel only where roles are Berlin-tagged or fully remote-DE. **[INFERENCE]**

### 6.4 Hiring locations — Berlin

- Berlin city itself (all §6.1 employers; Zalando/Delivery Hero/HelloFresh HQs); Helsing splits Berlin/Munich/Paris/London with remote-DE postings **[OBSERVED board + INFERENCE]**; Munich carries more hyperscaler/enterprise AI (Google Munich etc.) — out of the 40% Berlin allocation. **[INFERENCE]**

### 6.5 Language expectations — Berlin

- English is the working language at the observed employers (all postings in English) and at the scale-up/tech layer generally. German required mainly at domestic consumer corporates — which are not the top AI-infra targets here. **[OBSERVED + INFERENCE]**
- German remains a differentiator for Zalando-class German consumer companies' non-engineering-adjacent process; for engineering roles English-first. **[INFERENCE]**

### 6.6 German immigration for this candidate

- **EU citizens (incl. French) may enter and work in Germany with no visa and no residence permit; no labour-market restrictions; only a passport/ID needed; register with the municipality after moving.** **[VERIFIED]** https://www.make-it-in-germany.com/en/working-in-germany/information-eu-citizens (official Federal Government portal; IT specialists listed as a demand profession on the site)

---

## 7. Berlin — decision-relevant summary (40%)

| Tier (thesis) | Realistic named targets | Evidence | Fit/effort |
|---|---|---|---|
| 1 – AI-infra vendors | (no verified Berlin-HQ vendor surfaced; German cloud/GPU vendors are HQ'd elsewhere) | — | Reallocate vendor-tier effort to Zurich or Germany-wide-remote roles **[INFERENCE]** |
| 2 – model labs / AI-first scale-ups (selective) | Inceptive (senior AI data-infra, on-site); Helsing (ML eng, GPU/distributed) | [OBSERVED] live postings | Strong but research-competitive; needs training-stack evidence |
| 3 – AI product w/ substantive infra | Zalando ML Platform (re-verify); Delivery Hero/HelloFresh class; Zeta Global ML Ops | [OBSERVED] Zeta; **[INFERENCE]** others | Best conversion odds for an SRE profile; platform/reliability/economics scope |

**Net read:** Berlin's realistic funnel for this profile is *in-house ML platform/MLOps in product-scale companies* plus *senior infra roles inside AI scale-ups*; it is not a GPU-cloud-vendor market the way parts of the US are. The candidate's SRE/economics/observability story is the strongest Berlin currency; the missing piece is again ML-toolchain evidence. **[INFERENCE]**

---

## 8. Cross-market facts (both)

- **Work authorization:** none needed as an EU/EFTA national in either market (SEM page verified for CH incl. France; Make it in Germany verified for DE). Biggest practical lever in the search: remove all visa-fear framing; target companies hiring internationally. **[VERIFIED]**
- **Effort split:** Switzerland 60% / Berlin 40% (standing decision) maps naturally to Zurich-anchored §3 targets vs Berlin-anchored §6 targets.

---

## 9. Role-title aliases (search vocabulary)

Canonical per CONTEXT.md: **AI Infrastructure Engineer**; aliases **AI Platform Engineer, GPU Platform Engineer, ML Platform Engineer, SRE – AI Infrastructure** when responsibilities match.

Aliases observed in this session's live postings (add to search strings): **[OBSERVED]**
- *Senior AI Infrastructure Engineer* (Loki, Zurich)
- *GPU Platform Engineer* (Lyceum, Zurich)
- *ML Ops Engineer* (Zeta Global, Berlin)
- *Research Engineer, Production Model Post-Training* (Anthropic, Zurich)
- *Autonomy Engineer – ML & DL Infrastructure / Deep Learning Infrastructure / Deep Learning Model Acceleration* (Skydio, Zurich)
- *Secure Data Infrastructure for AI* (Inceptive, Berlin) — role-family phrasing, not a title
- *Systems Engineer – Platform Automation*, *DevOps Engineer* (CSCS)

Additional alias set worth matching on, by market convention **[INFERENCE]**: *ML Systems Engineer, Compute/Compute-Platform Engineer, Training Platform Engineer, Inference/Serving Platform Engineer, HPC & AI Platform Engineer, MLOps/ML Platform Engineer*.

---

## 10. Recurring requirement pattern — consolidated (both markets)

From observed postings §3/§6 (attribute per listing):
1. Kubernetes + containers + Linux (universal in infra postings; SRE lines at Google/CSCS).
2. IaC (Terraform-class), CI/CD, GitOps; observability (Prometheus/Grafana/OpenTelemetry) — mirrors resume.
3. AI-specific: GPU cluster operations, distributed training, model fine-tuning pipelines, serving/acceleration stacks, data pipelines for training.
4. SRE-specific: reliability engineering, incident response, capacity/cost economics, scale operations.
5. Soft signals: English working language; hybrid/on-site lean in observed AI postings (Inceptive on-site; Anthropic Zurich hybrid; several Helsing roles remote).

**Resume deltas this market profile exposes** **[INFERENCE]** (feed ticket 06 training priorities): (a) demonstrable GPU/training-infrastructure work (even small-scale), (b) at least one training/inference orchestration layer (Ray/Slurm-class or vLLM/TensorRT-class), (c) Python/ML-toolchain literacy beyond ops glue.

---

## 11. Limitations and source-date caveats

1. **Web search engine wall:** mid-session, all search providers failed (bot-detection/timeouts). NVIDIA-Zurich and Meta-Zurich presence, Zalando ML-platform hiring specifics, DeepL/ElevenLabs Berlin roles and Hetzner GPU-cloud hiring were **not verified** and are marked [INFERENCE] or omitted. Re-verify before any application targeting them.
2. **Aggregator data is a crawl, not a census:** AI Dev Jobs counts (Zurich 5 jobs/4 employers; Berlin 29 jobs/9 employers; salary figures) reflect one board's crawl on 2026-09-09; posting ages shown (19h–1y) date the crawl entries, not verified first-party posting dates. Salary bands shown by boards are unreliable; treat Inceptive's $200–275k and all "avg salary" figures as directional noise.
3. **LinkedIn mirrors of Google roles** (ch.linkedin.com) are third-party copies of official postings; canonical source is careers.google.com / sre.google.
4. **Date stamps:** CSCS openings dated 2026-05/2026-09; IBM postings numbered 2025_xxx/2026_xxx; SEM page last modified 13.01.2026; swiss-ai.org compute-call window 2026-08-03→09-14; Anthropic careers page live 2026-09-09. Postings expire — treat employer shortlists as current as of 2026-09-09 and re-check live pages during application runs.
5. **Company-presence claims for unverified employers** (Swisscom AI roles, Zalando/Delivery Hero/HelloFresh ML-platform orgs, NVIDIA/Meta Zurich) rest on [INFERENCE]; each needs a 5-minute first-party check (careers site / engineering blog) before entering the roster.
6. No Swiss/German salary benchmarking was performed against primary sources this session (search wall); compensation claims beyond observed listing bands are excluded rather than guessed.
