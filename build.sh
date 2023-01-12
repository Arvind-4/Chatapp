#!/usr/bin/env bash

set -o errexit

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

python manage.py makemigrations --noinput
python manage.py migrate --noinput


DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

python manage.py createsuperuser \
    --email $DJANGO_SUPERUSER_EMAIL \
    --noinput || true

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear