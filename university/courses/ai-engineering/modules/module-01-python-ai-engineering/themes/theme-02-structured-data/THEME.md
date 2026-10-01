# Theme 2 — Structured data and validation

- **Module:** Python AI Engineering
- **Owner:** assigned Engineering Faculty Lecturer
- **Status:** approved frame and prepared materials; Dean readiness recorded

## Boundary

Read, validate, transform, and serialize structured data while preserving
types and invariants. Do not expand into databases or model training.

## Theme outcome

The Student can define a small data shape, validate it, transform it, and
report invalid data without silently changing its meaning.

## Success criteria

- required fields and expected types are explicit;
- valid and invalid data paths are both tested;
- serialization preserves the stated structure;
- the Student explains the limits of the validation performed.

## Complete Lesson sequence

This Theme contains exactly four Lessons:

1. identify a small structured data shape and read it without losing types;
2. validate required fields, types, ranges, and invalid input;
3. transform and serialize the data while preserving its declared structure;
4. complete a bounded data-validation component and return the Theme evidence.

## Theme checkpoint and stop condition

The final artifact must read, validate, transform, and serialize one bounded
data structure, demonstrate valid and invalid cases, and state the limits of
its validation. The accepting Worker runs and inspects the artifact. After
Lesson 4 the Lecturer returns evidence to Dean; no fifth Lesson is created
without a new Dean decision.

## Sequence traceability

Theme 2 advances Module 1 Exit Contract criteria 4 and 6: deliberate handling
of invalid behavior, and reading/validating/transforming/serializing structured
data while preserving types and invariants.

| Lesson | Consumes | Adds | Enables |
|---|---|---|---|
| 1 — read | Module 1 basic file/command skills | JSON object and Python type mapping | explicit schema validation |
| 2 — validate | Lesson 1 parsed object | required fields, exact types, and range invariants | safe transformation |
| 3 — transform/serialize | Lesson 2 validated object | non-mutating status transformation and JSON output | integrated pipeline |
| 4 — checkpoint | Lessons 1–3 complete pipeline | bounded transfer, invalid-output boundary, and validation-limit evidence | Contract 6 handoff to Dean |

No Lesson is an independent restart. A later Lesson must consume the prior
artifact/result and add the next Theme criterion.

## Lecturer handoff

The Lecturer prepares these four Lessons only, invokes the Instructional
Assistant before each delivery, and returns the final evidence to Dean. A
database, model-training, or new data domain is a scope change and returns to
Dean.

After the Instructional Assistant review and the Lecturer's final source
control, the Lecturer invokes the Translator Profession for the Ukrainian
native-language and anglicism audit. The Translator preserves exact code/API
names, commands, paths, and required output strings, while the Lecturer remains
responsible for technical and academic meaning. A second Assistant review is
needed only for a material learner-path change or flagged clarity risk.
