#!/bin/bash
#
# This script runs the Docker container for building Sphinx documentation.
# It uses the current user's UID and GID to ensure proper file permissions.
#
# Usage:
#   ./docker-sphinx-utils-run.sh
#

# TODO: view this
# RUN2  : docker run -it --user root:root -v $(pwd):/usr/local/src/app-src-mounted mp/sphinx-doc:0.1.1

# Run docker image
DOCKER_IMAGE_VERSION=0.1.1

# Please navigate to the directory where Sphinx documentation is located
# for example:
# cd apps/sphinx-doc/docs

# Following command will run the docker image with the current user's permissions
docker run --rm -it --user $(id -u):$(id -g) \
    -v $(pwd):/usr/local/src/app-build mpc-sphinx-doc-utils:${DOCKER_IMAGE_VERSION} \
    make html
