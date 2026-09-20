.DEFAULT_GOAL := help
MAKEFLAGS += --no-print-directory

include make/agents.mk
include make/repos.mk

.PHONY: help init git-hooks check-hooks clean-runtime

help:
	@echo "Agentic University workspace commands"
	@echo "  make init                  - compose workspace, initialize runtime adapters and hooks"
	@echo "  make runtime-check         - validate Claude/Codex/Cursor runtime"
	@echo "  make workspace-check       - validate runtime + students private origin"
	@echo "  make git-hooks             - install University Git hooks"
	@echo "  make check-hooks           - verify University Git hooks"
	@echo "  make clean-runtime         - remove generated University runtime state"
	@echo "  make status                - show University/Students Git status"
	@echo "  make fetch-all             - fetch origin for both repositories"
	@echo "  make pull-all              - fast-forward pull both clean repositories"
	@echo "  make commit-all            - commit pending changes in both repositories"
	@echo "  make push-ready            - push committed changes that are ahead"

init:
	@bash ./scripts/workspace-init.sh
	@bash ./scripts/agents-init.sh
	@bash ./scripts/runtime-check.sh
	@bash ./scripts/setup-git-hooks.sh
	@echo "✅ Agentic University workspace initialization complete"

git-hooks:
	@bash ./scripts/setup-git-hooks.sh

check-hooks:
	@bash ./scripts/check-hooks-installed.sh

clean-runtime:
	@bash ./scripts/clean-agent-runtime.sh
