import os

from .base import *

print("Production Settings")

# Basic Settings

SECRET_KEY = str(os.environ.get('DJANGO_SECRET_KEY'))

ADMIN_URL = str(os.environ.get('DJANGO_ADMIN_URL'))

DEBUG = bool(int(os.environ.get('DJANGO_DEBUG')))

ALLOWED_HOSTS = []

ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('DJANGO_ALLOWED_HOSTS').split(','),
    )
)

# Authentication Settings

LOGIN_URL = 'login'

# Email Settings

EMAIL_USERNAME = str(os.environ.get('EMAIL_USERNAME'))
EMAIL_PASSWORD = str(os.environ.get('EMAIL_PASSWORD'))

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL_USERNAME
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Static Settings

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security Settings

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 2592000
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Database Settings

PG_DATABASE_NAME = str(os.environ.get('PG_DATABASE_NAME'))
PG_DATABASE_USER = str(os.environ.get('PG_DATABASE_USER'))
PG_DATABASE_PASSWORD = str(os.environ.get('PG_DATABASE_PASSWORD'))
PG_DATABASE_HOST = str(os.environ.get('PG_DATABASE_HOST'))
PG_DATABASE_PORT = int(os.environ.get('PG_DATABASE_PORT'))

DB_IS_AVAILABLE = all([
    PG_DATABASE_NAME,
    PG_DATABASE_USER,
    PG_DATABASE_PASSWORD,
    PG_DATABASE_HOST,
    PG_DATABASE_PORT
])

if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': PG_DATABASE_NAME,
            'HOST': PG_DATABASE_HOST,
            'PORT': PG_DATABASE_PORT,
            'USER': PG_DATABASE_USER,
            'PASSWORD': PG_DATABASE_PASSWORD,
        }
    }

    DATABASES['default']['CONN_MAX_AGE'] = 500
    DATABASES['default']['ATOMIC_REQUESTS'] = True

# Redis Settings

REDIS_USER = str(os.environ.get('REDIS_USER'))
REDIS_PASSWORD = str(os.environ.get('REDIS_PASSWORD'))
REDIS_PORT = str(os.environ.get('REDIS_PORT'))
REDIS_HOST = str(os.environ.get('REDIS_HOST'))

REDIS_URL = f'redis://{REDIS_USER}:{REDIS_PASSWORD}@${REDIS_HOST}:${REDIS_PORT}'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    },
}