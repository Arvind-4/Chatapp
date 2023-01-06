from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    LoginForm,
    RegistrationForm,
    UserPasswordChangeForm,
    EditProfileForm
)
from .models import Profile

# Create your views here.

User = get_user_model()


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        remember_me = request.POST.get('rememberme', None)
        if remember_me is not None:
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        username_data = form.cleaned_data.get('username')
        password_data = form.cleaned_data.get('password')
        user = authenticate(
            username=username_data,
            password=password_data
        )
        login(request=request, user=user)
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/login_view.html', context=context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        new_password = form.cleaned_data.get('password2')
        user.set_password(raw_password=new_password)
        user.save()
        next_url = request.GET.get('next', None)
        if next_url:
            return redirect(next_url)
        return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'accounts/register_view.html', context=context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'accounts/change_password/change_password.html'
    success_url = reverse_lazy('password_reset_complete')


class ProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile/profile_view.html'

    def get(self, request, user, *args, **kwargs):
        instance = User.objects.filter(username=user)
        if not instance:
            return redirect('/error/')
        obj = Profile.objects.filter(user__username=user)
        if not obj.exists():
            created = Profile.objects.create(user=
                User.objects.get(username=user)
            )
        if request.user.username == user:
            is_user = True
        else:
            is_user = False
        context = {
            'user_context': instance.first(),
            'is_user': is_user,
        }
        return render(request, self.template_name, context=context)


class ProfileEditView(LoginRequiredMixin, View):
    template_name = 'accounts/profile/edit_profile.html'

    def get(self, request, *args, **kwargs):
        instance = Profile.objects.filter(user=request.user)
        if instance.exists():
            instance_pass = Profile.objects.get(user=request.user)
        else:
            instance_pass = Profile.objects.create(user=request.user)
        form = EditProfileForm(request.POST or None, instance=instance_pass)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        instance = Profile.objects.get(user=request.user)
        if not instance:
            return redirect('/error/')
        form = EditProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context=context)