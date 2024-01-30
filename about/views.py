from django.views.generic import ListView
from .models import AboutPage


class AboutListView(ListView):
    model = AboutPage
    template_name = "about.html"
    context_object_name = "about_post"
