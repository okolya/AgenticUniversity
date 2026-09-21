# Pre-course Bridge — Python Engineering Foundations

## Identity

- **Course:** AI Engineering
- **Target:** Module 1 — Python AI Engineering Entry Contract
- **Layer:** Pre-course bounded bridge
- **Status:** Approved public bridge frame
- **Assigned Profession:** Lecturer, Engineering Faculty scope; the active
  Lecturer Worker is resolved through Profession Routing

## Purpose

Establish a usable Python engineering foundation before Module 1 starts. The
bridge connects general programming and development-environment
capabilities to readable, executable Python components without assuming that a
particular external course is a complete curriculum. The supplied Udemy
Python course is treated as a partial supplementary source only; it does not
define the Theme boundary or replace coverage of the Module contract.

## Relation to the Module Entry Contract

This bridge is intended to prepare evidence for the relevant Entry Contract
targets:

1. **General-purpose programming:** read and modify small Python programs,
   identify inputs, outputs, control flow, data values, and named-function
   purpose.
2. **Problem decomposition:** break a small computational problem into
   explicit steps and state expected behavior for ordinary and invalid inputs.
3. **Development environment:** work with files and directories, run commands,
   inspect output, and read error messages.
4. **Version control:** establish the basic distinction between a working
   change and a saved Git revision, including inspecting what changed.
5. **Separation of concerns:** distinguish application source from packages,
   runtime configuration, and secrets.

The bridge is competency-based: this frame does not require re-teaching
verified capability and does not imply that the Student must consume every
available source.

## Intended bridge outcome

The Student can explain and implement a small, readable Python component from
stated requirements, run it from a development environment, inspect its
behavior and failures, and describe the boundaries between code, structured
data, files/commands, dependencies, configuration, secrets, and a Git
revision.

## Broad Bridge Success Criteria

By the end of this bridge, the Student should be able to:

- trace and modify a small Python program using functions, core control flow,
  and explicit inputs and outputs;
- decompose a bounded problem into named steps and identify expected behavior
  for valid and invalid inputs;
- represent, read, validate, transform, and serialize basic structured data
  while keeping data boundaries and expected types visible;
- execute a component through files, directories, and commands, and use
  diagnostics and error messages to locate the general class of a failure;
- distinguish application source, external packages, runtime configuration,
  and secrets, including why secrets must not be embedded in source;
- describe and inspect the difference between an uncommitted working change
  and a saved Git revision;
- explain the role of a Python component as one maintainable part of a larger
  AI engineering system.

These are broad bridge criteria for Lecturer planning and formative evidence,
not a Course Entry decision, Module verdict, or permanent Theme sequence.

## Boundaries and non-goals

This bridge remains bounded to:

- Python execution and readability;
- decomposition, functions, interfaces, and basic maintainable structure;
- structured data boundaries and basic validation/serialization;
- files, directories, commands, diagnostics, and ordinary error handling;
- separation of configuration, dependencies, and secrets from source code;
- basic Git context needed to inspect and preserve changes.

It does not, by itself, prescribe or complete:

- the Module 1 Exit Contract or full Module delivery;
- advanced Python internals, broad standard-library coverage, or another
  programming-language learning track;
- machine learning, model engineering, APIs, retrieval, agents, deployment,
  cloud, MLOps, or production architecture beyond lightweight context;
- detailed Lessons, exercises, labs, assessment designs, or a complete resource
  catalogue;
- a mandatory product, framework, external service, certification, or Udemy
  course completion target.

Any need to change Module outcomes, start Module delivery, or expand these
boundaries returns to the Dean for approval.

## Optional product context

Teaching or examples may use a small, bounded application context from
SonikaAI or MarkHere when it clarifies transfer to AI engineering. Either
context is optional, and neither is a required deliverable or prerequisite.
The Lecturer must keep the same bridge criteria assessable without access to
either product and must not let product implementation expand the Module
scope.

## Handoff to the assigned Lecturer

The active Lecturer Worker assigned to this bridge owns the detailed bridge
teaching design within this approved frame. The runtime resolves that Worker
through Profession Routing and Worker Activation; callers invoke the Lecturer
Profession rather than a named Worker.
The assigned Lecturer should use the permitted Student evidence and current
pre-course bridge plan to choose what needs introduction, what may be compressed
or skipped, and which near-term Lessons and materials are justified. The Lecturer
may use the supplied Udemy course selectively as supplementary material after
the reported review; its partial fit must remain explicit.

The assigned Lecturer should return any proposed scope or outcome change to the
Engineering Faculty Dean before proceeding. Teacher reinforcement, laboratory
practice, and independent
measurement remain separate downstream responsibilities and should be
requested only against these criteria.

## Available bounded assessment

- `assessment-python-entry-diagnostic.md` — independent Python diagnostic for
  the pre-course evidence handoff; conducted by the Learning Analyst when the
  Dean requests it.
- `assessment-course-entry-git-and-boundaries.md` — bounded diagnostic for the
  remaining Git and source/configuration/secrets Entry Contract criteria.
