# Benchmark AI Infrastructure Hiring Evidence

Type: research
Status: resolved

## Question

What capabilities and observable evidence do current AI Infrastructure Engineer openings expect, especially for GPU compute, workload orchestration, distributed training or inference, model serving, performance, reliability, observability, and cost—and how do those expectations compare with the evidence in `~/Documents/resume_v3.pdf`?

## Answer

The current resume already supports the operations/SRE band of AI infrastructure: production Kubernetes, reliability and incident response, observability, IaC/CI/CD, cost reduction, security-hardened environments, and hybrid-cloud work. That makes reliability roles on AI platforms reachable now; control-plane software roles are stretch targets, and staff/principal inference-cluster roles are out of band without substantially stronger evidence.

Across 28 first-party job descriptions, repeated demand was Kubernetes (23/28), GPU fleet work (18/28), Python (17/28), Go (17/28), incident/on-call work (13/28), observability (11/28), HPC or workload schedulers (11/28), and cost/capacity work (9/28). The resume’s largest observable gaps are missing Python/Go evidence, keyword-only GPU claims, no distributed-training or model-serving evidence, and no explicit SLO/error-budget/canary evidence. Datacenter fabrics, AI storage, and low-level performance are narrower vendor/HPC gaps rather than universal baseline requirements.

Research asset: `research/ai-infrastructure-benchmark` at commit `ff2a1cadeadbcb1b32cb8920e7b739fc42e1f749`, file `research/ai-infrastructure-hiring-evidence.md`.
