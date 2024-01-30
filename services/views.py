from django.views.generic import ListView
from .models import ServicesModel


class ServiceListView(ListView):
    model = ServicesModel
    template_name = "serve.html"
    context_object_name = "services_post"
