# Codex adapter

Read and obey `AGENTS.md`. Treat `university/` as canonical.

Use project custom agents from `.codex/agents/university-*.toml` when delegating a University Profession. Explicitly request/delegate subagent work when the workflow changes academic responsibility. Pass the target Worker and activation context because delegated agents have their own thread/context.

Use discovered `university-*` Agent Skills as tools/capabilities of the active Worker. Skills do not own academic decisions. The standard `make init` flow also installs the project-scoped Codex overlay from `agent-runtime/adapters/codex/config.toml`.

For every session, follow `university/policies/dialogue-language.md` to select the dialogue language. For a new session, follow `university/policies/runtime-command-whitelist.md` after routing into the `university/` repository. Use the bounded bootstrap context once, then run `university-rector-startup`; do not probe both the workspace aliases and repository paths separately.
