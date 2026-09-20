# Workers

Workers are named appointments of Profession agents, not additional runtime agent definitions.

Current appointments:
- Petro — Rector
- Bob — Dean, Language Faculty
- Luke — Dean, Engineering Faculty

Activation is defined in `university/protocols/worker-activation.md`.

A Worker inherits Profession baseline skills and may add Worker-specific skills. Additional Worker skills extend rather than replace Profession skills unless an explicit policy says otherwise.

## Creation and discovery

Workers are created through `skills/appoint-worker` under `workflows/worker-appointment.md`, then registered by `skills/register-worker`. Rectors discover University staff in `university/staff/REGISTRY.md`; Deans discover Faculty staff in the Faculty `STAFF.md`.
