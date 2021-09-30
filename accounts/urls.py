from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import UserPasswordResetForm
from .views import (
    login_view,
    register_view,
    logout_view,
    CustomPasswordChangeView,
    ProfileView,
    ProfileEditView,
)

urlpatterns = [
    path('login-view/', login_view, name='login'),
    path('register-user/', register_view, name='register'),
    path('logout-user/', logout_view, name='logout'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset/password_reset.html',
             form_class=UserPasswordResetForm,
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('change-user-password/', CustomPasswordChangeView.as_view(), name='change_password'),

    path('profile-user-view/<str:user>/', ProfileView.as_view(), name='profile'),

    path('edit-profile/', ProfileEditView.as_view(), name='profile_edit'),
]