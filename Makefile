.DEFAULT_GOAL := test-core
.PHONY: test-core check-links check-manifest test-core-selftest setup-hooks

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
