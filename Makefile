.DEFAULT_GOAL := help
MAKEFLAGS += --no-print-directory

include make/agents.mk
include make/repos.mk

.PHONY: help init init-with-hooks git-hooks check-hooks clean-runtime

help:
	@echo "Agentic University workspace commands"
	@echo "  make init           - compose workspace, initialize runtime adapters/hooks"
	@echo "  make workspace-init - alias for make init"
	@echo "  make agent-init    - initialize project-scoped runtime adapters"
	@echo "  make runtime-check - validate runtime adapters and canonical references"
	@echo "  make workspace-check - validate runtime + private students origin remote"
	@echo "  make git-hooks     - install root Git hooks"
	@echo "  make check-hooks   - check root Git hooks"
	@echo "  make clean-runtime - remove only generated University runtime links/directories"
	@echo "  make status / fetch-all / pull-all / commit-all / push-ready - manage workspace repos"

init:
	@bash ./scripts/workspace-init.sh
	@$(MAKE) agent-init
	@$(MAKE) git-hooks
	@echo "✅ Agentic University workspace initialization complete"

init-with-hooks: init

git-hooks:
	@bash ./scripts/setup-git-hooks.sh

check-hooks:
	@bash ./scripts/check-hooks-installed.sh

clean-runtime:
	@bash ./scripts/clean-agent-runtime.sh
