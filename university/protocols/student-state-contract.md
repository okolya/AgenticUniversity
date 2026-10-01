# Student State Contract

Host-neutral description of private Student state. It defines what state
exists, who may read or write it, and the invariants every store must keep.
It grants no authority: authority comes from `policies/student-state-authority.md`,
the active Profession, Workflow, and Policy. The contract is derived from the
state the University already records; it adds no academic meaning.

A **state store** is any implementation of this contract. Two are recognized:

- the private core-relative `students/` Git repository of Markdown files (CLI
  hosts);
- any other store a host provides (for example a database) that keeps the same
  entities, operations, and invariants.

Skills and Workflows name contract operations, never store paths. "The
private Student workspace" in workflows means the state store.

## Machine-readable form

`schemas/student-state.schema.json` (JSON Schema) is the machine-readable form
of this contract, with a synthetic `schemas/student-state.example.json`. Each
written entity carries `recorded` (acting Profession, workflow, date). Where the
schema and this prose disagree, this prose and the authority policies govern;
fix the schema. `make check-manifest` validates the example against the schema.

## Entities

| Entity | Holds | Notes |
|---|---|---|
| Student | id, status (`registered`, ...), goals | one per real Student; isolated from all others |
| Enrollment | public route reference, mode, status (including `COMPLETED`), rationale, prior context, unconfirmed capabilities, next actions | references a public Course/Module; never copies its definition |
| Plan | kind (Module learning plan, application plan, certification plan), purpose, verified-and-not-repeated items, coverage, capacity, dates, actual progress, current Lesson reference, checkpoint, stop condition, next actions, adaptations, status | Student-specific plans (`workflows/learning-plan.md`, `workflows/module-exit.md`); the public frame stays in `university/` |
| Evidence | date, workflow, criteria references, artifact reference, observed, demonstrated, evidence status, limitation, handoff | one entry per assessment or practical result; also carries criterion-level findings, gaps, retention findings, competency verification, and Module verdicts |
| Decision | date, deciding Profession and scope, decision, conditions carried forward | Dean placement/entry decisions and agreed trajectory |
| Note | free text | only private Student-specific educational facts |
| Registry | list of registered Students routing to their state | an index, not a copy of Student state |

There is no separate Mastery entity. Verified mastery is what verified
Evidence for assigned criteria supports; nothing is stored as mastery unless
an authorized Evidence or Decision entry records it.

An **artifact reference** identifies a submitted Student artifact (for example
code) independently of where it is stored. It is opaque to the contract: a path
in a CLI store, an object key in another. Evidence without a retrievable
artifact cannot support executable work under `policies/practical-work.md`.

Artifact handling. A host that accepts executable or document work from a
Student provides artifact storage and retrieval: the submitted artifact is kept
under its artifact reference, stays retrievable by the Worker who accepts it,
and the Evidence entry links to it. The artifact belongs to the Student's
private state and is never published or shown to another Student. A host
without artifact storage cannot accept work that needs inspection; it follows
`policies/practical-work.md` (non-executing task or deferral).

A **public entity reference** is a stable, slash-separated identifier of a
public University entity:

```text
<course>/<module>/<theme>/<lesson>
```

For example:
`ai-engineering/module-01-python-ai-engineering/theme-01-python-components/lesson-01-separate-function-responsibilities`.
References must not omit the owning Course or Module and must not depend on a
host filesystem prefix. A host resolves the identifier against its canonical
`university/courses/` tree before presenting or using it.

## Operations

| Operation | Effect | Used by |
|---|---|---|
| `read` (Student, selectors) | returns only the requested entities/sections | `inspect-student-state` |
| `initialize-student` | creates Student and Registry entry with id, status, goals | Rector, `workflows/student-initialization.md`; a non-CLI host performs it on the Student's sign-up request under the Rector's authority |
| `record-enrollment` | creates or updates Enrollment and its agreed Plan | `create-enrollment` (Dean) |
| `update-plan` | changes Plan progress, next actions, adaptations | Dean; teaching Workers return progress observations to the Dean, they do not write the Plan |
| `append-evidence` | adds an Evidence entry | `update-evidence` (Learning Analyst, Examiner) |
| `record-decision` | adds a Decision entry | Dean |
| `complete-enrollment` | marks an Enrollment completed when its plan is resolved | Dean |
| `add-note` | adds a Note | Dean or Rector for their own decisions and metadata; other Workers' formative observations are recorded only through an authorized Dean or Learning Analyst write |

Every write carries the acting Profession, the active Workflow, and a date.

## Authority

Write authority is exactly the table in `policies/student-state-authority.md`:

- Lecturer, Teacher, Laboratory Specialist — formative observations only; never
  verified mastery;
- Learning Analyst — `append-evidence` for assigned assessment criteria;
- Examiner — `append-evidence` and the Module verdict under `module-exit`;
- Dean — `record-enrollment`, `update-plan`, `record-decision`,
  `complete-enrollment`; never rewrites independent Evidence or verdicts;
- Rector — `initialize-student` and high-level goals;
- Dean and Rector — `add-note` for their own decisions and metadata only
  (as in the Operations table; no additional authority).

A Skill never gains authority by invoking an operation.

## Invariants

1. **Isolation.** A read or write is scoped to one Student. Access to one
   Student never grants access to another.
2. **Minimum context.** `read` returns only what the active workflow and
   appointment scope need.
3. **Reference, don't copy.** State refers to public entities by reference and
   never embeds their definitions.
4. **Evidence is append-only.** Independent Evidence and verdicts are not
   rewritten; a correction is a new entry that refers to the earlier one.
5. **No invention.** Missing state is reported as missing; no fake Student,
   enrollment, evidence, or mastery is created.
6. **Privacy.** Private state is never promoted into public University
   knowledge (`policies/knowledge-and-state-ownership.md`).
7. **Verify after write.** After a write the caller reads back the affected
   state (`protocols/artifact-verification.md`); a Worker or Skill report is not
   proof.

## CLI store mapping

In the core-relative `students/` repository each Student has one
`students/<id>/STUDENT.md`;
`students/registry/REGISTRY.md` is the Registry.

| Entity | Location in `STUDENT.md` |
|---|---|
| Student | `id`, `status`, `## Goals` |
| Enrollment | `## Active enrollments` |
| Plan | `## Active Module 1 plan` style sections (`## Active <scope> plan`) |
| Evidence | `## Independent evidence` |
| Decision | `## Dean decision — <date>` sections |
| Note | `## Notes` |

Artifact references in Evidence are repository-relative paths (for example
under `homeworks/`). The template is `templates/student-state/STUDENT.template.md`.
