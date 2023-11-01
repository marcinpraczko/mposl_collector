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
help: ## Help: Show this help message
	@echo 'usage: make [target] ...'
	@echo
	@echo 'Targets:'
	@echo '========'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

.PHONY: build-all-images
build-all-images: ## Build: Build ALL images and upload them to minikube
build-all-images: build-docker-images upload-images-to-minikube apply-kubectl-manifest

.PHONY: build-docker-images
build-docker-images: ## Build: Build ALL docker images
	/usr/local/bin/docker-compose build
	/usr/local/bin/docker-compose ps

.PHONY: upload-images-to-minikube
upload-images-to-minikube: ## Deploy: Upload docker images to minikube
	minikube image load mpc-sphinx-doc-docs:0.1.0

.PHONY: apply-kubectl-manifest
apply-kubectl-manifest: ## Deploy: Apply k8s manifest for docker images
	kubectl apply -f k8s/sphinx-doc-docs.yaml

.PHONY: run-mpc-sphinx-doc-utils-interactive
run-mpc-sphinx-doc-utils-interactive: ## Run: Run docker image interactivly (Debug / Troubleshooting)
	docker run \
		-it --entrypoint /bin/bash mpc-sphinx-doc-utils:0.1.0
