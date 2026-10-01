# Practical Work Policy

This policy applies to every exercise, lab, diagnostic, assessment task, and
Lesson task that asks a Student to write or modify executable code.

## Minimum practical contract

Every practical task must state only the information needed to act:

- the target file or bounded code area;
- the behavior or capability to implement or change;
- the inputs and expected outputs, including a meaningful failure case;
- the command or minimal method used to run the work;
- the small amount of evidence the Student must return.

The task must not require a long narrative, duplicated program map, repeated
tracebacks, or explanations unrelated to the learning criterion. A requested
explanation is justified only when it provides evidence of the target
understanding.

For a Student who has already demonstrated the same capability, the task must
not repeat the prior diagnostic or Lesson merely with renamed variables,
different values, or a new story. The accepting Worker and Lecturer must use
the smallest new task that exposes the next capability or transfer demand.

## Acceptance of executable work

The Worker who accepts a practical submission must:

1. inspect the submitted code;
2. run it in the stated environment or an equivalent permitted environment;
3. check ordinary, boundary, and required failure cases against the task;
4. compare the Student's short description with the observed code and runtime
   behavior;
5. record whether a failure comes from the code, environment, or insufficient
   evidence.

The evaluator must not accept a claimed result without inspecting and running
the submitted artifact. A pasted output without the corresponding code is not
enough for executable work.

## Evidence of understanding and authorship

Runnable code alone does not establish that the Student understands it. The
evaluator must use the smallest additional check needed, such as:

- one short explanation of the main data flow or function boundaries;
- one focused question about a behavior observed during the run;
- one small controlled change or debugging request performed by the Student.

The evaluator does not need to prove whether code was generated. The relevant
decision is whether the Student can explain and safely modify the submitted
code. If AI use is allowed, the Student reports it according to the applicable
AI-use mode; allowed AI use does not remove the understanding check.

The Student is not required to produce a long handwritten explanation to prove
authorship. The accepting Worker verifies understanding by inspecting and
running the code and, where needed, asking one focused question or requesting
one controlled change. A short explanation may support that check but cannot
prove that code was not AI-generated.

## Minimal evidence returned by the Student

Unless the specific criterion requires more, request only:

- the code path or submitted artifact;
- the run command;
- a compact result summary for required cases;
- one or two short explanations or answers that expose understanding.

The evaluator may retain raw logs privately when needed, but the Student is
not required to rewrite full terminal traces into the response.

## Roles

- Lecturer evaluates understanding for Lesson teaching evidence.
- Laboratory Specialist evaluates practical activity results within a Lab.
- Learning Analyst performs independent measurement when the workflow requires
  verified evidence.
- Examiner evaluates Module-level practical evidence within the examination.
- Instructional Assistant reviews task clarity and evidence burden; it does not
  run submissions, judge code correctness, or issue a verdict.

The accepting Worker owns the run-and-inspect obligation for the submitted
practical artifact. This obligation cannot be delegated to the Student's
description.


## Hosts without code execution

Run-and-inspect acceptance requires the accepting Worker's host to execute the
submitted artifact. The host declares whether it can
(`policies/runtime-portability.md`).

If the host cannot execute code:

1. the Worker does not issue executable tasks that need run-and-inspect
   acceptance as verified evidence;
2. it chooses a non-executing task that still exposes the target criterion
   (code reading, prediction of behavior, debugging by inspection, design
   explanation) or defers the practical task to a host that can execute;
3. it never records evidence as run, observed, or verified when the artifact was
   not executed; inspection-only results are recorded as inspected, not run, and
   cannot alone support a verified-mastery Evidence status for a criterion that
   requires execution.

A Student may run code in their own environment, but a submitted pasted output
without executable inspection by the accepting Worker remains insufficient (see
"Acceptance of executable work"). Hosts without execution therefore defer, not
downgrade, execution-dependent criteria.
