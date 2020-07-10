#!/bin/sh

set -e

echo "=== DOCKER ENTRYPOINT ==="
COMMAND="$1"
echo "=== ATTENTION | RUN PYTHON COMMANDS USING PIPENV ==="

case "$COMMAND" in
  bundle)
    echo "=== ACCESSING LOCAL DEPENDENCIES ==="
    echo "=== INSTALLING DEPENDENCIES ==="
    pipenv sync
    ;;
  run)
    echo "=== RUNNING SCRAPPER ==="
    pipenv run python -i main.py
    ;;
  *)
    echo "=== RUNNING COMAND  $*==="
    sh -c "$*"
    ;;
esac