from decouple import config

from .base import *

print("Production Settings")

# Basic Settings

ASGI_APPLICATION = 'backend.asgi.application'

SECRET_KEY = config('DJANGO_SECRET_KEY', cast=str)

ADMIN_URL = config('DJANGO_ADMIN_URL', cast=str)

DEBUG = config('DJANGO_DEBUG', cast=bool, default=False)

ENV_ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=str)

ALLOWED_HOSTS = []
ALLOWED_HOSTS += [x.strip() for x in ENV_ALLOWED_HOSTS.split(",")]

# Authentication Settings

LOGIN_URL = 'login'

# Email Settings

EMAIL_USERNAME = config('EMAIL_USERNAME', cast=str, default='')
EMAIL_PASSWORD = config('EMAIL_PASSWORD', cast=str, default='')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL_USERNAME
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Static Settings

STATICFILES_DIRS = [
    BASE_DIR.parent / 'public',
]
STATIC_ROOT = BASE_DIR.parent.parent / 'staticfiles_build' / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent.parent / 'mediafiles_build' / 'media'

# Security Settings

# DJANGO_LIVE = config('DJANGO_LIVE', cast=bool)
# if DJANGO_LIVE:
#     # SECURE_HSTS_SECONDS = 31536000
#     # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     # SECURE_HSTS_PRELOAD = True
#     # SECURE_CONTENT_TYPE_NOSNIFF = True
#     # SECURE_BROWSER_XSS_FILTER = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 2592000
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Database Settings

from backend.db.postgres_db import * # noqa

# Redis Settings

from backend.cache.redis_cache import * # noqa
