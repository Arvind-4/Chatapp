#!/usr/bin/env bash

set -o errexit

echo "Upgrade pip..."
python -m pip install --upgrade pip

echo "Installing dependencies..."
python -m pip install -r requirements.txt

echo "Migrating database..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Creating superuser..."

DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

python manage.py createsuperuser \
    --email $DJANGO_SUPERUSER_EMAIL \
    --noinput || true

echo "Running npm install..."
npm run i

echo "Running npm Production..."
npm run production

echo "Clear Cache..."
rm -rf apps/chatjs

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear