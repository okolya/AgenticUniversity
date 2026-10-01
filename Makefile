.DEFAULT_GOAL := test-core
.PHONY: agents-init check-links check-manifest check-pinned-core check-staff generate help setup-hooks test-core test-core-selftest

help:
	@echo "Agentic University public core commands"
	@echo "  make agents-init        - install core resources into provider homes"
	@echo "  make check-links        - validate Markdown links"
	@echo "  make check-manifest     - validate university/MANIFEST.md"
	@echo "  make check-pinned-core REVISION=<tag-or-commit> - verify an exact clean core revision"
	@echo "  make check-staff        - validate generated staff indexes"
	@echo "  make generate          - regenerate all generated core indexes"
	@echo "  make setup-hooks        - install core-local Git hooks"
	@echo "  make test-core          - run integrity, link, and generated-index checks"
	@echo "  make test-core-selftest - prove every integrity check detects defects"

agents-init:
	@bash scripts/agents-init.sh

generate:
	@python3 scripts/generate-manifest.py --write
	@python3 scripts/generate-staff.py --write

test-core:
	@python3 scripts/check-core.py --root .
	@npm run links-check-frail --silent
	@$(MAKE) check-manifest
	@$(MAKE) check-staff

check-links:
	@npm run links-check-frail --silent

check-manifest:
	@python3 scripts/generate-manifest.py --check
	@python3 scripts/check-manifest.py

check-staff:
	@python3 scripts/generate-staff.py --check

test-core-selftest:
	@python3 scripts/check-core-selftest.py

check-pinned-core:
	@test -n "$(REVISION)" || (echo "REVISION is required" >&2; exit 2)
	@python3 scripts/check-pinned-core.py --revision "$(REVISION)"

setup-hooks:
	@bash scripts/setup-hooks.sh
