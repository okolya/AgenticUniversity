# Runtime adapters

Canonical University semantics live under `university/`. This directory contains only thin provider-specific adapters for the supported runtime triad: Claude, Codex and Cursor.

`make init` links these adapters into generated project-scoped runtime directories. Do not place Worker-specific agents here: runtime agents represent Professions; Workers are concrete appointment/context records.
