---
name: register-worker
description: Internal staffing-index operation used after an authorized appointment/change to synchronize Worker discovery indexes. It grants no appointment authority.
---
# Register worker

Synchronize staff discovery indexes from an already-authorized `WORKER.md`.

## Source of truth

The Worker's `WORKER.md` is the canonical appointment record. Registries are discovery indexes, not independent authority sources.

## Indexes

- University index: `university/staff/REGISTRY.md`
- Faculty index: `university/faculties/<faculty>/STAFF.md` when faculty-scoped

## Rules

1. Read the existing Worker record; never invent missing appointment data.
2. Add/update the University index.
3. If faculty-scoped, add/update the Faculty index.
4. Remove stale index entries when a Worker changes Faculty/scope/status.
5. Deactivation updates indexes but preserves the Worker record/history.
6. Never create runtime agents.
7. Normally invoked by `appoint-worker`; direct use is limited to registry repair/synchronization and cannot create authority.
