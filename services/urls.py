from django.urls import path
from .views import ServiceListView

app_name = "services"

urlpatterns = [
    path("service/", ServiceListView.as_view(), name="serve"),
]
