# 0001. University core is the source of truth; hosts are separate

Status: Accepted
Date: 2026-09-30 (recorded retroactively for plan v0.0.1)

## Context

The University runs today as a CLI workspace (Claude Code, Codex, Cursor). The
goal is to also run it online as a chat bot. `AGENTS.md` already declares the
academic model provider-neutral, and `policies/runtime-portability.md` treats
runtimes as adapters.

## Options considered

- **Rewrite the University inside the bot** — fast to start, but forks the
  academic logic; two sources of truth drift apart.
- **Keep the bot in this repository** — one place, but mixes hosting
  infrastructure with the logical core and makes the core depend on one host.
- **Separate bot repository that reads the core** — the core stays the single
  source of truth; hosts supply runtime, storage, channels, and security.

## Decision

`university/` stays the logical core and the only source of truth. Every host,
including the CLI workspace and any bot, is a separate consumer that reads the
core and never copies it. The CLI path stays fully supported.

## Consequences

- Bot-readiness changes are additive and must never weaken CLI behavior.
- Hosts pin the core by Git tag or commit and read it through `MANIFEST.md`.
- Hosting infrastructure, authentication, and databases live outside the core.
- See `policies/runtime-portability.md`. Private implementation records belong
  to the composing workspace and are not core dependencies.
- Revisit if a host needs core behavior that cannot be expressed declaratively.
