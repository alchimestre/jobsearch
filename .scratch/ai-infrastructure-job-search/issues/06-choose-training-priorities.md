# Choose Capability and Training Priorities

Type: grilling
Status: resolved
Blocked by: 03, 04

## Question


## Answer

### Gaps to close through training (produce observable evidence)

Three gaps, closed through one coherent project: a **GPU fleet Kubernetes operator** with an **SLO/error-budget layer**.

1. **Programming — Python first, then Go.** Python is the first language (AI/ML lingua franca, faster to productive evidence). Go is the second (gates the stretch Band 2: control-plane/platform software roles).
2. **GPU cluster operations.** Build a Kubernetes operator that schedules GPU workloads, monitors fleet health via DCGM metrics, and handles node cordoning/draining on unhealthy GPUs. Test against real cloud GPU instances (Lambda, Vast.ai, or RunPod spot, ~$5–20 total cost). No local NVIDIA GPU available (MacBook Air M4 only).
3. **SLO/error-budget methodology.** Define SLIs (scheduling latency, GPU utilization, fleet-health check success rate), error budgets, Prometheus alerts, and a runbook for the operator project itself. The operator is the system under SRE.

### Gaps to handle through positioning (no training)

4. **Distributed training/serving frameworks.** Removed from CV claims. Light conceptual study only (~4 hours total): data/model parallelism, FSDP, Ray/Slurm basics. Enough to answer honestly if asked; no artifacts, no claims.
5. **Datacenter fabric, AI storage, HPC performance.** Removed from CV claims. Light conceptual study only (~4 hours total): InfiniBand, RDMA, NCCL at a conceptual level. No artifacts, no claims.

### Phase structure

- **Phase 1 (weeks 1–6): Full Python project.** Build the complete GPU fleet operator in Python (using Kopf or equivalent), test against real cloud GPUs, add SLO layer (SLIs, error budgets, Prometheus alerts, runbook). Produce a complete GitHub repo with documentation by end of week 6. Evidence for gaps 1 (Python), 2 (GPU), and 4 (SLO) is available by this point.
- **Phase 2 (weeks 7–12): Go port.** Rewrite or extend the operator in Go. Deepen the implementation, improve the scheduling logic, and polish the GitHub repo. Produces Go evidence for the stretch band (Band 2: control-plane/platform software). Light conceptual study for gaps 3 and 5 happens in parallel during low-energy periods.

### Priority order

1. Python programming (weeks 1–6) — highest market weight, fastest to evidence
2. GPU cluster operations (weeks 1–6, integrated) — second-highest market weight
3. SLO/error-budget methodology (weeks 4–6, integrated) — differentiates SRE-on-paper from SRE-on-AI-fleet
4. Go programming (weeks 7–12) — gates stretch band, lower urgency
5. Distributed training/serving (light study, parallel) — positioned away
6. Datacenter fabric/HPC (light study, parallel) — positioned away

### Single project architecture

One GitHub repository containing:
- Kubernetes operator (Python in phase 1, Go port in phase 2) that schedules GPU workloads
- DCGM-based GPU fleet health monitoring against real cloud GPU instances
- Node cordoning and workload draining on GPU health failures
- SLI definitions, error budgets, Prometheus alert rules, and a runbook
- Architecture documentation and design decisions

This single artifact closes three evidence gaps (programming, GPU, SLO) and demonstrates the differentiators from the positioning thesis: cross-domain pattern transfer, infrastructure-to-architecture translation, and systems thinking.
Which gaps between Vincent’s current evidence and the target-role benchmark should the 12-week self-training plan address, in what priority order, and which gaps should be handled through positioning rather than study?
