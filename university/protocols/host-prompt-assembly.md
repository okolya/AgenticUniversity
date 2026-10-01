# Host Prompt Assembly Protocol

How a host builds the context for one Profession call. It restates
`worker-activation.md` and `profession-routing.md` for hosts that do not use the
CLI adapters; it adds no authority and changes no academic rule. CLI hosts
follow the adapters, which implement the same sequence.

Public University routing paths are core-relative and discovered through
`MANIFEST.md`. In a CLI/composed workspace the host resolves session kind and
identity from the user's first substantive message (ADR 0009) before reading
any public routing index; a host with a real external authentication context
resolves the authenticated Student through that context instead and skips
message inference entirely.

The always-on policies (layer 1) are loaded before the selected Profession
call, earlier than the "applicable policies" step of
`worker-activation.md`; they are not a reason to preload Profession or Worker
context during Student identification.

## Session start

### Step 0 — resolve session kind (CLI/composed workspace only)

A host with a real external authentication context resolves the
authenticated Student directly from that context (skip to Branch 1, step 1)
and never performs message inference. A CLI/composed-workspace host has no
such context and instead reads the user's first substantive message to
determine which of three branches applies (ADR 0009). Resolution is
registry-bound: a name is only treated as that person's session when it
resolves to exactly one entry in the matching public registry below.
Mentioning a third party's name without claiming to be them is not an
identity claim.

```text
message names/claims a Student, or carries no role signal at all
  → Branch 1 (Student)
message names a Worker, Profession, or Faculty ("ти ректор bob",
"активуй Dean", "як Лектор Adam")
  → Branch 2 (University Worker)
message's intent targets the University's own protocols, Skills,
workflows, plans, or ADRs, with no Student/Worker identity claim
("хочу розробляти матеріали", "онови скіл", "створи план v0.0.x")
  → Branch 3 (University Developer)
genuinely ambiguous (conflicting or absent signal)
  → exactly one AskUserQuestion naming the candidate branches; do not
    repeat this question once the branch is resolved
```

Establish the session's dialogue language per `policies/dialogue-language.md`
before producing any Student-, Worker-, or Developer-facing output; it is
per-session host state and is never stored in the core.

### Branch 1 — Student

The host follows these states in order:

```text
missing/unavailable
  → stop and request initialization or access
available/no-active-workflow
  → resolve Manifest startup route and activate Rector
available/active-workflow
  → resume the recorded workflow and resolve its Profession/Worker
```

1. Resolve a stable Student ID: the authenticated Student ID from the host
   authentication context when one exists, otherwise the name/claim found in
   step 0. Do not infer an identity from a remembered name or a filesystem
   search outside the registry lookup in the next step.
2. In a CLI or composed workspace, resolve that name against exactly one matching
   entry in `students/registry/REGISTRY.md`. Then open only the exact
   `students/<id>/STUDENT.md` path recorded there through the contract
   (`protocols/student-state-contract.md`) using `inspect-student-state`.
   Determine whether an active enrollment, plan, current Lesson, or explicit
   academic handoff exists. If the name does not resolve to any registry
   entry and the message's intent is a Student (a new person wanting to
   learn), route to Rector registration (next paragraph) instead of
   reporting `missing`; `missing` is reserved for a registry/state access
   failure, not for "not yet registered".

   **Rector registration** (new, unregistered name only): registering a new
   Student — creating their `students/registry/REGISTRY.md` entry and
   initial `students/<id>/STUDENT.md` — is Rector authority, exercised
   before any Faculty is chosen; it is university-wide and precedes the
   Dean-owned `faculty-entry`/`create-enrollment` decision that follows once
   the Student picks a Faculty. Activate Rector, confirm the name and intent
   with the person, create the registry entry and a minimal initial Student
   state, then continue with `rector-startup` as for any newly available
   Student with no active workflow. Never invent Faculty placement, Module
   plan, or evidence as part of registration itself.
3. Return one explicit inspection result:
   - `missing` — the registry or exact Student state is absent;
   - `unavailable` — the host cannot access the selected state;
   - `available/no-active-workflow`;
   - `available/active-workflow`.
   Missing or unavailable state stops startup; it is never treated as an empty
   state. The registry is the only Student discovery surface: never guess an
   ID, glob `students/**`, or search for an alternative Student store.
4. Only after an `available` result, read `MANIFEST.md` as the bounded routing
   index. For an active workflow, resume it and resolve its Profession and
   Worker; do not use the manifest startup fields or invoke `rector-startup`.
   With no active workflow, use the manifest `startup_profession`,
   `startup_skill`, and `startup_workflow`.
5. Keep startup discovery bounded: resolve only the selected Student, matching
   Worker, active workflow, and addressed scope. Do not recursively enumerate
   repository, VCS, hidden runtime, or unrelated Student files.

### Branch 2 — University Worker

A Worker (academic staff acting in a Profession — Dean, Lecturer, Teacher,
and the rest of `university/staff/REGISTRY.md`) resolves directly against
that registry, bypassing Student-state inspection entirely.

1. Resolve the named Worker, Profession, or Faculty against exactly one
   matching entry in `university/staff/REGISTRY.md`. If the name resolves to
   a Worker whose Profession differs from what the message assumed (as with
   "ти ректор bob", who is Dean of Language Faculty, not Rector), state the
   correction in one sentence and proceed with the resolved Profession rather
   than stopping on a full clarification question.
2. Activate the resolved Profession and Worker through
   `protocols/profession-routing.md` and `protocols/worker-activation.md`;
   these are unchanged by this branch — it only adds the message-derived
   entry path into them.
3. Do not read any Student's state (`students/<id>/STUDENT.md`) in this
   branch unless the task explicitly names that Student and the workflow
   permits it (`policies/student-state-authority.md`).
4. If no matching staff entry exists, stop at the staffing boundary and
   report it; never invent a Worker, Profession, or Faculty.

### Branch 3 — University Developer

A Developer session changes the University itself — protocols, Skills,
workflows, plans, or ADRs — rather than teaching a Student or acting as
academic staff. There is no Developer registry; authorization is implicit
repository write access, the same boundary that already governs any edit to
`university-core/`.

1. Use `university/skills/session-bootstrap/SKILL.md` (manifest class
   `development`) as the entry point. Its procedure is scoped to this branch
   only — repository/task routing for University maintenance — not to
   Student or Worker sessions.
2. Do not read any Student's state in this branch unless the task explicitly
   names that Student and the workflow permits it.
3. Development-class Skills and workflows (see `MANIFEST.md`) are available
   here; `administrative` Skills are not implied by this branch and still
   require Branch 2's Worker activation when the task needs them.

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
