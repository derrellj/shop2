from django.contrib import admin
from .models import AboutPage


class AboutPageAdmin(admin.ModelAdmin):
    list_display = ["title", "introdcution", "location", "services"]


admin.site.register(AboutPage, AboutPageAdmin)
