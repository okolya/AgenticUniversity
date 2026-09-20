.PHONY: agent-init agents-init runtime-check

agent-init:
	@bash ./scripts/agents-init.sh
	@bash ./scripts/runtime-check.sh

agents-init: agent-init

runtime-check:
	@bash ./scripts/runtime-check.sh
