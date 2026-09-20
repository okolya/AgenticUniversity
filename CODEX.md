# Codex adapter

Read and obey `AGENTS.md`. Treat `university/` as canonical.

Use project custom agents from `.codex/agents/university-*.toml` when delegating a University Profession. Explicitly request/delegate subagent work when the workflow changes academic responsibility. Pass the target Worker and activation context because delegated agents have their own thread/context.

Use discovered `university-*` Agent Skills as tools/capabilities of the active Worker. Skills do not own academic decisions.
