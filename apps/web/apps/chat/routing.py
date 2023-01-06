from django.urls import re_path
from django.conf import settings

from .consumers import ChatConsumer

websockets_urlpatterns = []

if settings.DEBUG:
    websockets_urlpatterns += [
        re_path(r'^ws/(?P<room_name>[^/]+)/', ChatConsumer.as_asgi()), 
    ]

else:
    websockets_urlpatterns += [
        re_path(r'^wss/(?P<room_name>[^/]+)/', ChatConsumer.as_asgi()), 
    ]

print("Websockets URL Patterns: ", websockets_urlpatterns)