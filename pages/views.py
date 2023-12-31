from django.views.generic import TemplateView, ListView
from .models import HomePost


class HomePage(ListView):
    model = HomePost
    template_name = "home.html"


class AboutPage(TemplateView):
    template_name = "about.html"

class ServicesPage(TemplateView):
    template_name = "services.html"