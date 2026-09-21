---
name: appoint-worker
description: Create any University Worker from a Profession template for a concrete specialization, faculty/scope, and appointment, then register the appointment.
---
# Appoint worker

Create a concrete Worker without creating a new runtime agent. The Worker always uses the runtime agent of the selected Profession.

## Inputs

- appointing Worker;
- target Profession;
- worker name/identity;
- appointment title;
- faculty/scope;
- specialization, if any;
- additional responsibilities, skills, or policies beyond the Profession baseline;
- status.

## Procedure

1. Verify the target Profession exists.
2. Verify the appointing Worker has authority under `policies/worker-appointment.md`.
3. Load the Profession definition and baseline skills.
4. Load the target Faculty/scope specification when applicable.
5. Create `university/workers/<worker>/WORKER.md` from `templates/worker/WORKER.template.md`.
6. Keep the Worker thin: do not copy Profession responsibilities, baseline
   Skills, or baseline policies into it.
7. Record only identity, appointment, status, scope, a genuine narrower
   specialization, and explicit additive or scope-narrowing additions.
8. If any addition beyond identity/appointment/status/scope is non-empty,
   mark it as an exception, justify it in `WORKER.md`, and report it to the
   University owner before commit.
9. Invoke `register-worker` to update staff discovery indexes.
10. Return the created Worker path and effective composition summary,
    including any reported exception.

## Effective worker

`Profession + Faculty/scope + Worker appointment + Worker additions = acting Worker`

This Skill creates an appointment, not a new Profession agent.
