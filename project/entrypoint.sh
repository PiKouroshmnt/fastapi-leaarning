#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z web-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

echo "Updating database..."
alembic upgrade head

exec "$@"