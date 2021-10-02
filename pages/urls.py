from django.urls import path

from .views import (
    error_view,
    HomeView,
    AboutView,
    ContactUsView,
)

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('error/', error_view, name='error'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us')
)