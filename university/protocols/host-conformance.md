# Host Conformance

Checklist a host satisfies before serving Students. The University core states
these duties; it does not implement them. The CLI workspace meets them through
the `students/` repository, the runtime adapters, and `make init`. A host that
cannot meet an item must not serve Students, or must declare the limitation and
follow the fallback named in the item.

## Core access

- [ ] Reads the core through `MANIFEST.md` and pins it by Git tag or commit.
- [ ] Uses `MANIFEST.md` as a bounded discovery index and does not recursively
      scan unrelated repository, VCS, hidden runtime, or Student files.
- [ ] Treats the core as read-only input by default; the only `.4` mutation
      exception is an authorized, bounded correction to learning MATERIALS
      through the correction-governance contract. Policies, Skills, workflows,
      framework, configuration, and service files remain read-only.
- [ ] Builds calls per `protocols/host-prompt-assembly.md`.
- [ ] Implements the startup states `missing`, `unavailable`,
      `available/no-active-workflow`, and `available/active-workflow`.
- [ ] Loads `MANIFEST.md` and Profession context only after an `available`
      Student inspection result.

## Student state

- [ ] Stores state through `protocols/student-state-contract.md`; the stored
      shape validates against `schemas/student-state.schema.json`.
- [ ] Authenticates the Student and isolates state: one Student's session can
      never read or write another Student's state. This is a host duty.
- [ ] Resolves the authenticated Student ID through the registry and exposes
      only selector-based reads from `inspect-student-state`.
- [ ] Creates Student homework/artifact directories only when the selected
      workflow needs them and the required directory is absent.
- [ ] Applies the write authority of `policies/student-state-authority.md`
      (by acting Profession and workflow) and reads every write back.
- [ ] Keeps Evidence append-only and never promotes private state into public
      content.
- [ ] Keeps dialogue language and other session data out of the core.

## Skills and Workers

- [ ] Exposes only `learning` Skills in Student sessions; `administrative` and
      `development` Skills are not reachable.
- [ ] Exposes `technical` Skills only through an explicitly authorized Worker
      workflow with bounded inputs and target checks; class membership alone
      never grants authority.
- [ ] Keeps CLI Student teaching and authorized Worker operations distinct from
      a restricted Student web profile.
- [ ] Validates all declared workflow/Skill dependencies and rejects
      administrative or development reachability from a learning chain.
- [ ] Resolves Workers from the manifest; no prompt, agent, or tool is named
      after a Worker.
- [ ] Inspects the authenticated Student state before startup routing and
      resumes any active enrollment, plan, current Lesson, or explicit
      academic handoff.
- [ ] Runs the manifest `startup_skill` (`rector-startup`) under the
      `startup_workflow` only after that inspection confirms that no active
      workflow exists.
- [ ] Validates Student-facing interaction objects against
      `schemas/interaction-response.schema.json`.

## Declared capabilities

The host declares each and Workers do not assume an undeclared one
(`policies/runtime-portability.md`):

- [ ] code execution (none: `policies/practical-work.md` fallback);
- [ ] artifact storage and retrieval (none: no work needing inspection);
- [ ] private state store (required);
- [ ] public content persistence (none: material is delivered in-session and
      reported for maintainer promotion).

## Host evolution boundary

- [ ] The Student bot's purpose is learning from ready plans and materials; it
      does not create canonical material or development plans.
- [ ] A future Worker host has a separate permission profile and may expose
      approved correction operations only after issue/Git/check capabilities,
      authorization, and required validations exist.
- [ ] An initial host may expose read-only University tools. MCP transport
      exposes bounded tools only; it does not grant authority, replace host
      orchestration, provide state, or bypass the active Profession/workflow.
- [ ] Mandatory policies, active workflow, current Lesson, and source/version
      context are loaded explicitly. Retrieval, when added later, supplements
      that context and does not replace it.

## Safety

- [ ] Code execution, if offered, runs in an isolated sandbox with limits.
- [ ] Usage limits and logging exist; logs never expose one Student's state to
      another.
- [ ] A pinned core copy is checked by exact Git tag or commit before serving;
      mutable branches and parent-workspace aliases are rejected.
