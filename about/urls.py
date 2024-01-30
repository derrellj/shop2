from django.urls import path
from .views import AboutListView

app_name = "about"


urlpatterns = [
    path("about/", AboutListView.as_view(), name="about"),
]
