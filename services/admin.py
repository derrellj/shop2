from django.contrib import admin
from .models import ServicesModel


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ["service_page_title", "name_of_service", "price", "comments"]


admin.site.register(ServicesModel, ServiceModelAdmin)
