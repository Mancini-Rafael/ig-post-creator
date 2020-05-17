#!/bin/sh

set -e

echo "=== DOCKER ENTRYPOINT ==="
COMMAND="$1"
echo "=== ACCESSING LOCAL DEPENDENCIES ==="
echo "=== INSTALLING DEPENDENCIES ==="
pipenv sync
echo "=== ATTENTION | RUN PYTHON COMMANDS USING PIPENV ==="
case "$COMMAND" in
  run)
    echo "=== RUNNING SCRAPPER ==="
    pipenv run python main.py
    ;;
  *)
    echo "=== RUNNING COMAND  $*==="
    sh -c "$*"
    ;;
esac