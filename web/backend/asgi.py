"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import dotenv
import pathlib

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / ".env"

if ENV_FILE_PATH.exists():
    dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ['DJANGO_SETTINGS_MODULE'] =  'backend.settings'

import django
django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from chat.routing import websockets_urlpatterns

django_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websockets_urlpatterns
            )
        )
    )
})