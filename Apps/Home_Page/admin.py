from django.contrib import admin
from .models import *


@admin.register(SiteDetailModel)
class SiteDetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'email']

