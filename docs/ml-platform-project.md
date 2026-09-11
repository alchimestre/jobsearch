# ML Platform on Kubernetes — evidence artifact

Replaces `gpu-fleet-operator` as the single portfolio project (amended 2026-09-11, second amendment).
Closes the same gaps as the old plan — Python, SLO/error-budget methodology — and adds the ML-lifecycle
evidence that ML platform / MLOps job descriptions screen on, while reusing the proven strengths
(Kubernetes, Helm, Terraform-class IaC, Prometheus/Grafana/OTel, CI/CD, cost-aware operations).

**Status:** spec, not yet built. Target: complete by week 6.

---

## 1. What it must prove

| JD requirement (benchmark + market research) | How this artifact proves it |
|---|---|
| Kubernetes as the platform ML workloads run on | Every component is a Kubernetes workload with Helm-managed deployment, probes, resources, and scaling |
| ML lifecycle ownership (the MLOps core) | Training pipeline → model registry → serving → monitoring, wired end to end |
| Python | The pipeline, the serving service, the drift job, and the tests are Python |
| Reliability / on-call / incident response | Failure drills with recorded recovery: failed pipeline step, bad model version rollback, unhealthy replica |
| Observability | Prometheus metrics for pipeline *and* service, Grafana dashboard, alert rules |
| Cost / capacity awareness | Resource requests/limits, HPA behaviour on the serving path, a written cost note (node-hours, what would change at 100× traffic) |
| Rollout safety | Versioned rollout and rollback of a model+image pair, with the failure drill to prove the rollback works |
| SLO / error budgets (the differentiator) | SLIs defined below, error-budget policy, burn-rate alerts, runbook |

**Non-goals — do not build or claim:** distributed training, CUDA/NCCL/RDMA/HPC, GPU fleet management,
multi-tenant isolation, production-scale anything. The artifact is a learning platform; call it that in
the README and in interviews.

---

## 2. Architecture

```
                 ┌──────────────── Kubernetes (single node, OrbStack) ─────────────────┐
  CronJob /      │  Argo Workflows (or plain Jobs)                                    │
  manual ───────▶│   step 1 fetch data ─▶ step 2 train (scikit-learn) ─▶ step 3 eval  │
                 │                                        │                           │
                 │                                        ▼                           │
                 │                          MLflow tracking + model registry         │
                 │                             (versions, stage transitions)          │
                 │                                        │                           │
                 │                                        ▼                           │
                 │      FastAPI model server  ◀── Helm chart ──  Deployment + HPA    │
                 │            │  /metrics, /predict                                  │
                 │            ▼                                                       │
                 │   Prometheus ─▶ alert rules ─▶ Alertmanager ─▶ Grafana dashboard   │
                 │   drift job ─▶ drift gauge ─▶ alert on threshold breach            │
                 └────────────────────────────────────────────────────────────────────┘
   GitOps: GitHub Actions (test, build, push) ─▶ Argo CD / Flux ─▶ cluster
```

### Component choices (boring, small, defensible)

| Layer | Choice | Why this and not the heavy option |
|---|---|---|
| Pipeline | **Argo Workflows** if the k8s-CRD learning is worth it; otherwise a Python orchestrator creating `Job`s | Kubeflow Pipelines is the canonical keyword but is heavy for one node and eats the time budget; Argo is k8s-native and still real orchestration |
| Registry | **MLflow** (tracking server + registry), artifacts on a PVC or MinIO | Canonical, easy, and the registry/stage concept is exactly what MLOps JDs ask about |
| Serving | **FastAPI** in a small image, Helm-deployed, `/predict`, `/metrics`, `/healthz` | KServe/TorchServe add operators and moving parts; the reliability work is the point, not the serving framework |
| Rollout | Kubernetes rolling update + explicit rollback drill; **Argo Rollouts** only if time allows | Canary is a nice keyword, not worth the week it costs here |
| Monitoring | Prometheus + Grafana + Alertmanager (already in the proven stack); drift via PSI/KS as a gauge | No new observability vendor |
| CD | GitHub Actions build/test → **Argo CD** (or Flux) sync of the Helm chart | Evidences GitOps, which the CV already claims |
| Model/data | Small public tabular dataset (e.g. a UCI set) + scikit-learn model | CPU-only, fast retrains, no GPU dependency. Optional: swap in a tiny transformer if an LLM-flavoured artifact is wanted — decide at week 5, not before |

### Optional GPU (honesty support only)

One bounded cloud-GPU session (≤ $20) may compare CPU vs GPU serving latency on the same model, purely to
keep the CV's `GPU exposure` line honest. Not part of the artifact's acceptance criteria, no ongoing spend.

---

## 3. SLIs and error budgets

| SLI | Definition | Target | Error budget |
|---|---|---|---|
| Serving availability | successful `/predict` responses ÷ total | 99.5% | 0.5% monthly |
| Serving latency | p95 `/predict` latency | < 250 ms | 5% of requests may exceed within budget |
| Pipeline success rate | successful scheduled runs ÷ attempts | ≥ 95% | 5% of runs monthly |
| Drift score | PSI between training and live feature distributions | < 0.2 (alert on breach) | n/a — alerting signal, not a budget |

Policy: when a budget is exhausted, feature work stops on that component until the cause is fixed and the
runbook is updated. That policy is the SLO *evidence* — write it down, don't just have the numbers.

---

## 4. Week plan (mirrors strategy §5)

| Week | Deliverable | Done when |
|---|---|---|
| 1 | Repo, README, architecture, OrbStack cluster, first containerised training step | A training job runs on the cluster and writes a model artifact |
| 2 | MLflow registry + end-to-end serving | A trained model is registered, served, and answering requests |
| 3 | Scheduled retrain → registry version → rollout, wired end to end | The retrain→register→serve path runs unattended |
| 4 | Grafana dashboard, alert rules, error-budget burn, drift monitoring | Alerts fire on a synthetic failure; drift gauge moves on injected skew |
| 5 | Failure drills + runbook | Failed step, bad-version rollback, unhealthy replica each recovered and recorded |
| 6 | Complete package + README landing page | A reviewer clones and reproduces the whole path from the README alone |

Overrun rule: see strategy §7 rule 5 — slip more than a week and 10% of weekly time moves from search to
training until recovered. Do not extend the artifact into weeks 7–12; Go and search own that window.

---

## 5. Verification (what "done" means, checkably)

- `make up` / documented commands bring the platform up on a clean OrbStack cluster.
- Each component has an acceptance test that fails when the component is broken (not a mock echo).
- `docs/evidence.md` in the repo records the drills: what was broken, what the alert did, what the
  recovery was, and the metrics before/after. Claims in the CV must trace to a line in that file.
- README states plainly: lab-scale, single node, not production, dataset and model provenance given.

---

## 6. Honesty rules

1. The repo is described as a **lab/learning platform**. No "production", no "at scale", no invented users.
2. Numbers that go on the CV must exist in `docs/evidence.md` with the command or screenshot that produced them.
3. Until week 6 completes: CV/LinkedIn may say nothing about it, or `currently building` — never more.
4. `GPU exposure` stays as-is unless the optional GPU run happens.
5. Python and SLO/error-budget claims are switched from `in progress` to plain only when the repo proves them.
