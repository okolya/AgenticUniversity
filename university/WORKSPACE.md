# Agentic University

This is the public Agentic University core repository. It is independently
usable as the source of public academic knowledge and runtime adapters.

- `university/` — public University: behavior, agents, reusable knowledge, courses and learning materials.
- A host may provide `students/` as a separate private repository for Student
  state; it is not a core dependency.
- A composed workspace may expose root AI files as runtime-managed links to
  this core.

Standalone core checks:

```bash
make test-core
make setup-hooks
```

Workspace orchestration, host runtime installation, and private Student state
belong to the host repositories that compose this core.
