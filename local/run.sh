#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

pipenv run python showcase/manage.py runserver &
sleep 1
open http://localhost:8000/
