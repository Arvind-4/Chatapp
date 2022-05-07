from django.urls import path
from .consumers import ChatConsumer
from django.conf import settings

websockets_urlpatterns = []

if settings.DEBUG:
    websockets_urlpatterns += [path('ws/<str:room_name>/', ChatConsumer.as_asgi())]

else:
    websockets_urlpatterns += [path('wss/<str:room_name>/', ChatConsumer.as_asgi())]