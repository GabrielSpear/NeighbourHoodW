rom django.views.generic import TemplateView
from django.http import HttpResponse, Http404


class HomePage(TemplateView):
    template_name = 'index.html'
