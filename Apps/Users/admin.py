from django.contrib import admin

from .models import *


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'is_staff', 'is_superuser']