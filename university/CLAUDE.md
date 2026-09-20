# Claude Code adapter

Read and obey `AGENTS.md`. Treat `university/` as canonical.

Use project subagents from `.claude/agents/university-*.md` for Profession delegation. A named Worker is activated through the matching Profession agent using `university/protocols/worker-activation.md`; do not create worker-specific subagents.

Use discovered `university-*` Agent Skills as tools/capabilities of the active Worker. Skills do not own academic decisions.
