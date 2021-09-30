from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ErrorView(TemplateView):
    template_name = 'pages/error.html'


class HomeView(TemplateView):
    template_name = 'pages/home.html'
