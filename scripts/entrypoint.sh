#!/bin/bash

APP_PORT=${PORT:-8000}
/opt/venv/bin/daphne -b 0.0.0.0 -p $APP_PORT app:app