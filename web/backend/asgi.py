"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
import dotenv
import pathlib

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / ".env"

dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

from chat.routing import websockets_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websockets_urlpatterns
        )
    )
})
