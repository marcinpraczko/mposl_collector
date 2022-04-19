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

# https://github.com/marcinpraczko/collector/blob/master/quick-start/Makefile-verinfo.txt
# TODO: This is hardcoded so far - would be nice to add URL Prefifx as variable - will be easier to testing
# TODO: Add above task to GH as an issue
THIS_MAKEFILE = https://raw.githubusercontent.com/marcinpraczko/collector/5-add-simple-makefile-for-downloading-modules-from-repo/quick-start/Makefile
THIS_MAKEFILE_VER_URL = https://raw.githubusercontent.com/marcinpraczko/collector/5-add-simple-makefile-for-downloading-modules-from-repo/quick-start/Makefile-verinfo.txt
THIS_MAKEFILE_VER_FILENAME = Makefile-verinfo.txt
THIS_MAKEFILE_VER = 0.1.1

.PHONY: help
help: ## HELP: Show this help message.
	@echo 'usage: make [target] ...'
	@echo
	@echo 'Version: $(THIS_MAKEFILE_VER)' 
	@echo
	@echo 'Targets:'
	@echo '========'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'


.PHONY: init-local-check-update
init-local-check-update: ## INIT-LOCAL: Check for available update for this Makefile
	@echo "Checking for available update for this 'Makefile'"
	@echo "URL: $(THIS_MAKEFILE_VER_URL)"
	@echo -n "Current version   : "
	@cat $(THIS_MAKEFILE_VER_FILENAME)
	@echo -n "Available version : "
	@curl $(THIS_MAKEFILE_VER_URL)


.PHONY: init-local-update
init-local-update: ## INIT-LOCAL: Download newer version of this Makefile
	@echo "Downloading newer version for this 'Makefile'"
	@wget -O Makefile $(THIS_MAKEFILE)


.PHONY: init-local-setup
init-local-setup: ## INIT-LOCAL: Create initial structure on local folder
	@echo "Init local: Create initial structure on local folder"


.PHONY: init-dump-version
init-dump-version: ## INIT: Dump version for this Makefile
	@echo "Dumping version for this 'Makefile' to file: $(THIS_MAKEFILE_VER_FILENAME)"
	@echo "$(THIS_MAKEFILE_VER)" > $(THIS_MAKEFILE_VER_FILENAME)
	@cat $(THIS_MAKEFILE_VER_FILENAME)
