# Cursor adapter

Read and obey `AGENTS.md`. Treat `university/` as canonical.

Use `.cursor/agents/university-*.md` as Profession subagents. Cursor subagents have isolated context, so every delegation must name the target Profession and include the Worker resolved by `university/protocols/profession-routing.md` and the activation context required by `university/protocols/worker-activation.md`.

Use `university-*` Skills for reusable operations; do not substitute a subagent for a Skill. The canonical Skill source is `university/skills/<name>/SKILL.md`; provider-home copies are runtime installations and are not a substitute for reading the core contract. Project rules under `.cursor/rules/` enforce the canonical University boundary.

The legacy root `.cursorrules` file is not used by this repository and must not
be created, initialized, or searched during startup. Cursor runtime rules are installed as namespaced
`.mdc` files under the provider-home `~/.cursor/rules/` directory.

## Mandatory session route

For every host session, after reading `AGENTS.md`, follow
`university/protocols/host-prompt-assembly.md` as the Cursor startup contract:

1. Follow `university/policies/runtime-command-whitelist.md` for the bounded
   read-only bootstrap surface, then run
   `university/skills/session-bootstrap/SKILL.md`.
2. Resolve the authenticated Student ID through the registry and inspect only
   the permitted state through
   `university/skills/inspect-student-state/SKILL.md`. Do not load the
   Manifest, Profession, Worker, workflow, or startup Skill before an
   `available` inspection result.
3. After Student inspection, read `university/MANIFEST.md` and the always-on
   policies named by the host-prompt protocol.
4. If an active enrollment, plan, current Lesson, or explicit academic
   handoff exists, resume it and resolve its Profession and Worker. Do not run
   `rector-startup`.
5. Only when no active Student workflow exists, use the manifest startup
   Profession, workflow, and Skill, then activate the resolved Rector Worker.
6. Before the active Profession acts, load the applicable workflow, policies,
   scope, Worker record, and effective Skills specified by
   `worker-activation.md`.

The required policy/workflow documents are context inputs, not optional
search suggestions. Use the manifest and the host-prompt protocol as bounded
discovery indexes; do not recursively scan repository, VCS, hidden runtime,
or unrelated Student files.
