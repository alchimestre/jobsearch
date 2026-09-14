# Tooling inventory — Vincent

Single source of truth for every tool claimed, its deployment depth, and its employer. Populated
from Vincent's 2026-09-11 session answers; corrected each time an attribution error surfaced.
Depth is tracked here for interview defence; the CV and application answers list tools without the
depth qualifier (Vincent's call, 2026-09-11).

Depth legend: `deployed` = installed/configured/operated in production · `used` = consumed, queried,
or debugged, not operated.

## Kiln — SRE, Jun 2024 – Jan 2026

| Tool | Depth | Notes |
|---|---|---|
| nginx | deployed | ingress |
| Flux | deployed | GitOps delivery |
| cert-manager | deployed | TLS automation |
| Velero | deployed | cluster backup/restore |
| Teleport | deployed | access management / identity-aware proxy |
| SOPS | deployed | secrets encryption |
| External Secrets | deployed | secrets operator |
| Redis | deployed | cache / KV |
| Elasticsearch | deployed | search / log index |
| PostgreSQL | deployed | relational database (also Cometh) |
| Loki | used | log aggregation |
| Argo CD | used | GitOps |
| Vault | used | secrets |
| Kyverno | used | policy enforcement |
| Datadog | used | monitoring |
| Jaeger | used | tracing |
| Thanos | used | Prometheus long-term storage |
| Geth | deployed | Ethereum execution client |
| Nethermind | deployed | Ethereum execution client |
| Lighthouse | deployed | Ethereum consensus client |
| Prysm | deployed | Ethereum consensus client |
| Teku | deployed | Ethereum consensus client |
| Besu | deployed | Ethereum execution client |
| IPFS | used | content addressing |

## Cometh — SRE, Feb 2023 – Oct 2023

| Tool | Depth | Notes |
|---|---|---|
| Traefik | deployed | ingress / reverse proxy (Vincent 2026-09-11) |
| Kong | deployed | API gateway (Vincent 2026-09-11) |
| HAProxy | deployed | load balancing (Vincent 2026-09-11; also Docaposte) |
| PostgreSQL | deployed | relational database (also Kiln) |
| MongoDB | deployed | document database |
| GCP Pub/Sub | deployed | messaging (confirmed Cometh 2026-09-11) |
| etcd | deployed | Kubernetes datastore (confirmed Cometh 2026-09-11) |

## Docaposte — DevOps Engineer, Jun 2022 – Feb 2023

| Tool | Depth | Notes |
|---|---|---|
| MetalLB | deployed | bare-metal load balancing |
| Cilium | deployed | CNI / network policy |
| HAProxy | deployed | bare-metal load balancing (also Cometh) |

## CI/CD

| Tool | Depth | Role |
|---|---|---|
| Drone CI | deployed | earlier role (pre-2024) |
| GitHub Actions | used | Kiln (most recent role) |

## Unplaced — employer not yet confirmed

| Tool | Depth | Likely role [INFERENCE] |
|---|---|---|
| Ceph | used | Kiln or Cometh |
| BigQuery | used | Cometh (GCP) |
| Jenkins | used | Docaposte-era |
| Terragrunt | used | Kiln or Cometh |
| Alertmanager | used | any |

## Removed — never used (do not re-suggest)

| Tool | Reason |
|---|---|
| Kafka | Vincent did not use it (2026-09-11) |
| KEDA | Vincent did not use it (2026-09-11) |
| Cloudflare | Vincent did not use it (2026-09-11) |
| MySQL | Never used professionally (2026-09-11) |

## Excluded from AI-lane CV positioning

Crypto node clients (Geth, Nethermind, Lighthouse, Prysm, Teku, Besu) and IPFS are real operational
evidence for the "40+ production networks" claim, but `CONTEXT.md` removes crypto-specific tooling
from the AI-lane positioning. They are currently on the CV as a substantiating bullet; drop them if
pursuing non-crypto roles and the bullet reads as noise.

## Open items

1. **Elasticsearch** — placed under Kiln; possibly used at multiple employers. Confirm scope.
