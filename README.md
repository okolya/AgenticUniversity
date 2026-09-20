# Agentic University

Public, provider-neutral source of the Agentic University.

## Ownership

- `university/` — professions, workers, faculties, courses, skills, policies, workflows, protocols, templates, and all reusable/public accumulated knowledge.
- `agent-runtime/` — runtime adapters for Claude, Codex, and Cursor.
- private Student data lives only in the nested `students/` repository created/preserved by workspace initialization.

## Start

```bash
make init
```

Run it from this root repository. It creates or preserves the private `students/` repository, installs University-owned runtime resources, validates the runtime, and installs University Git hooks.

After connecting `students/` to its private `origin`:

```bash
make workspace-check
```

## Repository operations

```bash
make status
make fetch-all
make pull-all
make commit-all
make push-ready
```

These commands operate on the public root repository and the nested private `students/` repository. `commit-all` commits but never pushes; pushing is explicit via `push-ready`.

## Boundary

The root repository owns orchestration and public University content under `university/`. Students owns only private educational state and is ignored by the root repository.
