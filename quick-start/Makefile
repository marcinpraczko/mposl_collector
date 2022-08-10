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

# TODO: This is hardcoded so far - would be nice to add URL Prefifx as variable - will be easier to testing
# TODO: Add above task to GH as an issue
THIS_MAKEFILE = https://raw.githubusercontent.com/marcinpraczko/collector/master/quick-start/Makefile
THIS_MAKEFILE_VER_URL = https://raw.githubusercontent.com/marcinpraczko/collector/master/quick-start/Makefile-verinfo.txt
THIS_MAKEFILE_VER_FILENAME = Makefile-verinfo.txt
THIS_MAKEFILE_VER = 0.1.3

HELPER_MAIN_SCRIPT = https://raw.githubusercontent.com/marcinpraczko/collector/marcinp/gh-15/quick-start/helper-main.sh
HELPER_MAIN_SCRIPT_FILENAME = helper-main.sh

.PHONY: help
help: ## HELP: Show this help message.
	@echo 'usage: make [target] ...'
	@echo
	@echo 'Version: $(THIS_MAKEFILE_VER)' 
	@echo
	@echo 'Targets:'
	@echo '========'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

.PHONY: init-setup
init-setup: ## INIT: Run all INIT targets in expected order
init-setup: init-dump-version init-check-for-update init-download-helpers-scripts

.PHONY: init-dump-version
init-dump-version: ## INIT: Dump local version for this Makefile
	@echo ""
	@echo "Dumping version for this 'Makefile' to file: $(THIS_MAKEFILE_VER_FILENAME)"
	@echo "$(THIS_MAKEFILE_VER)" > $(THIS_MAKEFILE_VER_FILENAME)
	@cat $(THIS_MAKEFILE_VER_FILENAME)


.PHONY: init-check-for-update
init-check-for-update: ## INIT: Check for available update for this Makefile
	@echo ""
	@echo "Checking for available update for this 'Makefile'"
	@echo "URL: $(THIS_MAKEFILE_VER_URL)"
	@echo -n "Current version   : "
	@cat $(THIS_MAKEFILE_VER_FILENAME)
	@echo -n "Available version : "
	@curl $(THIS_MAKEFILE_VER_URL)


.PHONY: init-download-updated-version
init-download-updated-version: ## INIT: Download newer version of this Makefile
	@echo "Downloading newer version for this 'Makefile'"
	@wget -O Makefile $(THIS_MAKEFILE)
	@echo ""
	@echo "NOTE: Please run command: 'make init-setup'..."


.PHONY: init-setup-local-workspace
init-setup-local-workspace: ## INIT: (Not Implemented YET) Create initial structure on local folder
	@echo "Init local: Create initial structure on local folder"


.PHONY: init-download-helpers-scripts
init-download-helpers-scripts: ## INIT: Download all required helpers scripts
	@echo "Downloading ALL required helpers scipts..."
	wget -O $(HELPER_MAIN_SCRIPT_FILENAME) $(HELPER_MAIN_SCRIPT)
	chmod 755 $(HELPER_MAIN_SCRIPT_FILENAME)

.PHONY: test-run-script
test-run-script: ## WIP-TEST: Run external script
	./$(HELPER_MAIN_SCRIPT_FILENAME)
