# Writing style — application answers and candidate-voice copy

Rule file for any agent drafting text in Vincent's applicant voice (application answers, outreach
messages, cover letters, LinkedIn copy, CV bullets). The failure mode this exists to prevent: answers
that read like a strategy memo instead of a candidate answering a question.

## Two registers — do not mix them

| Register | Where | Style |
|---|---|---|
| **Applicant voice** | Anything a recruiter reads | Direct, concrete, short. Every sentence carries a fact or a decision. |
| **Agent voice** | This repo's internal docs, notes, rationales | Explanatory is fine; still no padding. |

## Hard rules for application answers

1. **Word budget.** Each answer ≤ 100 words unless the question asks for detail. A labeled list
   (one `**Label:** a · b · c` line per category) is exempt from the cap — keep it ≤ 6 lines.
2. **One paragraph. No structure theatre.** No headers, no bullets, no "Two things:" sign-offs.
3. **Concrete nouns only.** Companies, numbers, technologies, outcomes. Delete abstractions that
   don't carry a fact: "the production substrate", "blast radius of a degraded dependency",
   "reliability discipline", "moving real money".
4. **No rhetorical contrasts.** Ban "not X, it was Y", "the safest change is the boring one",
   rule-of-three flourishes, and closing aphorisms.
5. **No narrative openings.** Never start with scene-setting ("My high-traffic work has been in
   environments where…"). Start with the fact.
6. **Em-dash budget: zero** in application answers. Use commas or separate sentences.
7. **No hedging.** Cut "I believe", "I would say", "essentially", "fairly", "quite".
8. **Do not restate the question** before answering it.
9. **Lists are flat.** One line per item, one item per line. No sub-bullets, no parenthetical
   justification, no "because" clauses inside a list.
10. **Every figure is verifiable or bracketed.** Use `⟨placeholder⟩` for anything Vincent must
    confirm. Never invent metrics.

## Rewrite examples

| Don't | Do |
|---|---|
| "Traffic there was not user-facing HTTP: it was sustained protocol-level traffic across dozens of live networks." | "Sustained protocol-level traffic across 40+ live networks." |
| "The reliability work followed from scale: I standardized observability… which cut MTTR" | "Standardized observability (Prometheus, Grafana, OpenTelemetry, ELK); cut MTTR." |
| "cost at scale is an architecture signal, not a purchasing one" | (delete) |
| "Python (scripting and automation) · Go (working knowledge)" | "Python · Go (working knowledge)" |
| "Reliability practice: incident response · MTTR reduction · production hardening · capacity planning · cost optimization · security-hardened environments (ISO 27001, HDS)" | "Incident response · capacity planning · cost optimization · ISO 27001 / HDS" |

## Free-text fields are prose, not a keyword list

A cover letter, a "why are you suitable" box, or any free-text application field is **read by a human
who already has your CV**. Restating the tool list there adds nothing and reads as filler.

- **Do not enumerate tools.** The CV carries the stack. Name at most one or two tools, and only when
  the sentence needs them to make sense.
- **Write outcomes and ownership.** What did you own end to end, what changed because of you, what was
  the hard part.
- **Natural sentences.** If a paragraph reads like a skills matrix with verbs attached, cut it.
- **Say the one or two things only you can say.** Regulated-environment work, payment or transaction
  scale, ownership of a production path — pick the genuinely differentiating facts.
- **Admit a real gap in one sentence** when the JD has a hard requirement you lack. Interviewers find
  it anyway; naming it first reads as confidence.

**Before → after:**

| Don't | Do |
|---|---|
| "run the full observability stack (Prometheus, Grafana, OpenTelemetry, ELK, Loki)" | "made production systems observable enough that MTTR dropped" |
| "deployed and operated platform tooling — Flux, cert-manager, Velero, Teleport, SOPS, External Secrets" | "built the internal platform other teams deployed on" |
| "Terraform IaC and Helm charts at multi-environment scale" | "owned infrastructure as code across several environments" |

## Self-check before delivering

- Count the words. Over budget → cut the weakest sentence, don't compress words.
- Read aloud. If a sentence sounds like a TED talk, delete it.
- Ask: could each sentence survive an interviewer asking "specifically?" If no, cut or add the specific.
