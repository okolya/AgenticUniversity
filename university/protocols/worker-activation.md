# Worker Activation Protocol

A Worker is a concrete appointment of a Profession. Workers do not get their own runtime agent definitions.

## Required activation input

The caller must identify:

1. Profession.
2. Worker file: `university/workers/<worker>/WORKER.md`.
3. Current workflow and task.
4. Faculty/scope when applicable.
5. Applicable policies and success criteria.
6. Only the Student context permitted for this task.

Resolve named Workers through `university/staff/REGISTRY.md` or the relevant Faculty `STAFF.md` when possible. If the requested Worker does not exist, stop and report that an appointment is required. Do not silently create one.

## Activation sequence

1. Load `university/professions/<profession>/PROFESSION.md`.
2. Load `university/professions/<profession>/SKILLS.md`.
3. Load the concrete `WORKER.md`.
4. Verify that Worker profession matches the invoked Profession agent.
5. Load Faculty/scope referenced by the Worker if it exists and is needed.
6. Resolve effective skills as:
   `Profession baseline skills + Worker additional skills`.
7. Load only the applicable policies/workflow/success criteria.
8. Load only permitted Student context.
9. Act as the named Worker under Profession authority.

## Delegation contract

When handing work to another Profession, the parent must pass at minimum:

- target Profession;
- target Worker path/name;
- task/purpose;
- workflow stage;
- relevant scope/faculty;
- applicable success criteria/policies;
- permitted Student context or a precise instruction where to read it.

Do not assume a subagent sees parent conversation history.

## Skill rule

A Skill is not a Worker or subagent. Invoke/use Skills inside the active Worker context. A Skill returns an operation result; the Worker retains academic authority.
