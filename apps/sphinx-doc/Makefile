# ============================================================================
# Based on page: https://gist.github.com/prwhite/8168133
#
# Example of self-documented makefile
#
# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# 
# Downloaded from:
#   https://raw.githubusercontent.com/marcinpraczko/collector/master/snippets/000-hardcoded/001-Makefile-self-describe-usage.txt
# ============================================================================

.PHONY: help
help: ## Help:: Show this help message
	@echo 'usage: make [target] ...'
	@echo
	@echo 'Targets:'
	@echo '========'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

# Define the version variable
MPC_SPHINX_DOC_UTILS_VERSION = "0.1.1"
MPC_SPHINX_DOC_DOCS_VERSION  = "0.1.1"

MPC_SPHINX_DOC_UTILS_TAG = "mpc-sphinx-doc-utils:$(MPC_SPHINX_DOC_UTILS_VERSION)"
MPC_SPHINX_DOC_DOCS_TAG  = "mpc-sphinx-doc-docs:$(MPC_SPHINX_DOC_DOCS_VERSION)"

.PHONY: build-and-deploy-images
build-and-deploy-images: ## Build: NOT WORKING: Build ALL images and upload them to minikube
build-and-deploy-images: build-docker-images upload-images-to-minikube apply-kubectl-manifest

.PHONY: build-docker-images
build-docker-images: ## Build: Docker compose: Build ALL docker images
	docker compose build

.PHONY: build-sphinx-doc-docs
build-sphinx-doc-docs: ## Build: Docker compose: Build Sphinx-Docs docker image
build-sphinx-doc-docs: build-sphinx-doc-docs-static
	docker compose build --no-cache sphinx-docs

.PHONY: run-sphinx-doc-docs
run-sphinx-doc-docs: ## Run: Docker compose: Run Sphinx-Docs docker image
	docker compose up sphinx-docs

.PHONY: run-mpc-sphinx-doc-utils-interactive
run-mpc-sphinx-doc-utils-interactive: ## Run: Docker: Run Sphinx-Utils image interactivly (Debug / Troubleshooting)
	docker run \
		-it --entrypoint /bin/bash $(MPC_SPHINX_DOC_UTILS_TAG)

.PHONY: run-mpc-sphinx-doc-docs-interactive
run-mpc-sphinx-doc-docs-interactive: ## Run: Docker: Run Sphinx-Docs image interactivly (Debug / Troubleshooting)
	docker run \
		-it --entrypoint /bin/sh $(MPC_SPHINX_DOC_DOCS_TAG)

.PHONY: upload-images-to-minikube
upload-images-to-minikube: ## Deploy: Minikube: Upload docker images to minikube
	minikube image load $(MPC_SPHINX_DOC_DOCS_TAG)

.PHONY: apply-kubectl-manifest
apply-kubectl-manifest: ## Deploy: K8S: Apply k8s manifest for docker images
	kubectl apply -f k8s/sphinx-doc-docs.yaml

.PHONY: clean-all-images
clean-all-images: ## Clean:: Clean ALL images
	docker compose down

# --- HELPERS ---
.PHONY: build-sphinx-doc-docs-static
build-sphinx-doc-docs-static: ## Build: Static: Build static files (Snippets / results / etc)
	@echo "Building Sphinx-Docs static files"
	@echo "Syncing utils/helpers to docs/source"
	rsync -av --delete utils/helpers docs/source/
