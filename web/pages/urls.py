from django.urls import path

from .views import (
    error_view,
    HomeView,
    AboutView,
    contact_us_view,
)

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('error/', error_view, name='error'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact-us/', contact_us_view, name='contact-us')
)