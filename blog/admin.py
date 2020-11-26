from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import BlogCategory, BlogEntry


class BlogEntryResourseces(resources.ModelResource):
    class Meta:
        model = BlogEntry


class BlogCategoryResourseces(resources.ModelResource):
    class Meta:
        model = BlogCategory


class BlogEntryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ['name']
    resource_class = BlogEntryResourseces


class BlogCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ['name']
    resource_class = BlogCategoryResourseces


admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
