# Theme 3 — Runtime, project, configuration, and dependency boundaries

- **Module:** Python AI Engineering
- **Owner:** assigned Engineering Faculty Lecturer
- **Status:** bounded four-Lesson sequence approved; detailed Lessons are authored just in time

## Boundary

Make a Python component reproducible and safe to configure. Cover entry points,
project layout, runtime/dependency assumptions, example/local configuration,
and secret separation. Do not expand into cloud or platform operations.

## Theme outcome

The Student can run a component from a documented setup while keeping local
values and secrets outside shareable source and version history.

## Success criteria

- source, configuration, dependencies, and local values have explicit roles;
- the example configuration is valid and shareable;
- local configuration is excluded from version control;
- the run command and runtime assumptions are reproducible.

## Complete Lesson sequence

This Theme contains exactly four Lessons:

1. define a small project layout and its executable entry point;
2. separate source, example configuration, local configuration, and secrets;
3. state runtime and dependency assumptions and reproduce the run command;
4. complete a bounded reproducibility/configuration component and return the
   Theme evidence.

## Theme checkpoint and stop condition

The final artifact must run from a documented command, contain a valid
shareable example configuration, keep local values outside version control,
and state its runtime/dependency assumptions. After Lesson 4 the Lecturer
returns evidence to Dean; no fifth Lesson is created without a new Dean
decision. Cloud, container-platform, or deployment work is outside this
Theme.

## Lecturer handoff

The Lecturer prepares these four Lessons only, uses the existing
Git/configuration evidence as context rather than repeating entry work, and
returns the final evidence to Dean. Any need to add deployment scope returns
to Dean.
