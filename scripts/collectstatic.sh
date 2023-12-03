#!/bin/bash

echo "Collecting static files..."
/opt/venv/bin/python manage.py collectstatic --noinput --clear
echo "Static files collected"