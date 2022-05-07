from django.urls import path
from .views import home, room, room_list_view

urlpatterns = (
    path('', home, name='enter-room'),
    path('<str:room_name>/', room, name='room'),
    path('room/list/', room_list_view, name='room_list'),
)
