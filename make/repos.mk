.PHONY: workspace-init status check-repos fetch-all pull-all commit-all push-ready
workspace-init:
	@$(MAKE) init

check-repos status:
	@bash ./scripts/check-repos-status.sh

fetch-all:
	@bash ./scripts/fetch-all-repos.sh

pull-all:
	@bash ./scripts/pull-all-repos.sh

commit-all:
	@bash ./scripts/commit-all.sh

push-ready:
	@bash ./scripts/push-ready.sh

.PHONY: check-students-origin workspace-check
check-students-origin:
	@bash ./scripts/check-students-origin.sh

workspace-check: check-students-origin runtime-check
	@echo "✅ workspace repositories and runtime are ready"
