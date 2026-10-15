# AI Infrastructure Engineer — Hiring-Evidence Benchmark vs. Current Resume

- **Ticket:** `03-benchmark-role-evidence.md` (Wayfinder research, `.scratch/ai-infrastructure-job-search`)
- **Candidate profile:** `resume/resume.md` (SRE & Platform Engineer, Aix-en-Provence, France)
- **Benchmark date:** 2026-09-09
- **Scope:** Capability and evidence benchmark only. No training-plan recommendation (ticket 06).

## Method

28 first-party job descriptions (JDs) from 15 companies were sampled on 2026-09-09 directly from the
companies' own applicant-tracking systems (Greenhouse / Lever / Ashby public posting APIs), i.e. the
same text a candidate sees on the careers site. Tiers:

| Tier | Companies (JDs) |
|---|---|
| AI-infra vendors (GPU clouds, serving platforms) | CoreWeave (4), Nebius (3), Lambda (2), Fireworks (2), Cerebras (1), Baseten (1), Modal (1) |
| Model labs | Anthropic (3), Cohere (2), Mistral (2), xAI (1), OpenAI (1), Black Forest Labs (1) |
| AI product cos whose roles own AI infrastructure | Scale AI (3), Synthesia (1) |

Exact job titles, locations and URLs are listed in [Sources](#sources). One Ashby "Runway" posting was
fetched and then excluded: that board belongs to the *fintech* Runway, not Runway AI.

Term-frequency counts below are file-level counts over the 28 JDs (a JD either does or does not contain
the term). Counts are lower bounds on explicit demand: absence of a literal keyword does not mean a role
does not need the skill. Jobs are ephemeral — one CoreWeave posting (id 4699373006) disappeared while
this note was being written; see [Limitations](#limitations).

## 1. What the market repeatedly asks for

Explicit, repeated demand (count of sampled JDs):

| Requirement | Count | Notes |
|---|---|---|
| Kubernetes (operate/build/scale) | 23/28 | Table stakes across all three tiers; depth varies wildly (see §2.2) |
| GPU compute at cluster/fleet level | 18/28 | Hardware-adjacent skills: drivers, fleet health, cluster performance |
| Programming — Python | 17/28 | From "scripting" (SRE roles) to "production software" (platform roles) |
| Programming — Go | 17/28 | Explicit in most vendor platform roles; "ideally Golang" (Mistral), "proficient in Go" (CoreWeave) |
| On-call / incident response | 13/28 | Explicit; RCA + postmortems demanded (Anthropic, Mistral, Nebius, Lambda, CoreWeave, Cerebras) |
| Observability tooling (Prometheus 10, Grafana 9, OTel, Datadog, ELK, VictoriaMetrics…) | 11/28 | Near-universal in ops-adjacent roles; telemetry pipelines at inference scale (Nebius) |
| HPC / Slurm / workload schedulers | 11/28 | Slurm or HPC experience named even in non-HPC roles (Mistral, Cohere, BFL, xAI, Lambda) |
| Cost / resource efficiency / capacity | 9/28 | Cost-aware capacity, fractional GPUs, utilization, FinOps-adjacent |
| PyTorch / JAX / Megatron / FSDP | 6/28 | Concentrated in training-infra and lab roles; framework literacy, not research |
| Rust / C++ | 6/28 | Systems-adjacent roles (Nebius HPC, Lambda storage, xAI, Scale sandbox, Anthropic, CoreWeave) |
| Explicit SLO / SLI / error budgets | 5/28 | Lambda ("define and implement SLOs/SLIs"), Cerebras (SLOs, error budgets, chaos), Anthropic (postmortems, runbooks, SLOs), Mistral ("reliability KPIs… SLAs") |

Specialist (outlier) demand, concentrated in specific vendor/HPC roles rather than the general profile:
CUDA (2), NCCL (3), InfiniBand (3), RDMA (2), GPU Direct (2), eBPF (1), GPU-kernel authoring
(CoreWeave), disaggregated inference / inference latency & accuracy SLOs (Cerebras "nice to have").
These are real but belong to narrow roles, not to the generic AI-Infrastructure-Engineer baseline.

## 2. Capability-by-capability demand (with evidence)

### 2.1 GPU compute
- OpenAI — Fleet HPC: "reliability and uptime of all of OpenAI's compute fleet… minimizing hardware
  failure", automation for provisioning/monitoring server fleets; bonus PCIe, InfiniBand, power
  management, kernel perf tuning, IPMI/Redfish ([OA]).
- Nebius — HPC cluster engineer: tuning GPU clusters and InfiniBand networks, integrating new GPU
  hardware through Kubernetes/QEMU/KVM ([NB-HPC]); ML infra: GPU benchmarking CUDA/ROCm, kernel-level
  profiling ([NB-ML]).
- BFL — "Nvidia GPU drivers, and operators", operate large-scale GPU compute clusters ([BF]).
- xAI — "Designing, building, and scaling GPU compute infrastructure"; low-level understanding of NVIDIA
  drivers, CUDA toolkits ([XA]).
- Fireworks/CoreWeave/Scale name multi-GPU, multi-node, GPU-orchestration contexts ([FW-T], [CW-C], [SC-S]).

**Reading:** the baseline demand is *GPU cluster operations, fleet health and driver/stack fluency*, not
chip design. Kernel-authoring roles (CoreWeave "GPU Kernel Authoring & Optimization") are outliers.

### 2.2 Kubernetes / workload orchestration — three distinct depth bands
1. **Operate/admin at scale** (SRE-leaning): Lambda SRE, Managed Kubernetes — "bare-metal Kubernetes
   clusters, scaling up to thousands of nodes", Cluster API/kubeadm, GitOps/ArgoCD/Helm, SLOs/SLIs for
   Kubernetes ([LM-K]); CoreWeave platform engineer — "multi-tenant Kubernetes platforms", quotas,
   isolation, CKA "highly desired" ([CW-C]); Mistral SRE/Mistral Cloud ([MS-C], [MS-K]); Baseten
   ([BS]); Modal ([MD]).
2. **Build the control plane / fleet software** (platform-engineering): Anthropic Kubernetes Platform
   (London) — "extend the scheduler… topology-sensitive ML workloads across thousands of
   accelerators", scale apiserver/etcd, custom controllers/CRDs/operators; prefers Kueue/Volcano/Slurm
   and NCCL familiarity ([AN-K]); Mistral Managed Kubernetes — "control plane services, operators and
   custom controllers" ([MS-K]); Lambda Compute ([LM-C]); CoreWeave Kubernetes SWE — "custom Kubernetes
   operators and intelligent orchestration frameworks" ([CW-K]).
3. **User of k8s to run AI workloads** (training/serving roles): Cohere, Scale, Synthesia treat
   Kubernetes as an environment skill rather than the craft itself ([CH-T], [SC-S], [SY]).

**Reading:** a generic SRE can enter band 1 today; bands 2–3 at vendors/labs increasingly demand Go +
Kubernetes-internals engineering, plus scheduler/batch vocabulary (Kueue, Volcano, Slurm, gang
scheduling, topology awareness).

### 2.3 Distributed training / inference infrastructure
- Cohere, Training Infra Engineer: "distributed training infrastructures (Kubernetes, Slurm) and
  associated frameworks (Ray)", large-scale distributed training strategies, JAX/PyTorch/XLA/MLIR
  ([CH-T]).
- Fireworks, Training Infra Engineer: data parallelism, model parallelism, FSDP; optimize across
  "multiple GPUs, nodes, and data centers" ([FW-T]).
- Nebius: "data/tensor/context/expert parallelism, offloading, custom kernels", PyTorch/JAX/
  Megatron-LM/TensorRT-LLM, CUDA/NCCL stack ([NB-ML]).
- Anthropic: pre-training distributed-systems tech lead/manager, cluster-infrastructure staff roles
  (London) — scheduler extension, collective networking (NCCL) ([AN-K]).
- xAI: ML frameworks JAX/PyTorch + job schedulers (Slurm) ([XA]).

### 2.4 Model serving / inference
- Scale AI, "AI Infrastructure Engineer, Serving Platform" (London): fault-tolerant LLM serving at
  scale, "rate limiting, token streaming, load balancing, budgets"; nice-to-have vLLM, SGLang,
  TensorRT-LLM, TGI ([SC-SV]).
- Fireworks, LLM Infrastructure: build/serve control plane; open-source inference engines vLLM,
  SGLang, TRT-LLM; LLM internals (KV cache, disaggregated prefill) ([FW-L]).
- Nebius, SRE Token Factory (inference platform): "vLLM, Triton, Ray or another accelerator stack",
  GPU-heavy workloads, autoscaler tuning, request-routing/retry hardening ([NB-T]).
- Cerebras, Principal SRE – AI Inference: "model serving runtimes, disaggregated inference, GPU
  orchestration, latency and accuracy SLOs" ([CB]).
- Baseten: inference on B200/fractional H100 GPUs, multi-node inference ([BS]).
- Anthropic maintains whole Inference Infrastructure / Cloud Inference orgs (titles on board; only
  Kubernetes-Platform JD read in depth here) ([AN]).

**Reading:** serving-platform roles read as distributed-systems + backend engineering with an LLM-serving
stack. "AI Infrastructure Engineer, Serving Platform" is currently an exact, hiring title (Scale AI,
London + US) — a rare literal match for the canonical role name.

### 2.5 Performance
- CoreWeave HPC Performance Engineer: MPI workloads, RoCE/InfiniBand/GPUDirect/NUMA, public HPC
  benchmarks (HPCC, HPL, OSU, MLPerf-HPC, STREAM, IO500), custom kernel + kubevirt/qemu/vfio +
  containerd/nydus stack ([CW-H]).
- Nebius: performance profiling (Nsight, nvprof, perf), GPU acceptance testing, benchmarking
  dashboards ([NB-ML]).
- Synthesia: "schedule, monitor, and debug workloads running on GPUs"; performance-sensitive
  infrastructure ([SY]).
- OpenAI: "identify and fix performance bottlenecks", SQL/PromQL/Pandas on noisy fleet data ([OA]).
- BFL: "extract peak performance from the system (application and infrastructure side)" ([BF]).

### 2.6 Reliability (SRE)
- Anthropic, Staff+ SRE, Safeguards ML Infra (US): production change management at scale, canary
  analysis, "launch captain" releases, on-call; explicitly says ML/research background is **not**
  required — production judgment is the hiring bar ([AN-S]). Strong signal that SRE-only profiles are a
  recognized lab entry path.
- Lambda SRE: on-call rotation, "define and implement SLOs and SLIs", cluster recovery ([LM-K]).
- Cerebras: SLO/SLI for latency/throughput/accuracy, error budgets, blameless postmortems, chaos,
  MTTR ([CB]).
- Mistral SRE Cloud: reliability KPIs, RCA, on-call, SLA-oriented ([MS-C]).
- CoreWeave: SLA-backed multi-tenant platforms, on-call, RCA ([CW-C]).

### 2.7 Observability
Prometheus/Grafana/OpenTelemetry/Datadog/ELK/VictoriaMetrics/Loki/ClickHouse appear across SRE and
platform roles; Nebius Token Factory describes "telemetry pipelines — metrics, logs, and traces…
alert design and SLOs for high-throughput APIs" ([NB-T]); OpenAI wants PromQL fluency ([OA]).

### 2.8 Networking & storage (AI-flavored)
- Datacenter/GPU fabric depth is demanded *mostly by vendors/HPC*, not by labs: InfiniBand/RDMA
  (Nebius HPC, CoreWeave HPC), RoCE/GPUDirect/NUMA (CoreWeave HPC, CoreWeave Storage), NCCL
  (Nebius, Anthropic), eBPF (Anthropic preferred), network datapath monitoring (CoreWeave), plus xAI
  "Network Engineer — ML Infrastructure (High-Speed Interconnects)" and "Software Engineer, ML
  Networking" (Anthropic) as titles.
- AI storage: CoreWeave Storage — exabyte-scale S3-compatible object storage, RDMA, GPU Direct Storage,
  NFS/FUSE, Ceph/DAOS ([CW-S]); Lambda has SRE–Storage and Storage-control-plane roles ([LM] listing);
  Mistral SRE names "distributed storage"; BFL/xAI require understanding of data infrastructure at
  training scale ([BF], [XA]).

### 2.9 Programming
Python (17/28) and Go (17/28) dominate; Rust/C++ (6/28) for low-level roles. Platform/control-plane
roles insist on production code quality, and several state coding interviews explicitly (Nebius
"coding interviews as part of the process" [NB-HPC]; Mistral Golang [MS-K]; Anthropic any of
Go/Python/Rust/C++ [AN-K]; Lambda "strong programming skills in Go and Python" [LM-K]).

### 2.10 Cost
Cost efficiency/GPU utilization appears in 9/28: Fireworks ("cost efficiency… across compute, storage
and networking"), BFL ("balance performance with cost efficiency"), Synthesia ("cost-efficient"),
Cerebras ("cost-aware capacity management"), Baseten (multi-cloud capacity, fractional GPUs), Modal
(capacity planning), plus vendor capacity/finance-adjacent roles. Multi-cloud/hybrid operation is
explicit at Anthropic (AWS Bedrock / GCP Vertex), Baseten, Scale.

## 3. Benchmark matrix vs. the resume

Sources for resume claims: `resume/resume.md` (title block, "Profile", three SRE/DevOps
positions at Kiln, Cometh, Docaposte, Bitgen; Skills & Technologies lines; Core Competencies).
Only claims visibly present in the resume are treated as candidate evidence. `~` marks judgment calls that
are marked `[INFERENCE]` where interpretive.

| Capability | Demand seen in sample | Resume evidence (verbatim basis) | Verdict |
|---|---|---|---|
| Kubernetes / orchestration | 23/28; bands: operate (SRE) → build (platform) | "multi-environment Kubernetes clusters" (Kiln); "multi-zone Kubernetes clusters on GCP in a production environment" (Cometh); "recovered and stabilized critical Kubernetes clusters" (Docaposte); "Kubernetes" skill | **Supported strength.** Operations/admin band is evidenced; multi-environment + GCP production matches entry bands (e.g. Lambda "EKS, GKE or similar"). No evidence of control-plane/scheduler internals, operators/CRDs, or multi-tenant quota management |
| Reliability / SRE | on-call 13/28; SLOs 5/28; incident/RCA everywhere | 3 SRE/DevOps roles; "high-availability distributed infrastructure", "production hardening, risk mitigation" (Kiln); "led… incident response processes" (Cometh); ISO 27001 (Kiln, Cometh); HDS-certified healthcare (Docaposte) | **Supported strength** at the ops/SRE layer. Not evidenced: SLO/error-budget engineering, canary/rollout-safety methodology, quantified availability |
| Observability | 11/28 (Prometheus/Grafana/OTel/ELK/Datadog…) | "Improved system observability (Prometheus, Grafana, OpenTelemetry, ELK) and reduced MTTR" (Cometh); all four tools also listed in Skills | **Supported strength**; MTTR reduction claim is quantified directionally (no magnitude). Explicit MTTR appears in only 1/28 JDs (Cerebras) — the metric itself is on-demand language |
| GPU compute | 18/28; fleet/drivers/cluster ops baseline | Profile: "platforms for compute-intensive and GPU workloads"; Skills line "GPU Workloads" | **Ambiguous gap.** GPU appears as a keyword only; no bullet evidences managing GPU clusters, GPU drivers/operators, fleet health or GPU-adjacent tuning. If real Kiln/Cometh exposure exists it is not stated observably on the PDF |
| Distributed training/inference | Labs & training roles: parallelisms (DP/TP/FSDP), PyTorch/JAX/Megatron, NCCL/MPI, Slurm/Ray | No claim on resume | **Gap (unclaimed).** Nothing to compare; hiring evidence says framework *literacy* (not research) plus distributed-systems depth is the bar |
| Model serving | Serving roles: LLM serving fundamentals, vLLM/SGLang/TRT-LLM/TGI, token streaming, KV cache | No claim on resume | **Gap (unclaimed)** |
| Performance | HPC/perf roles: profiling, benchmarks (MLPerf/HPCC/OSU), MPI/RoCE/IB, kernel tuning | "Performance Tuning" skill keyword; "Reduced CI build times by 60% through pipeline optimization" (Cometh) | **Partially supported / thin.** One quantified pipeline-performance win exists; no profiling, benchmark, GPU or HPC performance evidence |
| Networking / storage | Fabric depth at vendors (IB/RDMA/GPUDirect/NCCL/eBPF); AI storage (S3-compatible, parallel FS) | "Managed Linux systems and distributed storage in production" (Docaposte); "40+ production networks" + "10+ distributed protocols" integrations (Kiln — blockchain networks, not datacenter fabrics) | **Ambiguous.** Distributed-storage ops is claimed but unquantified; no datacenter-fabric/GPU-networking evidence. Kiln "networks" are protocol networks — `[INFERENCE]` they are not InfiniBand/RDMA fabrics |
| Programming | Python 17/28, Go 17/28, Rust/C++ 6/28; coding interviews | No programming language claimed anywhere on the resume | **Gap (unclaimed).** Largest single mismatch with the "software engineer + operator" hybrid most JDs describe. Absence ≠ inability, but there is no observable evidence of Python/Go coding, which SRE-flavored roles (17/28) also demand |
| Cost | 9/28: utilization, fractional GPUs, cost-aware capacity, FinOps-ish | "Optimized infrastructure architecture, reducing cloud costs by 2…%" (Cometh — figure truncated in PDF extraction) | **Supported, weakly quantified.** Direction matches a repeated demand family; PDF magnitude illegible ("by 2[0?]%") — fix on resume |
| Workload orchestration beyond k8s | Slurm/HPC 11/28; Ray 2/28 (Cohere, Nebius); Kueue/Volcano (Anthropic pref.) | No claim | **Gap (unclaimed)** |
| Multi-cloud / hybrid | Anthropic (Bedrock/Vertex), Baseten, Scale | Kiln: "hybrid cloud environments" claim | **Supported claim** (Kiln hybrid cloud); cloud breadth otherwise GCP-centric — fine vs. JDs that accept one major cloud + IaC |

## 4. Decision-relevant summary (no training plan)

**Supported strengths to lead with:** Kubernetes operations at multi-environment/multi-zone production
scale; SRE/reliability/incident-response record incl. security-hardened environments (ISO 27001, HDS);
observability stack (Prometheus/Grafana/OTel/ELK) with a claimed MTTR reduction; Terraform/Ansible IaC +
CI/CD delivery; cost-reduction track record; hybrid-cloud claim (Kiln).

**Gaps and ambiguities to close with evidence (in descending order of market weight):**
1. **No programming-language evidence** (Python/Go) while 17/28 JDs name Python, 17/28 name Go, and
   platform/control-plane roles run coding interviews. This is the clearest blocker for "platform
   engineer" bands and labs' infrastructure-software roles.
2. **GPU claims are keyword-only** — no observable GPU-cluster, driver/operator or fleet-health
   evidence behind the "GPU Workloads" skill and the profile sentence.
3. **No distributed-training or model-serving evidence** (frameworks, parallelisms, NCCL/Slurm,
   vLLM/TGI-class serving) — required for lab and training-infra/serving-platform roles; less blocking
   for pure SRE-on-AI-fleet roles.
4. **No SLO/error-budget/canary-rollout evidence**, which separates SRE-on-paper from SRE-on-AI-fleet
   (Lambda, Cerebras, Anthropic wording).
5. **Thin/absent** datacenter networking (IB/RDMA), AI-storage, and HPC/performance-engineering
   evidence — mostly relevant to the vendor tier, which is the tier that most literally hires
   "AI Infrastructure"-titled roles.

**Role-band fit reading (resume ≈ 4 years SRE/DevOps through Jan 2026):**
- Reachable now: SRE / reliability roles on AI platforms (Nebius SRE families, Mistral SRE Cloud,
  CoreWeave platform ops, Lambda SRE bands at 3–6 yrs, Anthropic Safeguards SRE at 8+ "strong
  candidates", Baseten, Synthesia) — i.e. band-1 Kubernetes + reliability + observability is
  competitive; labs already state production-judgment (not ML) is the bar for one SRE org.
- Stretch: control-plane/platform software roles (Anthropic K8s platform expects 12+ yrs and k8s
  internals; CoreWeave Compute Services asks Go + 5+ yrs multi-tenant k8s; Mistral Managed Kubernetes
  asks Golang + 5 yrs).
- Out of band without strong artifacts: staff/principal inference or cluster-infra roles (Cerebras
  Principal SRE 15+ yrs, Anthropic staff cluster/K8s).
- `[INFERENCE]` SRE-labeled roles in this sample universally imply on-call even where the JD is silent.

## 5. Geography signals (input to ticket 02, not a market study)

- Exact "AI Infrastructure Engineer" postings: Scale AI — Serving Platform (London) and Sandbox
  Platform (London, SF/Seattle/NYC) — and Cerebras "AI Infrastructure Operations Engineer".
- Berlin appears in-sample via Nebius (Senior HPC Engineer, GPU Compute — Berlin/Amsterdam/London/
  EU-remote; SRE Token Factory — Berlin; Senior SWE Storage Virtualization — Berlin; Senior/Tech Lead
  Backend, Managed Kubernetes — Berlin/Amsterdam) and Cohere's office list (Berlin) for remote-friendly
  training-infra roles.
- Switzerland: **zero** Swiss-located AI-infra JDs in this 28-JD sample. Adjacent signals only:
  Anthropic hires AI research engineers in Zürich (post-training, Python + distributed computing);
  Mistral's Managed-Kubernetes posting lists Switzerland among eligible remote countries.
  `[INFERENCE]` Swiss AI-infrastructure hiring is thinner in public postings than Amsterdam/London/
  Paris/Berlin and leans to megacap/lab hubs (Google DeepMind Zürich, NVIDIA Zürich, IBM Research)
  whose ATSs were not sampled here; employer mapping belongs to ticket 02.
- EU-remote/Paris/Berlin/London coverage is strong (Mistral Paris + CH-remote, Nebius EU-remote,
  Synthesia Europe, BFL Freiburg, Cohere remote-friendly, Scale London, Anthropic London/Dublin/Zürich).
- US export-control constraint seen on CoreWeave postings (US-person requirement) — irrelevant for EU
  roles, a filter for US vendor roles. `[INFERENCE]` other US AI-cloud vendors may carry similar terms.

## 6. Limitations and source-date constraints

- All 28 JDs accessed **2026-09-09**; postings change or close without notice (CoreWeave job
  `4699373006` 404'd mid-session). Treat every URL as a snapshot, not a standing offer. JDs were
  captured from first-party ATS APIs (Greenhouse boards-api, Lever postings API, Ashby posting-api),
  i.e. the canonical careers-site text.
- Sample skews **senior/staff** (3–15+ yrs asked) and **US-heavy** among vendors/labs; early-career
  AI-infra roles are underrepresented (Nebius early-talent SRE/capacity excepted). Fireworks
  Training-Infra (3+ yrs) is the most junior-friendly training-infra role in the sample.
- OpenAI, Anthropic, xAI, Cohere, Mistral and BFL are treated as "model labs"; Scale AI and Synthesia
  as AI product companies. Tier boundaries are judgment calls — `[INFERENCE]`.
- Google DeepMind, Meta, NVIDIA and Hugging Face are **not** represented (Workday/closed ATS or board
  slug unavailable within budget); NVIDIA search returned no usable first-party posting. Their absence
  over-weights EU-accessible vendors (Nebius, Mistral, BFL, Synthesia) in the vendor/lab tiers.
- Keyword counts are literal-text lower bounds (e.g. a role saying "we own reliability" without the
  string "SLO" is not counted under SLO even if implied).
- Resume reading is from PDF text extraction; two values are truncated/illegible in extraction
  ("cloud costs by 2…%"; Cometh end date "OCT 202…") and are flagged rather than guessed. Resume
  internal claims ($8B assets, 40+ networks, 60% CI reduction, etc.) are reported as claims, not
  independently verified facts.
- No candidate experience was invented; every resume cell above traces to a PDF line.

## Sources

First-party posting URLs (accessed 2026-09-09):

**AI-infra vendors**
- `[CW-C]` CoreWeave — Senior Platform Engineer II, Compute Services (NJ/NY/Sunnyvale/Bellevue): https://boards.greenhouse.io/coreweave/jobs/4607559006
- `[CW-K]` CoreWeave — Software Engineer, Kubernetes (NJ/NY/Sunnyvale/Bellevue): https://boards.greenhouse.io/coreweave/jobs/4577764006
- `[CW-H]` CoreWeave — HPC Performance Engineer (NY/Sunnyvale/Bellevue): https://boards.greenhouse.io/coreweave/jobs/4601657006
- `[CW-S]` CoreWeave — Senior Engineer, Storage (NY): https://boards.greenhouse.io/coreweave/jobs/4709378006
- `[NB-HPC]` Nebius — Senior HPC Engineer, GPU Compute (Amsterdam/Berlin/London/EU-remote): https://boards.greenhouse.io/nebius/jobs/4383057101
- `[NB-ML]` Nebius — ML Infrastructure Engineer (Amsterdam/EU-remote/US-remote): https://boards.greenhouse.io/nebius/jobs/4864833101
- `[NB-T]` Nebius — Senior SRE — Token Factory, Inference Platform (Amsterdam/Berlin/London/Prague/EU-remote): https://boards.greenhouse.io/nebius/jobs/4600919101
- `[LM-K]` Lambda — Senior SRE, Managed Kubernetes (SF/San Jose/Bellevue): https://jobs.ashbyhq.com/lambda/9b0cf272-e690-4213-828f-1a1ed508b53c
- `[LM-C]` Lambda — Senior Software Engineer, Compute (SF/San Jose/Bellevue): https://jobs.ashbyhq.com/lambda/0f94de99-5027-4cae-a6d4-757eef2845b6
- `[FW-T]` Fireworks AI — Member of Technical Staff, AI Training Infrastructure (San Mateo): https://jobs.ashbyhq.com/fireworks/a2850702-dea3-4e2c-a3ec-7ae257d36eb7
- `[FW-L]` Fireworks AI — Software Engineer, LLM Infrastructure (San Mateo): https://jobs.ashbyhq.com/fireworks/82013447-2713-46ca-aab1-b0a34f7b565a
- `[CB]` Cerebras — Principal SRE, AI Inference (SF Bay Area/Toronto): https://jobs.ashbyhq.com/cerebras/1bf0ea92-b0fd-4163-b44c-3564e67b15c1
- `[BS]` Baseten — Cloud Platform Engineer (SF/Remote/Toronto/NYC/Montreal): https://jobs.ashbyhq.com/baseten/916e9d62-492a-4562-971f-3e97e3868392
- `[MD]` Modal — Member of Technical Staff, Platform Engineering (NYC/Stockholm): https://jobs.ashbyhq.com/modal/84467a68-6876-4730-9d80-6c6f3d0c2d71

**Model labs**
- `[AN-K]` Anthropic — Staff Software Engineer, Kubernetes Platform (London): https://boards.greenhouse.io/anthropic/jobs/5211305008
- `[AN-S]` Anthropic — Staff+ SRE, Safeguards ML Infra (SF/NYC/Seattle, US remote-friendly): https://boards.greenhouse.io/anthropic/jobs/5416709008
- `[AN-Z]` Anthropic — Research Engineer, Production Model Post-Training (Zürich): https://boards.greenhouse.io/anthropic/jobs/5112018008
- `[MS-C]` Mistral — Site Reliability Engineer, Mistral Cloud (Paris): https://jobs.ashbyhq.com/mistral.ai/4b25c97e-ab58-4148-9126-9d4e2c41aaf7
- `[MS-K]` Mistral — Mistral Cloud, Software Engineer, Managed Kubernetes (Paris; remote EMEA incl. Switzerland): https://jobs.ashbyhq.com/mistral.ai/9eba1e5b-c563-44e0-8851-97d2206fb985
- `[CH-T]` Cohere — Member of Technical Staff, Training Infra Engineer (London/Paris/SF/NY/Toronto/Montreal, remote-friendly): https://jobs.ashbyhq.com/cohere/a13207e7-dc82-473f-8ca4-e832452fe8c3
- `[CH-S]` Cohere — SRE, Inference Infrastructure (Toronto/SF/NY/Montreal): https://jobs.ashbyhq.com/cohere/8b6696e1-f1c4-4010-bde9-3cec1340a2a6
- `[XA]` xAI — ML Infrastructure Engineer (Palo Alto): https://boards.greenhouse.io/xai/jobs/5193037007
- `[OA]` OpenAI — Software Engineer, GPU Infrastructure – HPC (SF): https://jobs.ashbyhq.com/openai/f58cb1eb-9642-4a4d-a14d-d7a57d583a11
- `[BF]` Black Forest Labs — Member of Technical Staff, Research Infrastructure Engineer (Freiburg, DE / SF): https://jobs.ashbyhq.com/black-forest-labs/728b8f3b-f355-4e02-84b8-a64c94d0f351

**AI product companies**
- `[SC-SV]` Scale AI — AI Infrastructure Engineer, Serving Platform (London): https://boards.greenhouse.io/scaleai/jobs/4717977005
- `[SC-SD]` Scale AI — AI Infrastructure Engineer, Sandbox Platform (London): https://boards.greenhouse.io/scaleai/jobs/4717105005
- `[SC-F]` Scale AI — Software Engineer, Frontier AI Infrastructure (SF/NYC/STL/DC): https://boards.greenhouse.io/scaleai/jobs/4363623005
- `[SY]` Synthesia — ML Platform Engineer (Europe): https://jobs.ashbyhq.com/synthesia/6730e2e5-0d32-4919-a438-625f1673b70c

Supporting references:
- Candidate resume: `resume/resume.md`
- Ticket 03: `.scratch/ai-infrastructure-job-search/issues/03-benchmark-role-evidence.md`
- Board listings that informed sampling (same access date): Nebius/CoreWeave/Scale/Anthropic/xAI
  Greenhouse boards; Mistral/Cohere/BFL/Cerebras/Baseten/Modal/Lambda/Fireworks/OpenAI Ashby boards.
