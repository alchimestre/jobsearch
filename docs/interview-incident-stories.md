# Interview prep — production incident stories

**Status: prep scaffolding, not evidence.** This file contains *frameworks and hypotheses*, not events.
Every `⟨slot⟩` is a fact only Vincent can supply from memory, tickets or dashboards. Nothing here may be
told as a story until its slots are filled from the real record — that is the same rule the rest of this
repo runs on (`docs/search-plan.md` §8 "Claims lag evidence"; `docs/evidence-package.md` "No
fabricated claims").

## 0. Why this file is frames and not scripts

An invented incident dies on the second follow-up question, not the first. Interviewers ask: what time was
it, who paged you, which metric did you open first, what did the dashboard show at T+5, what did you try
that failed, what did the post-mortem action items say, how many closed. A fabricated story has no interior
— it has no false leads, no argument with another team, no fix that made it worse for ten minutes. SRE
interviewers hear dozens of these and the tell is always the same: a story with no friction.

The real ones, on the other hand, are already on the CV:

| CV line | Employer | What it already is |
|---|---|---|
| *"Recovered and stabilized critical Kubernetes clusters in a regulated healthcare environment"* | Docaposte | **An incident story already on the CV** — written down and never told |
| *"Led ISO 27001 security implementation and incident response processes"* | Cometh | Incident response *ownership*, plus the audit that rewrote the practice |
| *"Improved observability … and reduced MTTR"* | Cometh | A before/after number you are already claiming |
| *"Optimized infrastructure architecture, reducing cloud costs by 25%"* | Cometh | The number every cost question is fishing for |
| *"Operated … $8B+ in digital assets across 40+ production networks"* | Kiln | Blast radius, at a scale most interviewers will not have touched |

Five frames follow, each derived from the stack you actually operated. **Confirm or drop.** If a frame does
not match something that really happened, delete it rather than adapt it — an adapted story drifts under
questioning.

## 1. What you can defend today (from `CONTEXT.md` → Evidence Boundaries)

- Production Kubernetes operations at multi-environment / multi-zone scale
- SRE reliability, **incident response**, and security-hardened environments (ISO 27001, HDS)
- Observability stack with **MTTR reduction**
- Kiln tooling **deployed**: nginx (ingress), Flux (GitOps), **cert-manager (TLS automation)**, **Velero
  (backup/restore)**, Teleport (access), SOPS (secrets encryption), External Secrets, Redis, Elasticsearch,
  PostgreSQL
- Kiln tooling **used**: Loki, Argo CD, Vault, Kyverno, Datadog, Jaeger, Thanos
- Docaposte **bare-metal**: MetalLB, Cilium (network policy), HAProxy
- Cometh **edge/ingress**: Traefik, Kong, HAProxy; multi-zone GCP Kubernetes; Postgres, MongoDB, Pub/Sub, etcd
- Cost-reduction track record · Hybrid-cloud operations

## 2. What the story must not claim (same source)

Never adjacent-claim these while telling any incident below: **GPU fleet operations** (GPU-adjacent only),
**production Python/Go** (operational scripting only), **ML lifecycle** (pipelines, registry, serving,
drift), **owned SLO/error-budget programme**, distributed training or model serving, datacenter fabric.
A strong incident story told next to an undefendable claim loses both.

---

## Frame A — Bare-metal Kubernetes cluster recovery in an HDS-certified environment

**Surface (verified):** Docaposte, DevOps Engineer, Jun 2022 – Feb 2023. Bare-metal Kubernetes,
MetalLB (bare-metal load balancing), Cilium (CNI / network policy), HAProxy, Ansible-deployed systems,
Linux + distributed storage, HDS-certified health-data systems.

**Failure modes this surface produces**, pick the one that happened:
1. **MetalLB VIP failover / ARP** — the Service VIP stops answering after a node drop; connections to the
   ingress hang rather than error, so monitoring still shows the app as "up" while users see timeouts.
2. **Cilium policy or agent restart** — a CNI rollout or agent failure blackholes pod-to-pod traffic in one
   namespace only; symptoms look like one broken app, cause is cluster-wide.
3. **Control-plane / etcd instability** on bare metal after disk latency or storage degradation — API server
   slow, kubelets drop, workloads evicted in waves.
4. **Distributed storage degradation** — PVC latency climbing, pods Pending, a node's storage path degraded.

**Why it is hard (the part worth telling):** bare metal has no cloud control plane to lean on — no managed
node replacement, no security group you can check, no provider status page. The cluster says healthy while
the network does not work. And it is HDS: every intervention may be a regulated change requiring a written
trace, and patient-data availability is the blast radius.

**STAR skeleton — fill the slots:**
- **S:** ⟨date, environment, what was running on it⟩. The first signal: ⟨alert name / who reported / dashboard⟩.
- **T:** ⟨blast radius — how many services or sites, was patient-adjacent access affected, time pressure⟩.
  Your role: ⟨leading the bridge / on the bridge with ⟨who⟩⟩.
- **A:** ⟨first hypothesis — what you checked and what it ruled out⟩ → ⟨the false lead, and how long it cost⟩
  → ⟨the actual diagnostic step that found it: which command, which metric, which node⟩ → ⟨the fix applied,
  and whether you had to do it without ⟨something⟩⟩ → ⟨the decision under incomplete data you own: e.g. drain
  vs. reboot vs. failover, and what made you choose it⟩ → ⟨who else you pulled in and what you asked them
  for⟩.
- **R:** ⟨MTTR: detection → mitigation → full recovery⟩ → ⟨what changed permanently: runbook, alert rule,
  redundancy, automation⟩ → ⟨the one number: nodes, services, minutes, or backups validated⟩.

**Evidence hooks to cite by name:** MetalLB, Cilium, HAProxy, Ansible, HDS, "recovered and stabilized
critical Kubernetes clusters" (CV). If Velero existed in that environment, a **restore validation** after
the incident is the strongest possible ending.

**Drill they will run:** *How did you know it was the network and not the application? What did the
dashboard look like before and after? Why didn't an alert fire earlier? Did you restore anything from
backup, and how did you verify the backup was good? What in your own prior changes contributed?*

**Lane fit:** the strongest frame for **regulated / healthcare employers** — directly relevant to #31
(Annapurna, unnamed AI + healthcare client) and to any HDS/GDPR-heavy French employer.

---

## Frame B — Certificate expiry or ingress cascade, and the automation that ended the class

**Surface (verified):** Kiln. **cert-manager (TLS automation) deployed**, nginx ingress, Flux GitOps
delivery, multi-environment/multi-zone clusters, Terraform IaC, Teleport access, Prometheus/Grafana/Loki
observability, Datadog.

**Failure modes this surface produces:**
1. **Cert expiry on an ingress or an internal service** — renewal silently failing for weeks, then external
   clients fail TLS; internal services using the same issuer fail at the same moment.
2. **Renewal storm / rate limit** — every replica restarts at once on renewal, ingress reload load spikes,
   brief 502s.
3. **Ingress config drift during a GitOps rollout** — a Flux-applied change reduces replicas or drops a
   backend, and the revert is the interesting part.
4. **Cross-environment blast radius** — one Terraform/GitOps change reaching more environments than intended.

**Why it is hard:** the symptom (external TLS failures) is two layers from the cause (an ACME challenge
that stopped passing, or a DNS delegation). Meanwhile every consumer of that certificate fails at the same
second, which looks like an attack or a network fault.

**STAR skeleton:**
- **S:** ⟨which endpoint/service, who noticed — customers, an external partner, monitoring⟩.
- **T:** ⟨what was down for whom; the commercial or contractual pressure⟩.
- **A:** ⟨first check: expiry date, ACME order state, challenge path⟩ → ⟨why renewal had been failing —
  the real root cause, not "cert expired"⟩ → ⟨the stopgap used to restore service: manual issuance,
  temporary ingress, failover⟩ → ⟨the decision: issue manually vs. restore automation under pressure⟩ →
  ⟨the permanent change: monitoring on `certmanager_certificate_expiration_timestamp_seconds` with alerting
  well before expiry, alert on failed ACME orders, staging issuer in CI to catch it early, expiry runbook,
  or moving the class of problem out of human hands entirely⟩.
- **R:** ⟨time to restore; how many future occurrences were eliminated — "no expiry incident since, across
  N environments and M certificates"⟩.

**Evidence hooks:** cert-manager `deployed` at Kiln (`docs/tooling-inventory.md`) — note that TLS
automation *existing* is itself the residue of this class of incident. Prometheus alerting rules, Flux
rollback, nginx ingress.

**Drill:** *Why did the renewal fail — what was the actual mechanism? What was your alert threshold and why?
Did you alert on expiry or on renewal failure, and why that one? What did you do about the other
certificates with the same latent problem? How did you test the fix without breaking production again?*

**Lane fit:** universal — works for any employer running Kubernetes. Also the cleanest "I turned a manual
recovery into a system" story, which is what platform roles (#30 Atlantic) score highest.

---

## Frame C — Secrets and access: rotation, revocation, and the audit

**Surface (verified):** Kiln — **SOPS (secrets encryption) and External Secrets deployed**, Teleport
(identity-aware access), Vault (used), Kyverno (policy, used). Cometh — **led ISO 27001 security
implementation and incident response processes**; Traefik, Kong.

**Failure modes this surface produces:**
1. **Rotation breaks workloads** — the new secret reaches the external store but a workload still holds the
   old value; partial fleet failure that looks like an application bug.
2. **Credential exposed** — a key in a repo, a log, or a CI variable; the incident is the **revocation and
   blast-radius assessment**, not the leak itself: which systems used it, what it could reach, what must be
   rotated in what order to avoid an outage.
3. **Audit finding** — an ISO 27001 assessment turns up missing audit logging, weak access segmentation or
   an unrotated credential. The work is remediation under a deadline with evidence to produce.
4. **Access-path failure** — Teleport or an identity-aware proxy down means nobody can reach production,
   which is an availability incident *and* the moment everyone wants to bypass it.

**Why it is hard:** rotation is a distributed consistency problem with a human deadline, and the safe order
is usually the opposite of the obvious one. The second-hardest part is telling people "no" when bypass is
fastest.

**STAR skeleton:**
- **S:** ⟨exposure or finding, how it surfaced, sensitivity of the data⟩.
- **T:** ⟨deadline — 24h, or the audit window; the systems in scope; the constraint of not causing an
  outage⟩.
- **A:** ⟨blast-radius mapping: which workloads consumed it, where it was cached, where it was logged⟩ →
  ⟨rotation order and why: dual-credential window / staged rollout⟩ → ⟨the thing that broke mid-rotation
  and how you caught it before the outage spread⟩ → ⟨the enforcement: SOPS + External Secrets so the value
  never sits in a manifest, Kyverno policy to block plaintext, Teleport short-lived certificates so long-lived
  keys stop existing, audit logging on access⟩.
- **R:** ⟨time to full rotation, systems covered, audits passed, and the honest number of future manual
  rotations eliminated⟩.

**Evidence hooks:** SOPS, External Secrets, Teleport, Kyverno, Vault (inventory); Cometh ISO 27001 lead;
"risk-mitigation" bullet at Kiln.

**Drill:** *What was the search you ran to find every consumer? How did you prove nothing was missed? What
broke during rotation? What was the emergency-access story — how would you have got in if Teleport had
died? Who disagreed with your approach and why?*

**Lane fit:** strong everywhere; dominant for security-conscious AI-infra employers and for #29 idnow-style
regulated DE roles. Also the frame that answers "how do you handle a 24-hour deadline".

---

## Frame D — Node-fleet degradation on 40+ production networks

**Surface (verified):** Kiln, SRE, Jun 2024 – Jan 2026. High-availability distributed infrastructure
securing **$8B+ across 40+ production networks**, **10+ distributed protocols** integrated into hybrid cloud,
Terraform IaC across multi-environment Kubernetes, GitOps (Flux) delivery, Velero backup/restore, Teleport,
Prometheus/Grafana/Thanos/Loki/Jaeger/Datadog observability, 5+ consensus clients (Geth, Nethermind,
Lighthouse, Prysm, Teku, Besu), multi-zone.

**Failure modes this surface produces:**
1. **Client release degrades sync or peer connectivity** across a subset of networks; some nodes stop
   attesting or fall behind head. The pressure is *not* a single outage but **avoiding a mass event across
   many networks at once** — a rolling change that must be staged per network and per client.
2. **Disk / IO saturation** on a node class as chain data grows; nodes fall behind in waves, alerts fire
   across many networks simultaneously and the flood hides the real signal.
3. **Hybrid-cloud link degradation** — a network path between cloud and on-prem sites degrades; nodes stay up
   but lose peers, so every dashboard says healthy while rewards/monitoring silently drop.
4. **Upgrade desynchronisation** — the fleet ends up split across client versions and one version's peers
   refuse the other's connections.

**Why it is hard:** 40+ independent networks with different chains, clients and failure signatures; no single
control plane; and the cost of a bad decision is measured in downtime penalties across many networks at
once. Alerting noise is the enemy: the incident is *finding the pattern* across many simultaneous alerts.

**STAR skeleton:**
- **S:** ⟨which networks/clients, what the alert flood looked like, who noticed first⟩.
- **T:** ⟨the risk gradient: how many networks at risk if you moved too fast; the reward/metric at risk⟩.
- **A:** ⟨how you cut through the noise — grouping, a specific metric, a per-client comparison⟩ → ⟨the
  pattern you found: one client/version/kernel/node class, not all⟩ → ⟨the staging decision: which networks
  first, which held back, and why⟩ → ⟨the Velero/backup and rollback plan you had before touching anything⟩
  → ⟨the change in waves, observing per wave⟩.
- **R:** ⟨networks affected, downtime avoided — the number that matters here is *what did not happen*:
  "no network missed ⟨…⟩"⟩ → ⟨permanent: staged rollout policy, per-client canaries, alert grouping, a
  runbook per client version⟩.

**Evidence hooks:** 40+ networks, $8B+, 10+ protocols, Terraform multi-environment, Flux, Velero, Thanos
long-term metrics (good for "we could compare against last upgrade" claims).

**⚠️ Positioning guard:** `CONTEXT.md` excludes crypto-specific tooling from **AI-lane** positioning. Tell
this frame in **Web3-track** interviews or as a pure reliability story with the domain abstracted
("multi-tenant distributed networks"), not in AI-infra interviews where the reader is scanning for ML.

**Drill:** *How did you decide the rollout order? What was your rollback trigger and who had authority to
call it? How did you know a network was healthy after each wave — what was the SLI? What did you do when
two networks reacted differently to the same change?*

**Lane fit:** Web3 track (#25 Blockstream, #26 Anagram), and generic high-scale SRE.

---

## Frame E — Cloud cost runaway, and the −25%

**Surface (verified):** Cometh, SRE, Feb 2023 – Oct 2023. Multi-zone Kubernetes on GCP, Traefik/Kong/HAProxy
gateways, Postgres, MongoDB, Pub/Sub, etcd, CI/CD pipelines; **"Optimized infrastructure architecture,
reducing cloud costs by 25%"** on the CV. (Also available: −60% CI build time.)

**Failure modes this surface produces:**
1. **Unbounded egress or log volume** — one misconfiguration (verbose logging to a paid sink, a retry loop
   crossing a NAT boundary) producing a bill that is only visible at month end.
2. **Idle/oversized capacity** — over-provisioned node pools and orphaned resources accumulated release
   over release; nobody's incident, everybody's cost.
3. **A single deployment doubling infrastructure** — replicas or resource requests multiplied by a config
   default; the "incident" is the bill, and detection needs a cost *metric*, not a cost report.

**Why it is hard:** the feedback loop is a month long, so the fix is architectural, not operational: you
have to instrument cost per workload, attribute it, and change defaults so the regression cannot recur. The
political part is that the team causing the spend is not the team paying it.

**STAR skeleton:**
- **S:** ⟨where the spend showed up — a bill line, a budget alert; the number and the month⟩.
- **T:** ⟨the mandate: a target, a deadline, and who owned the constraint⟩.
- **A:** ⟨attribution method — cost per namespace/workload, per-service labels, right-sizing data⟩ → ⟨what
  the data showed: the two or three line items carrying most of it⟩ → ⟨changes: rightsizing, storage class
  and retention policy, egress paths, committed-use or scheduling changes, autoscaling fixes⟩ → ⟨the guard:
  budget alerts, cost dashboards visible to engineering, defaults in the IaC so the regression cannot merge⟩
  → ⟨the pushback you handled: a team whose request you right-sized or a non-production environment allowed
  to be slower⟩.
- **R:** **−25%** (⟨confirm the exact figure and the comparison basis — month-over-month, or versus the
  pre-optimisation architecture? Fix this before telling it⟩), plus ⟨the recurring discipline that kept it⟩.

**Evidence hooks:** the CV's −25% line, Cometh GCP multi-zone, −60% CI build time (same "make it efficient"
thesis), Pub/Sub and etcd in the inventory.

**Drill:** *Against what baseline is the 25%? Did anything get worse — reliability, latency, developer
velocity? How long did the savings hold? What was the cheapest win and what was the expensive one? How would
you apply the same method to a GPU-backed workload, where the unit economics are per-token rather than
per-node?*

**Lane fit:** directly relevant to **#30 Atlantic** (cost optimisation with measured savings is a named
responsibility) and any AI-infra role where inference cost per token is the product's problem. This is the
frame that converts a cost bullet into an engineering story.

---

## 3. The 90-second spine

Every one of the frames above compresses into the same seven beats. Rehearse this order, not a script:

1. **One line of context** — system, scale, your role. (No preamble about the company.)
2. **The symptom as a user would see it** — not "the CNI agent failed".
3. **Blast radius, stated numerically.**
4. **The first ten minutes** — what you looked at, and **the false lead you chased.**
5. **The real cause**, distinguished from the trigger. ("The cert expired" is the trigger; "renewal had been
   failing silently for three weeks because ⟨…⟩" is the cause.)
6. **The fix, and the decision you own** — the judgement call under incomplete data.
7. **The permanent change, with a number** — the runbook, alert, automation or policy that made the class
   recur no more.

The two beats that separate a real story from a rehearsed one are **the false lead (4)** and **the permanent
change (7)**. Interviewers listen for 4 to check you were actually there.

## 4. The drill — questions a sharp interviewer will ask

Answer these *out loud* against whichever frame you pick. Any you cannot answer from memory, check in your
notes or drop the detail.

1. What time of day was it, and who was paged first?
2. What was the first signal, and what alert rule fired?
3. What did you open first, and what did it show?
4. What did you initially think it was — and what ruled that out?
5. What did you try that did not work?
6. What was the trigger versus the underlying cause?
7. Who else was involved, and what did you ask them for?
8. What did you tell stakeholders, when, and what did you not tell them?
9. What decision did you make with incomplete information, and what was the alternative?
10. How long from detection to mitigation, and mitigation to full resolution?
11. What made recovery harder than it needed to be — including something **you** had done earlier?
12. What did you restore, and how did you verify the backup?
13. What alert should have fired earlier, and why didn't it?
14. What was the blast radius numerically?
15. What changed permanently — commit, runbook, alert rule, policy — and can you describe it?
16. What were the post-mortem action items, and how many actually closed?
17. What did it cost — downtime, money, trust?
18. What would you do differently, honestly, and not the humble-brag version?

If a frame cannot answer 5, 11, 13 and 15, it is not a story yet — it is a summary. Go find the detail or
choose a different frame.

## 5. Fill-in checklist per frame

| Frame | Must confirm before use | Drop the frame if |
|---|---|---|
| A — Docaposte cluster recovery | The actual failure (VIP / CNI / etcd / storage), blast radius, MTTR, what changed after | You are reconstructing the CV wording rather than remembering an event |
| B — Cert / ingress cascade | Which endpoint, why renewal failed, alert threshold, permanent fix | You only know that cert-manager exists |
| C — Secrets / access incident | The exposure or finding, rotation order, what broke mid-rotation, audit outcome | You were not the one who led the rotation or the remediation |
| D — Fleet degradation | Which clients/networks, the staging decision, how you cut alert noise, downtime avoided | You cannot name the metric that carried the diagnosis |
| E — Cost | The baseline behind the 25%, the line items, the guard rails, anything that got worse | The 25% was someone else's project |

## 6. One number per story, and it must be yours

Each frame needs exactly one figure you can defend and source: MTTR in minutes, nodes affected, networks
covered, certificates eliminated, systems rotated, percentage saved, backups validated. **If the number is
not in your record, use the qualitative version** ("it never happened again across N environments" → say
"it never happened again") rather than inventing precision. Precision is what gets checked.

## 7. Canonical examples of the same story, in different registers

Same incident, three audiences — pick by room:

**Recruiter screen (30 seconds):** *"I was on call when ⟨system⟩ went down for ⟨scope⟩. I led the response,
found it was ⟨cause⟩, and we were back up in ⟨time⟩. I then ⟨permanent fix⟩ so it couldn't recur."*

**SRE hiring manager (3 minutes):** the seven beats above, with the false lead and the judgement call.

**Platform/architecture interview (5 minutes):** the seven beats, then the design conversation — what you
changed structurally, why the system allowed the failure, and what you would build differently now.

---

*Next step: pick the frames that match events you actually remember, tell me the real trigger, the false
lead and the permanent change, and I will write each one out in the register above. Do not tell a frame
whose slots are still empty.*
