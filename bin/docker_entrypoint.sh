#!/bin/sh

set -e

echo "=== DOCKER ENTRYPOINT ==="

COMMAND="$1"

echo "=== INSTALLING DEPENDENCIES ==="
pipenv check || pipenv install --dev

case "$COMMAND" in
  *)
    echo "=== RUNNING COMAND  $*==="
    sh -c "$*"
    ;;
esac