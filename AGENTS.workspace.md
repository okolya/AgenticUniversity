# Agentic University workspace adapter

This workspace composes the public `university-core/` repository with private
development repositories and the private `university-core/students/`
repository. The public academic source lives in `university-core/university/`;
workspace orchestration lives at the root; planning and development records
live in `documentation/`.

Before acting, verify the relevant Git boundary with
`git rev-parse --show-toplevel`. Never make the root repository track nested
repository contents. Keep Student state private and inspect only the selected
Student context.

The public core is independently usable from inside `university-core/`,
including work with its ignored `students/` repository. The root workspace
assembles core, documentation, and optional component runtime resources through
`make agents-init`.

Academic ontology, authority, and runtime behavior are canonical in
`university/constitution/ONTOLOGY.md`,
`university/constitution/RESPONSIBILITY-MATRIX.md`, and the public core
protocols. Do not change academic authority while restructuring repositories.
