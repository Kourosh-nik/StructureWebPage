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
    search_fields = ('title', 'content')
    inlines = [ProjectImageInline]



class CoworkImageInline(admin.TabularInline):
    model = SoftCoworkingImage
    extra = 1

@admin.register(SoftCoworkingImage)
class CoworkingImageAdmin(admin.ModelAdmin):
    list_display = ('coworking', 'caption')

@admin.register(SoftCoworking)
class CoworkingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [CoworkImageInline]

admin.site.register(SoftCategory, CategoryAdmin)
admin.site.register(SoftVersion)
admin.site.register(SoftFee)