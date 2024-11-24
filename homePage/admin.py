from django.contrib import admin
from .models import Project, ProjectImage, Coworking, Category, LateralSys, GravitySys


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [ProjectImageInline]




@admin.register(Coworking)
class CoworkingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')


admin.site.register(Category, CategoryAdmin)
admin.site.register(GravitySys)
admin.site.register(LateralSys)