---
name: evaluate-exercise
description: Evaluate an exercise result against explicit criteria and return observations/evidence to the active Worker.
---
# Evaluate exercise

Evaluate an exercise result against its approved parent scope and explicit
criteria and return observations/evidence to the caller. For executable work,
inspect and run the submitted artifact before forming an observation. The Skill
does not open a new Lesson, Theme, or progression decision.

## Contract

Input must include the active Worker, parent Course/Module/Theme/Lesson scope,
purpose, target artifact/path, run command or permitted execution method,
applicable success criteria where relevant, policy/mode, and only the Student
context required for the operation.
Output is returned to the calling Worker; the Skill does not assume the
Worker's academic authority.

## Executable-work procedure

1. Inspect the submitted source, entry point, and relevant changed area.
2. Run the artifact using the Student's command or an equivalent permitted
   command.
3. Check the required ordinary, boundary, and failure cases.
4. Compare observed behavior with the Student's compact description.
5. If understanding or authorship is material, ask one or two focused
   questions or request one small controlled change. Do not require a long
   report as a substitute for running the code.
6. Distinguish code failure, environment failure, and missing evidence.
