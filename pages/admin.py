from django.contrib import admin

from .models import HomePost


class PageModelAdmin(admin.ModelAdmin):
    list_display = ["artist", "art", "info"]


admin.site.register(HomePost, PageModelAdmin)
