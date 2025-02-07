from django.contrib import admin
from .models import *


@admin.register(SiteDetailModel)
class SiteDetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'email']


@admin.register(ContactUsModel)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'created', 'seen']


@admin.register(SampleFileModel)
class SampleFileAdmin(admin.ModelAdmin):
    list_display = ['title']
