import os
import sys
import pathlib

CURRENT_WORKING_DIR = pathlib.Path(__file__).resolve(strict=True).parent

PATHS = [
    str(CURRENT_WORKING_DIR / 'apps'),
    str(CURRENT_WORKING_DIR / 'apps' / 'web'),
    str(CURRENT_WORKING_DIR / 'apps' / 'web' / 'backend'),
]

sys.path.extend(PATHS)

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()

from apps.web.backend import asgi
app = asgi.application