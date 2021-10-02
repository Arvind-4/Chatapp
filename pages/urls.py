from django.urls import path
from django.conf.urls import (
    handler404
)

from .views import (
    error_view,
    HomeView,
)

urlpatterns = (
    path('error/', error_view),
    path('', HomeView.as_view()),
)

handler404 = 'error_view'