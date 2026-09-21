# Module 1 — Python AI Engineering

## Identity

- **Course:** AI Engineering
- **Faculty:** Engineering Faculty
- **Module position:** 1 of 7
- **Status:** Public competency and Theme framework approved; detailed delivery is Lecturer-owned and prepared just in time
- **Learning-track boundary:** Python is the only programming language developed as a learning track in this Module and Course.

## Purpose and value

Establish Python as a dependable engineering language for AI/ML systems. The Module closes the programming, software-engineering, data-handling, and execution-reproducibility gaps that could block later work in model engineering, retrieval and knowledge systems, agentic systems, production AI, platforms, and MLOps.

The Module is oriented toward production-quality engineering habits and transferable Python system components, without presupposing a particular AI product or teaching path.

## Entry Contract

The learner must be able to demonstrate all of the following at a basic, observable level:

1. Read and modify a small program in at least one general-purpose programming language, identifying inputs, outputs, control flow, data values, and the purpose of named functions.
2. Decompose a small computational problem into steps and state expected behavior for ordinary and invalid inputs.
3. Work with files and directories, run commands, and inspect program output and error messages in a development environment.
4. Use basic version-control concepts: distinguish a working change from a saved revision, inspect a change, and describe what a revision contains.
5. Explain that external packages, runtime configuration, and secrets are separate concerns from application source code.

These are capability requirements, not requirements to have completed a particular prior Course Module.

## Exit Contract

At completion, the learner must independently demonstrate and explain the following in a bounded, unfamiliar Python engineering context:

1. Implement a readable Python component with clear functions and data boundaries, appropriate use of core language constructs, and behavior that matches stated requirements.
2. Organize a Python codebase so that its executable entry point, reusable code, configuration, dependencies, and documentation have explicit, maintainable boundaries.
3. Make the component reproducibly executable by declaring its Python/runtime and package assumptions and by separating configuration and secrets from source code.
4. Handle invalid inputs, expected operational failures, and dependency failures deliberately, with useful diagnostics and without silently producing misleading results.
5. Validate behavior with focused automated checks, use observed failures to diagnose and correct defects, and explain the limits of the validation performed.
6. Read, validate, transform, and serialize structured data in Python while preserving stated types, invariants, and error behavior.
7. Integrate a library or external service through a narrow Python interface with explicit input/output expectations, configuration boundaries, and failure handling.
8. Review the resulting implementation for maintainability, reproducibility, security-sensitive configuration handling, and suitability as a component of a larger production AI system, and justify identified trade-offs.

The criteria are independently observable and examinable; they do not require a prescribed lesson sequence, exercise, lab, resource set, or product.

## Broad competency areas

- Python language fluency for engineering work
- Program decomposition, interfaces, and maintainable code structure
- Runtime environments, dependencies, configuration, and reproducibility
- Structured data handling and validation
- Diagnostics, failure handling, and defensive behavior
- Automated verification and practical debugging
- Python integration boundaries for libraries and external services
- Production-minded quality and security hygiene for AI-system components

## Theme Framework

The Module is bounded by the following ordered Themes. This is the Dean-owned
coverage frame for Lecturer assignments; it is not a pre-written Lesson plan.
Each Theme must remain within its stated boundary and return evidence before the
next Theme is expanded.

### Theme 1 — Python components and maintainable boundaries

- purpose: turn basic Python reading and modification into small, readable
  components with explicit function, data, and entry-point boundaries;
- covers: functions, interfaces, decomposition, control flow, naming,
  modules/files, and readable change;
- evidence: implement and explain a small component with separated input,
  transformation, and output responsibilities;
- does not cover: frameworks, AI libraries, or production deployment;
- Module criteria: Exit 1 and 2.

### Theme 2 — Structured data and validation

- purpose: make data shape, types, invariants, and validation explicit;
- covers: JSON and equivalent structured data, parsing, transformation,
  serialization, required fields, type/range validation, and invalid input;
- evidence: read, validate, transform, and write structured data while
  preserving declared types and useful errors;
- does not cover: databases, model training, or external services;
- Module criteria: Exit 4 and 6.

### Theme 3 — Runtime, project, configuration, and dependency boundaries

- purpose: make a Python component reproducible and safe to configure;
- covers: executable entry points, project layout, runtime assumptions,
  dependency declarations, example/local configuration, secrets boundaries,
  and reproducible commands;
- evidence: run a component from a documented setup with shareable source and
  example configuration while keeping local values out of version control;
- does not cover: cloud deployment, containers as a separate specialization,
  or operational platform design;
- Module criteria: Exit 2 and 3.

### Theme 4 — Failures, focused checks, and debugging

- purpose: replace accidental behavior with deliberate failure handling and
  evidence-based correction;
- covers: expected input/operational/dependency failures, exception boundaries,
  diagnostics, focused automated checks, observed failures, and debugging;
- evidence: reproduce a defect or invalid case, correct it, and explain what
  the checks do and do not establish;
- does not cover: large test frameworks or production observability systems;
- Module criteria: Exit 4 and 5.

### Theme 5 — Narrow library and service interfaces

- purpose: use an external dependency without losing explicit boundaries;
- covers: selecting a small library or service, adapter functions, input/output
  contracts, configuration, dependency failure, and test doubles or safe local
  substitutes where needed;
- evidence: integrate one external interface through a narrow component and
  handle its success and failure paths;
- does not cover: AI model engineering, RAG, agents, or cloud platform design;
- Module criteria: Exit 3, 4, and 7.

### Theme 6 — Production-minded component review and integration

- purpose: consolidate the Module into an unfamiliar but bounded Python
  component and justify engineering trade-offs;
- covers: maintainability review, reproducibility, security-sensitive
  configuration handling, focused validation, documentation boundaries, and
  integration of the preceding skills;
- evidence: deliver and explain a bounded component, its checks, its failure
  limits, and the trade-offs found in review;
- does not cover: a full production AI product or the Exit Contracts of later
  Modules;
- Module criteria: all Exit criteria, with emphasis on Exit 1–5 and 8.

## Theme sequencing and handoff rules

1. The Dean assigns the current Theme and a bounded Lesson sequence to an
   appointed Lecturer through Learning Interaction Contract 1.
2. Adam is the currently appointed Engineering Faculty Lecturer and receives
   the first Theme assignment. No other Lecturer is invented by this frame.
3. The Lecturer proposes a short teaching-intent plan, prepares only the next
   useful Lesson(s), and invokes the Instructional Assistant for pedagogical
   review before delivery.
4. Practical tasks must use the run-and-inspect contract in
   `university/policies/practical-work.md`; the accepting Worker runs the code
   and checks understanding.
5. A Theme checkpoint returns evidence and unresolved gaps to the Dean. The
   Lecturer may not add Themes, Lessons, or change Module outcomes without a
   new Dean decision.

6. No Theme starts with an open-ended Lesson request. Its finite Lesson map,
   Theme result, Success Criteria, final checkpoint, and stop condition must
   be approved first. Detailed Lesson text may still be prepared just in time
   inside that approved map.

## Hard dependencies

- No prior AI Engineering Course Module is a hard dependency.
- The Entry Contract's general programming and development-environment competencies are hard prerequisites for meaningful entry.
- Later Course Modules may impose their own competency-based Entry Contracts; completion of this Module is evidence, not an automatic prerequisite for every later Module.

## Outcome strategy status

- **Professional application:** Recommended after internal examination when a suitable real-world context is identified; the context and bounded scope are decided with the Student in the private Module plan, not prescribed by this public contract.
- **External certification:** None currently adopted for this Module.

## Delivery boundary

This file defines the public Module contract and the approved Theme boundary.
Detailed Lessons, Labs, and assessments are created under the assigned Theme
just in time. Pre-course bridges and diagnostics live outside this directory
and do not count as Module delivery.
