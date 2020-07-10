#!/bin/sh

set -e

echo "=== DOCKER ENTRYPOINT ==="
COMMAND="$1"
echo "=== ATTENTION | RUN PYTHON COMMANDS USING PIPENV ==="

case "$COMMAND" in
  scrape)
    echo "=== RUNNING SCRAPPER ==="
    pipenv sync
    pipenv run python main.py
    ;;
  *)
    echo "=== RUNNING COMAND  $*==="
    sh -c "$*"
    ;;
esac