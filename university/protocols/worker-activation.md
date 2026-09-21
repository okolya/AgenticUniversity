# Worker Activation Protocol

A Worker is a concrete appointment of a Profession. Workers do not get their own runtime agent definitions.

Before activation, follow `university/protocols/profession-routing.md` to
select the Profession and resolve the active Worker whose appointment matches
the task scope. The routing layer attaches the resolved Worker path to the
Profession context; the runtime must still validate Profession, status,
Faculty, and scope.

For assessment work, the handoff must also include the applicable contract from
`university/protocols/assessment-contracts.md`. An assessment call without the
required Dean request, review context, or evidence-handoff fields is
incomplete.

## Required activation input

The caller must identify:

1. Profession.
2. Current workflow and task.
3. Faculty/scope when applicable.
4. Applicable policies and success criteria.
5. Only the Student context permitted for this task.

The routing layer resolves the matching active Worker from
`university/staff/REGISTRY.md` or the relevant Faculty `STAFF.md`, then attaches
that Worker record and file to the activated Profession context. Callers do not
select or invoke a Worker by name. If no matching appointment exists, stop and
report that an appointment is required. Do not silently create one.

## Activation sequence

1. Load `university/professions/<profession>/PROFESSION.md`.
2. Load `university/professions/<profession>/SKILLS.md`.
3. Load the concrete `WORKER.md`.
4. Verify that the resolved Worker profession matches the invoked Profession
   agent.
5. Load Faculty/scope referenced by the Worker if it exists and is needed.
6. Resolve effective skills as:
   `Profession baseline skills + Worker additional skills`.
7. Load only the applicable policies/workflow/success criteria.
8. Load only permitted Student context.
9. Act under Profession authority with the resolved Worker appointment as
   attached context. The Worker name is identity metadata, not a runtime call
   target.

After a delegated operation, the caller follows
`university/protocols/artifact-verification.md`. A Worker or Skill report is
not proof that an artifact, state change, or validation result has the
reported contents; verify the smallest relevant canonical surface before
presenting or using the result.

## Delegation contract

When handing work to another Profession, the parent must pass at minimum:

- target Profession;
- task/purpose;
- workflow stage;
- relevant scope/faculty;
- applicable success criteria/policies;
- permitted Student context or a precise instruction where to read it.

The receiving runtime resolves and attaches the matching Worker after these
fields are supplied. A delegation must not address a named Worker directly.

Do not assume a subagent sees parent conversation history.

## Skill rule

A Skill is not a Worker or subagent. Invoke/use Skills inside the active Worker context. A Skill returns an operation result; the Worker retains academic authority.
