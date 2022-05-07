import os
import dj_database_url

from .base import *

print("Production Settings")

# if not 'HEROKU' in os.environ:
#     pass

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security Settings

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 2592000
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Database Settings

# DATABASE_NAME = str(os.environ.get('DATABASE_NAME'))
# DATABASE_USER = str(os.environ.get('DATABASE_USER'))
# DATABASE_PASSWORD = str(os.environ.get('DATABASE_PASSWORD'))
# DATABASE_HOST = str(os.environ.get('DATABASE_HOST'))
# DATABASE_PORT = int(os.environ.get('DATABASE_PORT'))
# DATABASE_SSL_CA = str(os.environ.get('DATABASE_SSL_CA'))

# DB_IS_AVAILABLE = all([
#     DATABASE_NAME,
#     DATABASE_USER,
#     DATABASE_PASSWORD,
#     DATABASE_HOST,
#     DATABASE_PORT,
#     DATABASE_SSL_CA
# ])

# if DB_IS_AVAILABLE:
#     DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': DATABASE_NAME,
#     'HOST': DATABASE_HOST,
#     'PORT': DATABASE_PORT,
#     'USER': DATABASE_USER,
#     'PASSWORD': DATABASE_PASSWORD,
#     'OPTIONS': {
#         'ssl': {
#             'ca': DATABASE_SSL_CA
#             }
#         }
#     }
# }

#     DATABASES['default']['CONN_MAX_AGE'] = 500
#     DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES = {}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Redis Settings

REDIS_HOST = str(os.environ.get('REDIS_HOST'))
REDIS_PORT = int(os.environ.get('REDIS_PORT'))

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(REDIS_HOST, REDIS_PORT)],
        },
    },
}