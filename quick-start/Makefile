# ============================================================================
# Based on page:
#   https://gist.github.com/prwhite/8168133
# 
# Example of self-documented makefile
#
# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# ============================================================================

# Variables related with folders
LCD = $(shell pwd)

THIS_MAKEFILE_VER_FILENAME = Makefile-verinfo.txt
THIS_MAKEFILE_VER = 0.1.0

.PHONY: help
help: ## HELP: Show this help message.
	@echo 'usage: make [target] ...'
	@echo
	@echo 'Targets:'
	@echo '========'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

.PHONY: init-check-update
init-check-update: ## INIT: Check for available update for this Makefile
	@echo "Checking for available update for this 'Makefile'"

.PHONY: init-local
init-local: ## INIT-LOCAL: Create initial structure on local folder
	@echo "Init local: Create initial structure on local folder"

.PHONY: init-dump-version
init-dump-version: ## INIT: Dump version for this Makefile
	@echo "Dumping version for this 'Makefile' to file: $(THIS_MAKEFILE_VER_FILENAME)"
	@echo "$(THIS_MAKEFILE_VER)" > $(THIS_MAKEFILE_VER_FILENAME)
	@cat $(THIS_MAKEFILE_VER_FILENAME)
