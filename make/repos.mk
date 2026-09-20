.PHONY: status fetch-all pull-all commit-all push-ready check-students-origin workspace-check
status:
	@bash ./scripts/check-repos-status.sh
fetch-all:
	@bash ./scripts/fetch-all-repos.sh
pull-all:
	@bash ./scripts/pull-all-repos.sh
commit-all:
	@bash ./scripts/commit-all.sh
push-ready:
	@bash ./scripts/push-ready.sh
check-students-origin:
	@bash ./scripts/check-students-origin.sh
workspace-check: check-students-origin runtime-check
	@echo "✅ workspace repositories and runtime are ready"
