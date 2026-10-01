.DEFAULT_GOAL := test-core
.PHONY: test-core check-links check-manifest test-core-selftest

test-core:
	@python3 scripts/check-core.py --root .
	@python3 scripts/doc-links.py check
	@python3 scripts/check-manifest.py

check-links:
	@python3 scripts/doc-links.py check

check-manifest:
	@python3 scripts/check-manifest.py

test-core-selftest:
	@python3 scripts/check-core-selftest.py
