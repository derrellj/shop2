from django.views.generic import ListView
from .models import HomePost


class HomePage(ListView):
    model = HomePost
    template_name = "home.html"
    context_object_name = "home_post"
