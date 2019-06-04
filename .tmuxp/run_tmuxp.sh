#!/usr/bin/env bash

# MP_OLC:SCRIPT | CMD: Tmuxp: load configuration for project: collector
PROJECT_ROOT="$(git rev-parse --show-toplevel)" tmuxp load -y main.yml
