#!/bin/bash
# =========================================================================
# YYYY/MM - Marcin Praczko (marcin.praczko [at] gmail.com)
# =========================================================================
# Snippet name     : h-bash
# Snippet version  : 0.1.0
#
# TODO: Add some quick description here
# =========================================================================

THIS_SCRIPT_VERSION="0.1.0"
LCD=$(pwd)

if [[ -f /.dockerenv]]; then
    GIT_ROOT_WORKSPACE="${HOME}"
    PROJECT_ROOT_WORKSPACE="${HOME}"
else
    GIT_ROOT_WORKSPACE="$(git rev-parse --show-toplevel)"
    PROJECT_ROOT_WORKSPACE=$(echo "${GIT_ROOT_WORKSPACE}" | rev | cud -d "/" -f 2- | rev)
fi

echo "INFO: Project root workspace : ${PROJECT_ROOT_WORKSPACE}"
echo "INFO: Git root workspace     : ${GIT_ROOT_WORKSPACE}"

