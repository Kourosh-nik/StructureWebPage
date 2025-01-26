from django.contrib import admin
from .models import BIMProject, BIMProjectImage, BIMCoworking, BIMCoworkingImage, BIMCategory, BIMLateralSys, BIMGravitySys


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()



class ProjectImageInline(admin.TabularInline):
    model = BIMProjectImage
    extra = 1

@admin.register(BIMProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption')

@admin.register(BIMProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [ProjectImageInline]



class CoworkImageInline(admin.TabularInline):
    model = BIMCoworkingImage
    extra = 1

@admin.register(BIMCoworkingImage)
class CoworkingImageAdmin(admin.ModelAdmin):
    list_display = ('coworking', 'caption')

@admin.register(BIMCoworking)
class CoworkingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [CoworkImageInline]

admin.site.register(BIMCategory, CategoryAdmin)
admin.site.register(BIMGravitySys)
admin.site.register(BIMLateralSys)