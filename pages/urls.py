from django.urls import path

from .views import (
    ErrorView,
    HomeView,
)

urlpatterns = (
    path('error/', ErrorView.as_view()),
    path('', HomeView.as_view()),
)