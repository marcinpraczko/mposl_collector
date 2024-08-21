#!/bin/bash
#
# This script builds the Docker image for the Sphinx documentation.
#
# Usage:
#   ./docker-sphinx-docs-build.sh
#
# Variables:
#   DOCKER_IMAGE_VERSION - The version tag for the Docker image.
#
# Example:
#   ./docker-sphinx-docs-build.sh
#

# Build docker image
cd apps/sphinx-doc/docs

DOCKER_IMAGE_VERSION=0.1.1
docker build -t mpc-sphinx-doc-docs:${DOCKER_IMAGE_VERSION} . 
