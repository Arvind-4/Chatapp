from decouple import config
from django.conf.urls import url

from .consumers import ChatConsumer

DJANGO_LIVE = config('DJANGO_LIVE', cast=bool)

websockets_urlpatterns = []

if not DJANGO_LIVE:
    websockets_urlpatterns += [
        url(r"^ws/(?P<room_name>[^/]+)/$", ChatConsumer.as_asgi()), 
    ]

else:
    websockets_urlpatterns += [
        url(r"^wss/(?P<room_name>[^/]+)/$", ChatConsumer.as_asgi()), 
    ]