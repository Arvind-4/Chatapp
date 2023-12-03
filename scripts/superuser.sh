#!/bin/bash

echo "Creating superuser..."
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
/opt/venv/bin/python manage.py createsuperuser --email=DJANGO_SUPERUSER_EMAIL --username=DJANGO_SUPERUSER_USERNAME --noinput || true
echo "Superuser created"