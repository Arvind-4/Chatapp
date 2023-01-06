"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import pathlib

os.environ['DJANGO_SETTINGS_MODULE'] =  'backend.settings'

import django
django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from chat.routing import websockets_urlpatterns

djangoApp = get_asgi_application()

application = ProtocolTypeRouter({
    "http": djangoApp,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websockets_urlpatterns
            )
        )
    )
})