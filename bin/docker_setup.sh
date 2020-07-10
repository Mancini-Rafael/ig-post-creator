#!/bin/bash -e

echo "=== Starting project setup for docker development environment ==="
if ! command -v 'docker-compose' > /dev/null; then
  echo "Docker Compose not installed. Install before continue."
  exit 1
fi

echo "=== Docker Compose installed. Proceeding... ==="
echo "=== Building containers ==="
docker-compose build scrapper

echo "=== Setuping scrapper on mode DEVELOPMENT ==="
echo "=== Bundling  dependencies ==="
docker-compose run --rm scrapper bundle
echo "Setup Finished!"