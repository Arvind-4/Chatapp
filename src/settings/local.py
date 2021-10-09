from .base import *

DEBUG = True

ALLOWED_HOSTS = []

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