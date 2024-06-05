#!/bin/bash

# Wait for PostgreSQL to be ready
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

# Apply database migrations
python manage.py migrate

# Start the server
exec "$@"
