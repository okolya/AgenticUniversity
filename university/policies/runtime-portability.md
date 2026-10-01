# Runtime portability

The academic model is provider-neutral. Claude, Codex, Cursor, and future runtimes are adapters. Runtime-specific files must not become the canonical source of professions, policies, workflows, skills, faculties, courses, or Student state.


## Hosts and capabilities

A **host** is whatever runs the University: the CLI workspace (Claude Code,
Codex, Cursor with the `students/` repository) or another system such as an
online chat bot. The core is identical for every host; hosts differ in
capabilities and supply their own start-up.

- The CLI host implementation is described by `policies/context-loading.md`,
  `policies/runtime-command-whitelist.md`, and
  `protocols/workspace-composition.md`. Those files bind CLI hosts only.
- Any host reads the core through `MANIFEST.md`, keeps Student state through
  `protocols/student-state-contract.md`, and exposes only `learning` Skills in
  Student sessions.
- A host declares which capabilities it has: code execution, file or artifact
  storage, private state store, public content persistence (writing new
  Lessons, diagnostics, and Theme records into `university/`). A Worker must not
  assume a capability the host has not declared.
- Without public content persistence, Workers deliver prepared material in the
  session and report it for promotion by a maintainer; they never claim it was
  persisted to the public University.
- Code execution is optional. When it is unavailable, `policies/practical-work.md`
  governs the fallback.
- The CLI host declares: code execution yes, artifact storage yes (the
  Student's working files and the `students/` repository), private state store
  yes (`students/`), public content persistence yes (`university/` Git).
- Nothing here weakens or replaces the CLI path; adding a host never changes
  how CLI hosts behave.
