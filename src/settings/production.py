import os
import dj_database_url
import dotenv

from .base import *

print("Production Settings")

path = BASE_DIR / '.env'
dotenv.read_dotenv(path)

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

MY_URL = os.environ.get('MY_URL')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ALLOWED_HOSTS.append(MY_URL)

LOGIN_URL = 'login'

STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'static-root'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 2592000

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587

ADMIN_URL = os.environ.get('ADMIN_URL')
print('The Admin', ADMIN_URL)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# add to production 

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL