.DEFAULT_GOAL := test-core
.PHONY: help agents-init test-core check-links check-manifest test-core-selftest setup-hooks

help:
	@echo "Agentic University public core commands"
	@echo "  make help               - show standalone core commands"
	@echo "  make test-core          - run integrity, link, and manifest checks"
	@echo "  make check-links        - validate Markdown links"
	@echo "  make check-manifest     - validate university/MANIFEST.md"
	@echo "  make test-core-selftest - prove every integrity check detects defects"
	@echo "  make setup-hooks        - install core-local Git hooks"
	@echo "  make agents-init        - install core resources into provider homes"

agents-init:
	@bash scripts/agents-init.sh

test-core:
	@python3 scripts/check-core.py --root .
	@npm run links-check-frail --silent
	@python3 scripts/check-manifest.py

check-links:
	@npm run links-check-frail --silent

check-manifest:
	@python3 scripts/check-manifest.py

test-core-selftest:
	@python3 scripts/check-core-selftest.py

setup-hooks:
	@bash scripts/setup-hooks.sh
