# Agentic University

A public, provider-neutral foundation for a personal agentic university.

## Canonical source

- `university/` — professions, workers, faculties, courses, skills, policies, workflows, protocols and public templates.
- `agent-runtime/` — thin runtime adapters for Claude, Codex and Cursor.
- `AGENTS.md` — canonical runtime entry point.
- `CLAUDE.md`, `CODEX.md`, `CURSOR.md` — provider entry adapters.

The private Student repository is separate and is never stored here.

## Initialize

```bash
make init
```

This creates project-scoped runtime links under `.agents/`, `.claude/`, `.codex/` and `.cursor/` and installs root Git hooks when this directory is a Git repository. Existing unrelated runtime assets are not overwritten.

Validate with:

```bash
make runtime-check
```

Generated runtime directories are ignored by Git and are not part of the distributable source.

## Source rule

Every tracked file must have a current Agentic University responsibility. Legacy application infrastructure, backend templates, multi-repository automation and generated runtime state do not belong in this repository.

## v0.13 — Module Contracts

Modules now have a formal pre-content design layer: Dean-owned Entry and Exit competency contracts. A Module can be navigated, diagnosed, skipped, bridged, and prepared before Themes/Lessons/materials exist. Prior Module completion is evidence, not the universal prerequisite.

## Workspace deployment model

The University is deployed as a sibling of one private Students repository inside a non-repository workspace root. Run `make init` from this `university/` repository to create/validate the private repository and expose University-owned AI/runtime files at the workspace root via symlinks.

Repository management is intentionally retained from the monorepo template and adapted to the two sibling repositories. Use `make status`, `make fetch-all`, `make pull-all`, `make commit-all`, and `make push-ready`.

The Students repository contains only private learning-process state. All reusable/non-private accumulated knowledge belongs to this public University repository.
