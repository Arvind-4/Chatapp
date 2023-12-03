#!/bin/bash

echo "Waiting for Postgres..."
sleep 5
echo "Starting Postgres..."
echo "Connecting to Postgres..."
/opt/venv/bin/python manage.py makemigrations --noinput
/opt/venv/bin/python manage.py migrate --noinput
echo "Connected to Postgres"
set -e

echo "Creating superuser..."
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
/opt/venv/bin/python manage.py createsuperuser --email=DJANGO_SUPERUSER_EMAIL --username=DJANGO_SUPERUSER_USERNAME --noinput || true
echo "Superuser created"

echo "Collecting static files..."
/opt/venv/bin/python manage.py collectstatic --noinput --clear
echo "Static files collected"

echo "Starting server..."
APP_PORT=${PORT:-8000}
/opt/venv/bin/daphne -b 0.0.0.0 -p ${APP_PORT} app:app