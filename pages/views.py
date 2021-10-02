from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about_us.html'

class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'

def error_view(request, exception=None):
    return render(request, 'pages/error.html', status=404)