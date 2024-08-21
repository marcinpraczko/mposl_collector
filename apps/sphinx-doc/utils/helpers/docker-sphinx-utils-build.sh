#!/bin/bash
#
# This script builds the Docker image for the Sphinx documentation utilities.
#
# Usage:
#   ./docker-sphinx-utils-build.sh
#
# Variables:
#   DOCKER_IMAGE_VERSION - The version tag for the Docker image.
#
# Example:
#   DOCKER_IMAGE_VERSION=0.1.1 ./docker-sphinx-utils-build.sh
#

# Build docker image
cd apps/sphinx-doc/utils

DOCKER_IMAGE_VERSION=0.1.1
docker build -t mpc-sphinx-doc-utils:${DOCKER_IMAGE_VERSION} . 
