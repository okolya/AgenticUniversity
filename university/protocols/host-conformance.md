# Host Conformance

Checklist a host satisfies before serving Students. The University core states
these duties; it does not implement them. The CLI workspace meets them through
the `students/` repository, the runtime adapters, and `make init`. A host that
cannot meet an item must not serve Students, or must declare the limitation and
follow the fallback named in the item.

## Core access

- [ ] Reads the core through `MANIFEST.md` and pins it by Git tag or commit.
- [ ] Treats the core as read-only input; never embeds a copy of it.
- [ ] Builds calls per `protocols/host-prompt-assembly.md`.

## Student state

- [ ] Stores state through `protocols/student-state-contract.md`; the stored
      shape validates against `schemas/student-state.schema.json`.
- [ ] Authenticates the Student and isolates state: one Student's session can
      never read or write another Student's state. This is a host duty.
- [ ] Applies the write authority of `policies/student-state-authority.md`
      (by acting Profession and workflow) and reads every write back.
- [ ] Keeps Evidence append-only and never promotes private state into public
      content.
- [ ] Keeps dialogue language and other session data out of the core.

## Skills and Workers

- [ ] Exposes only `learning` Skills in Student sessions; `administrative` and
      `maintenance` Skills are not reachable.
- [ ] Resolves Workers from the manifest; no prompt, agent, or tool is named
      after a Worker.
- [ ] Runs the manifest `startup_skill` (`rector-startup`) under the
      `startup_workflow` for a session without an assigned workflow.

## Declared capabilities

The host declares each and Workers do not assume an undeclared one
(`policies/runtime-portability.md`):

- [ ] code execution (none: `policies/practical-work.md` fallback);
- [ ] artifact storage and retrieval (none: no work needing inspection);
- [ ] private state store (required);
- [ ] public content persistence (none: material is delivered in-session and
      reported for maintainer promotion).

## Safety

- [ ] Code execution, if offered, runs in an isolated sandbox with limits.
- [ ] Usage limits and logging exist; logs never expose one Student's state to
      another.
