# Agentic University

Public, provider-neutral source of the Agentic University.

## Ownership

- `university/` — professions, workers, faculties, courses, skills, policies, workflows, protocols, templates, and all reusable/public accumulated knowledge.
- `agent-runtime/` — runtime adapters for Claude, Codex, and Cursor.
- private Student data lives only in the sibling `students/` repository created/preserved by workspace initialization.

## Start

```bash
make init
```

Run it from this `university/` repository. It composes the parent workspace, creates the private `students/` repository when absent, exposes University-owned AI/runtime files in the workspace root via symlinks, validates the runtime, and installs University Git hooks.

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

These commands operate only on the sibling `university/` and `students/` Git repositories. `commit-all` commits but never pushes; pushing is explicit via `push-ready`.

## Boundary

University owns behavior and reusable knowledge. Students owns only private educational state. The parent workspace only composes them at runtime.
