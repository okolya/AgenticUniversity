# University execution ontology

This document fixes the meaning of the core execution concepts so responsibilities do not drift.

- **Profession** — reusable academic authority and responsibility template. A runtime agent represents a Profession.
- **Worker** — named appointment of one Profession in a concrete scope. A Worker is context, not a runtime agent.
- **Faculty / scope** — domain context in which a Worker is appointed. It supplies domain boundaries, not Profession authority.
- **Skill** — bounded reusable capability used by an active Worker as a tool. A Skill never owns a workflow and never grants academic authority.
- **Workflow** — ordered transfer/sequence of academic responsibility. A workflow says who owns each stage and which bounded operations may be used.
- **Policy** — non-optional constraint or authority rule. A Skill or Worker cannot override a Policy.
- **Protocol** — cross-runtime contract for activation, delegation, or boundary crossing.
- **Deterministic tool/script** — technical implementation utility. It may execute a repeatable operation but has no academic authority.
- **Runtime adapter** — Claude/Codex/Cursor representation of a Profession. It is not canonical academic truth.

## Composition

`Profession + Faculty/scope + Worker appointment + Worker additions + active Workflow + Policies + permitted context = acting Worker`

Worker additions are additive. They may narrow scope or add capabilities, but may not silently remove Profession duties, weaken Policies, or expand appointment authority.

## Non-equivalences

- Worker != Agent
- Skill != Agent/Subagent
- Skill != Workflow
- Workflow != Policy
- Faculty specialization != Profession
- Evidence != trajectory decision. Learning Analyst produces verified evidence/findings; Dean owns placement/progression planning; Examiner owns the final Module verdict.

## Curriculum ownership

A Course is a Faculty-owned public academic structure. The appointed Dean owns and approves its stable architecture. Subject specialists may contribute proposals and evidence, but contribution does not transfer ownership. Detailed Module content is adaptive and created/refined just in time. See `university/policies/curriculum-authority.md`.

## Module competency contract

A Module competency contract is a Dean-owned public boundary consisting of purpose, Entry Contract, Exit Contract, broad competency areas, and hard dependencies. It makes a Module navigable and assessable before Themes, Lessons, exercises, labs, or materials exist. Module relationships are defined by competency requirements, not mandatory prior content consumption.


## Module versus Student Module Enrollment

`Module` is a public, reusable University academic object. `Student Module Enrollment` is private Student state describing one Student's traversal of that Module. Examination, application/certification activity, and completion states belong to the enrollment. The public Module accumulates reusable knowledge and may evolve; it is not closed by Student completion.
