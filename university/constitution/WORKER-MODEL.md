# Worker model

A Worker is not a separate runtime agent type.

A Worker is an appointment/context applied to a Profession agent:

`Profession Agent + Worker Appointment + Faculty/Scope + Profession Skills + Worker Skills + Policies + Workflow Context = Acting Worker`

The runtime invokes the profession agent (`rector`, `dean`, etc.). Before acting as a named Worker, that agent loads the Worker's `WORKER.md` and appointment context.

## Skills inheritance

- Profession skills are the baseline capabilities available to every Worker of that Profession.
- Worker skills are additive specialization capabilities.
- Worker skills do not replace profession skills unless an explicit policy says otherwise.
- A Worker must not silently acquire skills outside the Profession or appointment rules.

This keeps runtime agents few and reusable while Workers remain real named University staff.
