from django.contrib import admin
from .models import *


@admin.register(RetroPanelModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(RetroTraining)
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
    model = RetroProjectImage
    extra = 1

@admin.register(RetroProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption')

@admin.register(RetroProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [ProjectImageInline]



class CoworkImageInline(admin.TabularInline):
    model = RetroCoworkingImage
    extra = 1

@admin.register(RetroCoworkingImage)
class CoworkingImageAdmin(admin.ModelAdmin):
    list_display = ('coworking', 'caption')

@admin.register(RetroCoworking)
class CoworkingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [CoworkImageInline]

admin.site.register(RetroCategory, CategoryAdmin)
admin.site.register(RetroGravitySys)
admin.site.register(RetroLateralSys)