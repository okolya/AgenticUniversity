# Assessment Contracts Protocol

This protocol governs the handoff from a Dean's academic decision to an
independent assessment and back. It applies to Course Entry, prerequisite,
gap, Theme, re-assessment, and retention diagnostics.

No assessment artifact may be created, published, or conducted when the
required contract fields are missing. A Worker returns an incomplete handoff
to its caller instead of inventing the missing scope or decision authority.

## Contract 1 — Dean → Learning Analyst: Assessment Request

The Dean owns and sends the request. It must contain:

- target Course/Module/Theme and exact Entry or Success Contract criteria;
- purpose: Course Entry, Module Entry, gap, re-assessment, retention, or other
  authorized measurement;
- the specific uncertainty or missing evidence to resolve;
- permitted Student context and privacy boundary;
- bounded assessment scope, allowed artifact/attempt limits, and stop condition;
- applicable AI/tool-use mode;
- required handoff stage and the fact that Dean retains placement and
  trajectory authority.

The Dean defines what must be measured, not the solution, lesson sequence, or
assessment implementation. The Dean must not write the assessment artifact as
a substitute for this request.

## Contract 2 — Learning Analyst: Assessment Artifact

The authorized Learning Analyst receives a complete request and creates the
learner-facing artifact under the relevant public Course, Module, or pre-course
path. The artifact must identify:

- purpose and target capability in learner language;
- exact task, inputs, outputs, failure/boundary cases, and evidence required;
- bounded scope, allowed tools, AI-use mode, and attempt limits;
- learner-facing instructions separately from assessor-only criteria;
- the accepting Profession/Worker and the run/inspection method when code is
  submitted;
- what the artifact does not assess.

The Analyst may choose the measurement method and task design within the Dean's
criteria, but may not change the criteria, placement authority, or trajectory.
The Analyst invokes the Instructional Assistant before publication or delivery
and completes the final assessment-owner review after receiving the report.

## Contract 3 — Instructional Assistant → Assessment Owner: Review Report

The Assistant receives the complete artifact, Contract 1, the assessment
criteria, the permitted learner context, and the applicable AI-use mode. The
Assistant returns:

- intended learner outcome and workflow stage;
- vocabulary, language, prerequisite, and cognitive-load findings;
- practical-task clarity and evidence-burden findings;
- for executable work, whether run-and-inspect and a minimal understanding
  check are explicit;
- questions and concrete revision suggestions;
- pedagogical readiness: `ready`, `ready_with_changes`, or `not_ready`.

The Assistant does not edit, publish, validate technical correctness, validate
assessment scoring/independence, inspect private evidence, or issue a verdict.
The Analyst decides how to apply the report and records the final review.

## Contract 4 — Learning Analyst → Dean: Assessment Evidence Handoff

After independent measurement, the Analyst returns:

- the request and criteria measured;
- artifact path and assessment mode;
- observed evidence, including actual runs and inspected files for executable
  work;
- criterion-level result: demonstrated, not demonstrated, or uncertain;
- Student explanation/controlled-change observations where used;
- environment or execution limitations;
- unresolved gaps and uncertainty;
- explicit statement that the Analyst did not choose placement or trajectory.

The Dean interprets the evidence and decides Course Entry, Module Entry,
bounded bridge, further measurement, or another permitted trajectory. The Dean
does not rewrite the Analyst's evidence or verdict.

## Contract validation

The Worker Activation Protocol must carry the applicable contract with every
assessment delegation. Profession routing resolves the Dean, Learning Analyst,
and Instructional Assistant separately; a single runtime agent must not silently
perform all three authorities.
