from django.urls import path

from .views import (
    error_view,
    HomeView,
)

urlpatterns = (
    path('error/', error_view),
    path('', HomeView.as_view()),
)