# Agentic University

This is the public Agentic University core repository. It is independently
usable as the source of public academic knowledge and runtime adapters.

- `university/` — public University: behavior, agents, reusable knowledge, courses and learning materials.
- `students/` is the ignored private Student repository for this core. It may
  be absent in a public-only clone and is created or attached by the host when
  a Student workspace is needed.
- A composed workspace may expose root AI files as runtime-managed links to
  this core.

Standalone core checks:

```bash
make test-core
make setup-hooks
```

Workspace orchestration and host runtime installation belong to repositories
that compose this core. Workers always resolve permitted private Student state
from the core-relative `students/` repository.
