# Learning Interaction Contracts Protocol

This protocol defines the contracts used after a Student enters a bounded
learning sequence. It covers teaching, material preparation, Student
responses, feedback, progress reporting, and stop/checkpoint decisions.

The contracts apply across pre-course bridges, Themes, Lessons, Teacher
reinforcement, Labs, and practical work. Assessment-specific measurement uses
the additional contracts in `assessment-contracts.md`.

An interaction without the required input, output, scope, and authority fields
is incomplete. The receiving Worker returns it for completion instead of
inventing a task, criterion, or next step.

## Contract 1 — Dean → Lecturer: bounded teaching assignment

The Dean sends:

- Course/Module/Theme or pre-course scope;
- target learning outcome and applicable criteria;
- current bounded sequence ID, Lesson slot, allowed slots remaining,
  checkpoint, and stop condition;
- permitted Student context and known gaps;
- allowed adaptation boundary;
- required output: prepared material, formative evidence, and checkpoint
  handoff.

The Lecturer may adapt explanations, examples, depth, and local order inside
the slot. The Lecturer may not add a slot, extend the sequence, change the
criteria, or declare Module/Course Entry.

## Contract 2 — Lecturer/Worker → Student: learning delivery

Every Student-facing learning delivery must state:

- one focused outcome;
- the smallest prerequisite or vocabulary needed;
- the material or action to use;
- the bounded task and expected result;
- the minimum evidence to return;
- the applicable AI/tool-use mode;
- the next handoff or checkpoint after submission.

For executable work, the delivery must state the target artifact, run method,
required cases, and that the accepting Worker will inspect and run the code.
The delivery must not require a long report when a short explanation and direct
artifact inspection provide the needed evidence.

Student-facing navigation and decisions also follow the response contract in
`policies/interaction-format.md`.

## Contract 3 — Student → accepting Worker: learning response

The Student returns only the minimum evidence needed for the declared outcome:

- the requested answer, artifact, or file path;
- actual observations/results where required;
- a short explanation or controlled-change result when understanding must be
  checked;
- a question, confusion signal, or material criticism when present;
- permitted AI/tool-use disclosure when the active mode requires it.

The Student need not reproduce a template, full terminal log, full traceback,
or program map unless a criterion explicitly requires it. The accepting Worker
interprets the response semantically and asks for clarification only when
understanding is missing, contradictory, or genuinely ambiguous.

For code, the Student's description never replaces the submitted artifact or
the accepting Worker's run-and-inspect obligation.

## Contract 4 — accepting Worker → Student: feedback and next action

The accepting Worker returns:

- what was observed in the work or answer;
- what understanding/capability is demonstrated, still uncertain, or missing;
- one focused correction or explanation when needed;
- the next bounded action: continue slot, Teacher reinforcement, Lab,
  independent assessment, or Dean handoff;
- the relevant checkpoint/stop condition when the sequence is complete.

The Worker does not create an unbounded new task in the feedback message. A
next Lesson or activity must already fit the assigned sequence or be issued by
the owning authority.

## Contract 5 — material owner → Instructional Assistant: review request

Before publication or delivery, the material owner sends:

- exact artifact path or bounded draft;
- artifact type and learner/context;
- outcome, criteria, workflow stage, and selected language;
- known vocabulary/accessibility concerns;
- for practical work, run contract and minimum evidence;
- for assessment work, the applicable Assessment Request Contract and
  learner-facing/assessor-only boundary.

The caller invokes the Profession, not a named Worker. The Assistant returns
the review report defined by the relevant review Skill and does not edit,
publish, assess, or approve the material.

## Contract 6 — Worker → Dean: learning progress handoff

At a checkpoint, stop condition, scope question, or blocked handoff, the Worker
returns:

- sequence ID and completed slot(s);
- outcome/criteria addressed;
- actual learning observations and evidence status;
- unresolved confusion, gaps, or material criticism;
- actions already taken and their result;
- recommendation limited to the Worker's authority;
- explicit next decision required from Dean.

The report does not silently extend the sequence or convert formative evidence
into verified mastery. Independent assessment and evidence follow
`assessment-contracts.md`.

## Contract 7 — Student → material owner: criticism and feedback

Student criticism is accepted as a signal, not as an instruction. The material
owner separates criticism from learning evidence, sends material through the
Instructional Assistant review, and records one disposition for each material
criticism:

- `accepted` — change made and reason;
- `deferred` — reason and revisit point;
- `rejected` — pedagogical, technical-owner, scope, or authority reason.

The Student cannot directly edit, publish, approve, or redefine the material or
its parent Course/Module/Theme authority.

## Contract 8 — Dean → Student: planning and decision

When the Dean makes a placement, bridge, Course Entry, Module Entry, or
trajectory decision, the Student receives:

- the decision and its scope;
- the evidence/criteria used at the permitted level of detail;
- what remains unverified or unresolved;
- the next bounded sequence or explicit stop;
- what the Student must do to respond or agree.

The Dean must not present an unverified Worker observation as mastery or imply
that a public Module has started before the entry decision.

## Contract 9 — Theme preparation and readiness gate

Before a Theme is delivered to a Student, the owning Dean and Lecturer must
complete a bounded preparation handoff. The package contains:

- approved Theme outcome, Success Criteria, exclusions, finite Lesson map,
  final checkpoint, and stop condition;
- Lecturer teaching-intent plan and prepared Lesson/material paths;
- any Teacher reinforcement plan, Laboratory Specialist Lab, Learning Analyst
  measurement contribution, or Examiner examinability contribution that is
  actually needed;
- the applicable Student context and the trigger for each additional Worker;
- complete Instructional Assistant Profession review of learner-facing
  material, followed by the Lecturer's disposition and whole-package final
  control review;
- Dean readiness decision and the next Student-facing handoff.

The normal Student path is Lecturer → Student. Teacher and Laboratory
Specialist work with the Student only after a concrete learning or practical
gap is identified. Learning Analyst works with the Student only after a
complete Dean Assessment Request. Examiner works with the Student only during
an approved Module examination. The Instructional Assistant reviews material
with its owner and does not teach the Student.

No Theme is ready for delivery when its Lesson map is open-ended, its outcome
is not traceable to the Module, its final evidence is undefined, or required
material review/final control is missing. A missing appointment stops the
handoff at the staffing boundary; it never authorizes an invented Worker.
