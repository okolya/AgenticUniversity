# Profession Routing Protocol

Runtime calls target a Profession. A concrete Worker is resolved and activated
after the Profession has been selected; a Worker never becomes a separate
runtime agent.

## Resolution sequence

1. Identify the requested responsibility, academic object, and current
   workflow stage.
2. Select the owning or explicitly contributing Profession from the authority
   matrix and active workflow.
3. Determine the narrowest applicable scope: University, Faculty, Course,
   Module, Theme, Lesson, practice, measurement, examination, or material
   review.
4. Resolve an active Worker with the selected Profession and matching scope
   from `university/staff/REGISTRY.md` and the relevant Faculty `STAFF.md`.
5. Validate that the Worker's appointment, scope, and status match the task.
   Do not invent a Worker, silently use a different Faculty's Worker, or fall
   back to a named person from conversation text.
6. Invoke the runtime adapter for the Profession, then activate the resolved
   Worker through `worker-activation.md`.
7. Pass the workflow, scope, success criteria, applicable policies, and only
   permitted Student context. The Worker retains the Profession's authority.

If no matching active Worker exists, stop at the staffing boundary and report
that appointment or explicit assignment is required. Do not invoke a similarly
named Profession or create a worker-specific runtime agent.

## Scope-to-Profession map

| Responsibility / object | Runtime Profession | Worker resolution |
|---|---|---|
| University structure, startup, University-wide governance | Rector | active University Rector |
| Faculty definition, Course architecture, Module contract, placement, trajectory | Dean | active Dean of the target Faculty |
| Theme design and new-material Lesson | Lecturer | Lecturer assigned to the Theme/Course inside the target Faculty |
| Reinforcement or remediation | Teacher | Teacher assigned to the relevant learning frame |
| Practical lab | Laboratory Specialist | Laboratory Specialist assigned to the relevant Faculty/learning frame |
| Independent entry, gap, retention, or Theme measurement | Learning Analyst | independent Analyst assigned to the assessment scope |
| Internal Module examination and verdict | Examiner | independent Examiner assigned to the Module scope |
| Pedagogical integrity/readability review of prepared material | Instructional Assistant | active University-wide Instructional Assistant appointment |

## Academic hierarchy routing

- A Course or Module request first resolves the Course's Faculty, then its
  active Dean. It does not route directly to a Lecturer for Course/Module
  architecture decisions.
- A Theme or Lesson request resolves the owning Faculty Dean for the approved
  frame, then the Lecturer assigned to that Theme. The Lecturer owns the
  teaching design inside the Dean-approved frame.
- Teacher, Laboratory Specialist, Learning Analyst, and Examiner calls require
  the relevant assigned scope and independence constraints. Their Profession
  does not grant permission to change parent curriculum or another Worker's
  verdict.
- Material review is intentionally cross-Faculty. It routes to the
  Instructional Assistant Profession and the University-wide appointment; it
  is not routed by the assistant Worker's name.

## Invocation boundary

Adapters and parent Workers must name the target Profession in a delegation
and provide the relevant scope so the routing layer can attach the resolved
Worker path to the activation context. They must not create provider agents
named after Workers such as `luke`, `adam`, or `livia`.
Registry names are appointment data, not callable runtime identities.
