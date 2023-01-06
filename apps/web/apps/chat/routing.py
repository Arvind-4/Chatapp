from django.conf import settings
from django.conf.urls import url

from .consumers import ChatConsumer

websockets_urlpatterns = []

if settings.DEBUG:
    websockets_urlpatterns += [
        url(r"^ws/(?P<room_name>[^/]+)/$", ChatConsumer.as_asgi()), 
    ]

else:
    websockets_urlpatterns += [
        url(r"^wss/(?P<room_name>[^/]+)/$", ChatConsumer.as_asgi()), 
    ]