from django.contrib import admin

from .models import *


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'is_staff', 'is_superuser']


@admin.register(UserFileModel)
class UserFileAdmin(admin.ModelAdmin):
    list_display = ['user', 'seen', 'created', 'file']
    list_filter = ['user', 'seen', 'created']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj and not obj.seen:
            obj.seen = True
            obj.save()
        return super().change_view(request, object_id, form_url, extra_context)
