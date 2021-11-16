from .base import *

import os

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'q8b(n5@^w@ucbx+x@o1#(9#@6b+%mige+p6clr=_8n0g31&ccw'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

STATICFILES_DIRS = [
    BASE_DIR / 'static-root',
]

ADMIN_URL = 'admin/'

LOGIN_URL = 'login'

STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'static-root'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587