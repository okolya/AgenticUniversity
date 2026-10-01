# Cursor adapter

Read and obey `AGENTS.md`. Treat `university/` as canonical.

Use `.cursor/agents/university-*.md` as Profession subagents. Cursor subagents have isolated context, so every delegation must name the target Profession and include the Worker resolved by `university/protocols/profession-routing.md` and the activation context required by `university/protocols/worker-activation.md`.

Use `university-*` Skills for reusable operations; do not substitute a subagent for a Skill. Project rules under `.cursor/rules/` enforce the canonical University boundary.
