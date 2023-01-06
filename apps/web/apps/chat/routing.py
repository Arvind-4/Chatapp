from django.urls import re_path

from .consumers import ChatConsumer

websockets_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/', ChatConsumer.as_asgi()), 
    re_path(r'^wss/(?P<room_name>[^/]+)/', ChatConsumer.as_asgi()), 
]