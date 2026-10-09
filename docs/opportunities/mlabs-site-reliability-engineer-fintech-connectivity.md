# MLabs (agency) — Site Reliability Engineer, fintech connectivity client (Remote First)

**Posting:** https://www.linkedin.com/jobs/view/4470903654/ (LinkedIn job id `4470903654`, posted ~1 month
before reading, "be among the first 25 applicants")
**Agency:** **MLabs Ltd** (`mlabs.city`, LinkedIn `mlabsconsulting`) — an agency that also runs technology
consulting. Contact address given for HR and data-protection requests; no named recruiter on the post.
**Client:** **unnamed** — *"a fast-growing financial technology company that provides high-performance
integration and hosted connectivity services to global trading venues and financial institutions"*. i.e.
**market-connectivity infrastructure**: hosted/cross-connect environments, exchange connectivity, network
engineering for trading venues.
**Market:** **EU-remote** ("Remote First. Hiring in Europe, UK, NY, and Canada.") · **Tier:** **C** (bridge) ·
**Channel:** **recruiter** (the 10% lane) · **Track:** `bridge`
**Seniority:** "Permanent | Full-time"; LinkedIn's "Berufseinstieg" (entry level) tag is a scraping artefact
and contradicts the JD's scope.
**Applied:** ✅ **2026-10-09** · **Stage:** Contacted · **Issue:** #34
**Compensation:** ✅ **£90,000 – £120,000 published**, plus company share options and a benefits package.
At ~£1 ≈ €1.12–1.18 `[INFERENCE — no FX source consulted]`, that is roughly **€101k–€142k**, comfortably above
the **€80,000** EU-remote floor (§2). **The first row in the pipeline whose compensation is published by the
employer and verifiably clears the floor.** Caveat: quoted in **GBP**, which points to a UK contracting entity —
see the location question below.
**Follow-ups:** 1st due **2026-10-16 → 2026-10-20** · final **2026-10-23 → 2026-10-29**
**jobradar:** no store row (agency posting, not an employer ATS board). MLabs is not tracked.

## Hard-filter checklist (§2)

- [x] Not Staff/Principal — SRE with broad ownership, no staff scope claimed
- [x] **Compensation ≥ €80k (EU-remote)** — ✅ **published and clearing**, the first verified pass in the
      pipeline. Directly relevant to the income cliff: this is the fastest-to-income shape on record
- [ ] Geography / remote start — ⚠️ **partially verified.** Remote-first, hiring across **Europe** (contains
      France) so the posting is in scope. But the **band is quoted in GBP** and the agency is UK-based, so the
      **employing entity is probably UK** — a UK contract held from France is a different thing from French
      employment, and it is unverified which is on offer. **Ask first, in writing**
- [x] No day-one GPU / training / serving requirement — no ML surface in the JD
- [x] Architectural scope — provisioning pipelines for servers **and networks**, CD automation reaching
      **network switches**, shared ownership across the whole environment

**Verdict: admissible, `bridge` track, and the best-verified compensation in the pipeline. The binding unknown
is contractual (UK entity vs French employment), not technical.**

## Craft read

| JD requirement | Candidate evidence |
|---|---|
| **Automation: Ansible** (essential) | ✅ CV and `CONTEXT.md` both claim Ansible IaC at Docaposte (*"standardized and hardened infrastructure deployed via Ansible"*). ⚠️ **Reconciliation item:** Ansible does **not** appear in `docs/tooling-inventory.md`, whose Docaposte table lists only MetalLB, Cilium and HAProxy. The claim is defensible from the CV bullet and `CONTEXT.md`; the inventory needs the row added so the depth is defensible in interview |
| Scripting / software from scratch in a language of choice | ⚠️ **the honest split**: operational scripting yes, **production software authorship is an excluded claim**. The process includes a **2–3 hour practical/coding exercise**, so this will be tested, not just discussed |
| **Combined systems + network engineering** | ✅✅ **the strongest match and a genuine differentiator**: Cilium CNI and network policy, MetalLB, HAProxy, Traefik, Kong, nginx ingress, TLS automation (cert-manager), multi-zone and bare-metal networking, DNS. Most cloud-only SREs cannot answer this section at all |
| Automated provisioning across **physical data centres and cloud (AWS, GCP)** | ✅ physical/bare-metal (Docaposte: MetalLB, Cilium, HAProxy on bare metal) and GCP multi-zone (Cometh) ✅✓. ⚠️ **AWS absent** — the third JD today (with Runware #32 and SpotMe #33) requiring AWS, which is not in the evidence base |
| CD pipelines automating software, server setup and **network switches** | ✅ Drone CI `deployed`, GitHub Actions `used`, Flux/Argo CD GitOps, config-as-code habits ✅✓. ⚠️ **switch automation unverified** — no Cisco/Juniper/Napalm/NetBox-class tooling anywhere in the inventory |
| **Vendor & partner interaction**: hardware vendors, telecom providers, financial institutions; **procurement, negotiating agreements, purchasing hardware** (essential) | ❌ **the largest gap, and it is listed as essential.** Nothing in the evidence base covers procurement, vendor negotiation or service delivery oversight — no inventory row, no CV bullet. This is a distinctive part of the job (a small infrastructure team that buys its own hardware and circuits) and the candidate has no receipts. Do not improvise a claim here; ask how much of the week it actually is |
| HA database architectures, clustering, replication (PostgreSQL) | ✅ PostgreSQL `deployed` across two employers, Redis, Elasticsearch ✅✓. Clustering/replication depth in production: ⚠️ partial |
| Authentication protocols: SAML, OAuth2, AD, Kerberos; Azure AD | ⚠️ adjacent only — **Teleport** (identity-aware access) and Vault are deployed, which is the right instinct but not the named protocols. Azure AD not evidenced |
| Autonomy, self-motivation, continuous learning | ✅ production SRE across three employers and three regulated/novel domains |
| Financial institutions as customers; high-stakes environments | ✅ analogous: Kiln ($8B+ secured), HDS-regulated healthcare at Docaposte, ISO 27001 lead |

## Risks, stated plainly

1. **Agency + unnamed client.** The ad *"regret[s] that we are unable to provide individual feedback"* and sets
   an explicit **4-week silence rule** — after four weeks, assume rejection. Also unverified: is this **direct
   employment with the client**, or an **MLabs placement/staff-augmentation** arrangement? The agency runs its
   own consulting business, so the difference matters.
2. **GBP band → UK entity.** If the contract is UK-based, working from France raises tax, social-security and
   permanent-establishment questions that are not the employer's problem to solve for a remote hire. Ask early
   and get it in writing.
3. **Procurement and vendor negotiation are essential and unevidenced.** This is the requirement most likely to
   eliminate, because it is unusual and cannot be inferred from infrastructure work.
4. **AWS absent** — third such JD in one day.
5. **Coding exercise (2–3h)** in the process, against the Python/software-authorship exclusion.
6. **Network switch automation** is real work in this role (configuring switches, not just load balancers) and
   the evidence covers the CNI/LB layer rather than the switch layer.
7. Trading-venue connectivity implies **market-hours sensitivity**; the ad does not mention on-call, which is
   worth asking about rather than assuming either way.

## What is genuinely attractive

- **First published, floor-clearing compensation in the pipeline.** Every other row has no band or an inferred
  one; here the employer states £90–120k. On the income cliff, that converts directly into the fastest path to
  income (Earliest-Start Rule).
- **Network engineering is the differentiator, not a gap.** The role explicitly wants systems **and** network
  depth; the Cilium/MetalLB/HAProxy/Traefik/Kong/nginx evidence set is unusual among SRE candidates and matches
  what a connectivity provider actually runs.
- **Physical data centres plus cloud** — bare-metal and on-prem history is directly relevant, and this is not a
  cloud-only shop.
- **Trading infrastructure is high-stakes reliability work** of the same kind as `$8B+` secured across 40+
  networks, with financial-institution customers where compliance and auditability matter — the ISO 27001 and
  HDS background transfers.
- Remote-first across four regions, an explicit process with defined stages, and a stated salary band — the
  clearest, most professional hiring process reviewed so far.

## Questions to put in writing (first follow-up)

1. **Which entity employs** — UK, another European country, or an employer-of-record for France? And is the
   arrangement direct with the client or through MLabs?
2. Is the £90–120k band **base**, and does it vary by country of residence?
3. **How much of the week is procurement and vendor management** versus hands-on infrastructure work?
4. Does the role require **network switch configuration** directly, and on which platforms?
5. Is the **coding exercise** infrastructure scripting or application software?
6. On-call: is there a rota, and does it follow market hours?
7. Which parts of the estate are physical data centres versus AWS/GCP?

## Timeline

- Contacted / applied: **2026-10-09** (LinkedIn, via MLabs)
- Follow-up 1 due (5–7 business days): **2026-10-16 → 2026-10-20**
- Follow-up 2 due (10–14 business days): **2026-10-23 → 2026-10-29** (final)
- Screen date: —
- Interview dates: —
- Outcome: pending

## Outcome record

- Stage reached: Contacted
- Salary: **£90,000–£120,000 published by the employer** (first verified floor-clearing band in the pipeline)
- Rejection reason (relevance / readiness / compensation / location / unknown): pending
- **Watch:** compensation cannot be the reason this one ends — the floor is cleared by a published band. The
  elimination set is therefore **relevance** (vendor management/procurement, software authorship, AWS) or
  **contractual** (UK entity from France). Like Runware #32, this is a row whose failure, if it comes, will be
  interpretable.
- What would have changed the outcome: —

## Funnel delta

Applications sent +1 (2026-10-09) · **EU-remote lane** · `tier:c` · `track:bridge` · **`channel:recruiter`** —
third recruiter-lane row (after #13 Bubblemaps and #31 Annapurna), moving that lane from ~7% toward its 10%
allocation. Second `bridge` row today, third application overall.
