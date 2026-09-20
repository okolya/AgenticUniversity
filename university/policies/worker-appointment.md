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

## Worker additions

Worker-specific responsibilities, skills, and policies are additive/narrowing only. They may not silently weaken Profession duties, University Policies, or appointment boundaries.

## Runtime

Appointment creates/updates Worker records and registry indexes. It never creates a named-worker Claude, Codex, or Cursor agent.
