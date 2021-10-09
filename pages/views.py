from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import ContactForm


# Create your views here.

class HomeView(TemplateView):
    template_name = 'pages/home.html'


class AboutView(TemplateView):
    template_name = 'pages/about_us.html'


# class ContactUsView(TemplateView):
#     template_name = 'pages/contact_us.html'

def contact_us_view(request):
    form = ContactForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'pages/contact_us.html', context=context)


def error_view(request, exception=None):
    return render(request, 'pages/error.html', status=404)
