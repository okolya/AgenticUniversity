# Worker appointment authority

Appointment is an institutional decision. `appoint-worker` performs the bounded creation/registration operation; it does not grant appointment authority.

## Founding Rector

The first Rector is a bootstrap appointment supplied by the University owner/template initialization. A Rector does not appoint itself.

## Rector

A Rector may:
- appoint, replace, or deactivate Deans;
- appoint University-wide Workers whose scope is not owned by a Faculty;
- establish initial Faculty leadership.

A Rector normally does not appoint ordinary Faculty teaching/assessment staff once that Faculty has an active Dean. The Rector may replace a Dean or resolve a vacancy; this does not transfer the Dean's normal Faculty staffing responsibility to Rector.

## Dean

A Dean may appoint, replace, or deactivate Workers inside that Dean's own Faculty for Professions such as Lecturer, Teacher, Laboratory Specialist, Learning Analyst, and Examiner.

A Dean may not appoint a Rector, appoint another Faculty's Dean, or staff another Faculty.

## Independence

Appointments must satisfy `assessment-independence.md`.

## Worker inheritance

A Worker is a thin appointment record and must maximally inherit from its
Profession. The Profession remains the single source of truth for duties,
authority, baseline Skills, policies, and runtime behavior.

A Worker may contain only:

- identity and appointment status;
- faculty, Course, Module, Theme, or University scope;
- a genuine specialization that is narrower than, and not a repetition of,
  the Profession;
- explicitly additive responsibilities, Skills, or policies required by the
  appointment.

Worker-specific additions are additive or scope-narrowing only. They may not
copy, replace, weaken, or silently reinterpret Profession duties, University
Policies, or appointment boundaries. Every non-empty addition beyond identity,
appointment, status, and scope is an exception: it must be justified during
appointment, recorded in `WORKER.md`, and reported to the University owner
before the change is committed.

## Runtime

Appointment creates/updates Worker records and registry indexes. It never creates a named-worker Claude, Codex, or Cursor agent.
