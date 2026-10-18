# ADR 0011: Complete material-preparation gate

- Status: accepted
- Date: 2026-10-02

## Context

ADR 0010 permits public Lessons to be prepared ahead of Students inside a
Dean-approved Theme frame. The related requirements existed in several places:
`theme-design.md` required research, provenance, review, and final control;
`lesson-preparation.md` described the individual Lesson sequence;
`learning-material-review.md` required an Assistant review and owner review;
and `theme-record-contracts.md` defined Theme-local records.

Those requirements were distributed rather than expressed as one completion
gate. A Worker could therefore author Lessons, use multimedia curation, and
pass repository structure checks while still omitting the research record,
Instructional Assistant review, owner disposition, or final preparation record.
The repository checks validate core structure, not completion of an academic
workflow.

## Decision

Introduce one reusable **complete material-preparation gate** for a public
Theme package or a materially revised learner-facing Lesson package.

Before a responsible academic owner may describe the package as `ready` for
ahead-of-student preparation or proceed to delivery preparation, the package
must have an auditable sequence:

1. **Scope handoff** — Dean-approved Theme frame, finite Lesson map, outcome,
   criteria, exclusions, checkpoint, stop condition, and responsible
   Profession are identified.
2. **Research decision** — suitable existing sources are researched when
   relevant; each retained, rejected, or unnecessary source has a bounded
   reason. `research-materials` is used when current public sources matter.
3. **Multimedia decision** — `curate-multimedia` is used when audio, image, or
   video could materially support the outcome; every proposal records role,
   exact fragment, learner action, accessibility, provenance, risks, and
   fallback. “No multimedia needed” is also a valid recorded decision.
4. **Authoring** — the Lecturer authors only the approved slots, records each
   Lesson's new evidence delta and dependency, and records exact provenance for
   external or Student-provided material.
5. **Pedagogical review** — the responsible owner invokes the Instructional
   Assistant Profession for the complete package, not only a selected Lesson.
6. **Disposition and final control** — the owner records every finding as
   accepted, deferred, or rejected with a reason, applies justified changes,
   rereads the complete final source, and checks outcome, prerequisites,
   sequence, vocabulary, evidence instructions, provenance, accessibility,
   AI-use boundaries, and scope.
7. **Required specialist/language handoffs** — Translator, Teacher,
   Laboratory Specialist, Learning Analyst, or Examiner is invoked when its
   trigger exists; otherwise the preparation record states why it was not
   invoked. A missing required appointment stops the gate.
8. **Readiness record** — `theme-preparation-record.md` and
   `material-review.md` record the evidence bundle, `unpiloted` status, open
   Student-specific checks, and the next stop/decision boundary.

The gate has two distinct outcomes:

- `ready` for ahead-of-student preparation: the public package is coherent and
  reusable, but remains `unpiloted`;
- `not_ready` for Student delivery until the owner checks the Student's
  verified evidence, omitted criteria, and new evidence delta.

Git hooks and `29/29` core checks remain repository integrity checks. They do
not grant academic readiness and do not replace this gate.

## Consequences

- `theme-design.md` and `lesson-preparation.md` use the same ordered gate.
- `theme-record-contracts.md` makes the research/curation decision and the
  owner completion record explicit, without imposing a fixed Lesson template.
- `learning-material-review.md` remains the detailed review workflow; this ADR
  adds the cross-stage completion boundary rather than duplicating its review
  rules.
- A Worker may commit an in-progress package for collaboration, but must not
  label it `ready` or deliver it as complete until the record shows the gate.
- Existing historical Theme records are not silently rewritten by this ADR.
  The gate applies to new preparation cycles and materially revised packages;
  an existing Theme must be brought to the new record contract before its next
  readiness claim or Student delivery.
- No Student state, academic authority, Course scope, or assessment
  independence changes.

## Scope boundary

This decision governs preparation evidence and readiness claims for public
learning material. It does not make repository checks semantic, require every
Lesson to use one document template, or authorize a Worker to change a
Dean-owned Theme, Module, Course, or Student decision.
