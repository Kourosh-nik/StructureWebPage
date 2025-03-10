from django.contrib import admin
from .models import *


@admin.register(SoftPanelModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(SoftTraining)
class BIMTrainingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()



class ProjectImageInline(admin.TabularInline):
    model = SoftProjectImage
    extra = 1

@admin.register(SoftProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption')

@admin.register(SoftProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title',)
    inlines = [ProjectImageInline]


admin.site.register(SoftCategory, CategoryAdmin)