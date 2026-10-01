# Host Prompt Assembly Protocol

How a host builds the context for one Profession call. It restates
`worker-activation.md` and `profession-routing.md` for hosts that do not use the
CLI adapters; it adds no authority and changes no academic rule. CLI hosts
follow the adapters, which implement the same sequence.

All paths are core-relative and discovered through `MANIFEST.md`.

The always-on policies (layer 1) are loaded up front, earlier than the
"applicable policies" step of `worker-activation.md`; this is intentional and
stricter, not a different rule.

## Session start

1. Read `MANIFEST.md`. Use `startup_profession`, `startup_skill`, and
   `startup_workflow` when no academic workflow is assigned.
2. Establish the session's dialogue language per `policies/dialogue-language.md`;
   it is per-session host state, never stored in the core.
3. Identify the Student (host authentication) and open only that Student's
   state through the contract (`protocols/student-state-contract.md`).

## One Profession call

Assemble layers in this order. Load only what the task needs; never scan the
tree.

| # | Layer | Source |
|---|---|---|
| 1 | Always-on policies | `policies/no-invention.md`, `policies/interaction-format.md`, `policies/dialogue-language.md`, `policies/academic-authority.md`, `policies/student-state-authority.md` |
| 2 | Profession | `professions/<profession>/PROFESSION.md`, `SKILLS.md` |
| 3 | Worker | the record named by the matching `workers` entry of the manifest; validate that its Profession, scope, and status match the task; include its additional policies, if any |
| 4 | Workflow | `workflows/<workflow>.md` plus the protocols and policies it names |
| 5 | Scope | only the Faculty, Course, Module, Theme, or Lesson files the task addresses |
| 6 | Skills | effective Skills = Profession baseline + Worker additions. In a Student session expose `learning` only; in an authorized Worker workflow expose only declared `technical` capabilities with bounded inputs and targets. Load each exposed Skill's `SKILL.md` when used |
| 7 | Student context | only what the workflow permits, obtained with contract operation `read` for a stated purpose |
| 8 | Task | the delegation fields below |

If no active Worker matches, stop at the staffing boundary and report it; never
invent a Worker or address one by name.

## Delegation

A call to another Profession is a new, isolated call: it does not see the
parent conversation. The parent passes at minimum: target Profession, task or
purpose, workflow stage, scope/faculty, applicable success criteria and
policies, and the permitted Student context or a precise instruction where to
read it. Assessment calls also carry the contracts from
`protocols/assessment-contracts.md`. The call targets a Profession; the host
resolves the Worker.

## Skills as tools

A Skill is a bounded capability of the active Worker, not a Worker or a
subagent. Skills that touch Student state perform contract operations and keep
the authority limits of `policies/student-state-authority.md`. A Skill result
returns to the active Worker, who keeps academic authority.

## After an operation

Verify material claims per `protocols/artifact-verification.md`: after a state
write, `read` the affected state back before relying on it.

## Not allowed

- a runtime agent, prompt, or tool named after a Worker;
- loading another Student's state, or more Student context than permitted;
- exposing `administrative`, `development`, or `technical` Skills directly in a Student session;
- allowing a learning dependency chain to reach `administrative` or `development`,
  or an undeclared/unbounded technical capability;
- storing Student-specific or session-specific data in the core.
