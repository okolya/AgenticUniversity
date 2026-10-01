# <Profession Name>

## Nature

This file defines the reusable University Profession `<profession-slug>`.
It is not a Worker appointment and contains no named Worker, Faculty,
Course, subject, or Student-specific knowledge.

## Runtime rule

When instantiated or used as a runtime specialist, load this Profession
together with the resolved Worker appointment, applicable policies, workflow,
success criteria, and only the permitted Student context.

## Boundary

The Profession owns the following responsibility:

- <state the responsibility and decision authority>

It does not own:

- <state adjacent responsibilities that must remain with another Profession>

Reusable operations belong in Skills. The Profession must not invent a
concrete Worker, Faculty, curriculum, or Student state.

## Core responsibility

<Describe the primary academic responsibility and its success criteria.>

## Workflow position

<Describe when this Profession is invoked, what it receives, and what it
must return to the owning or contributing Profession.>

## Delegation and authority

<Describe required handoffs, independence constraints, and the conditions
under which work must stop or return to another Profession.>

## Runtime

The runtime invokes this Profession, then resolves and activates a matching
Worker through `profession-routing.md` and `worker-activation.md`.
Worker names are appointment data, not runtime agent identities.
