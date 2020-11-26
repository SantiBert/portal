from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import BookEntry
# Register your models here.


class BookEntryResourseces(resources.ModelResource):
    class Meta:
        model = BookEntry


class BookEntryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ['name']
    resource_class = BookEntryResourseces


admin.site.register(BookEntry, BookEntryAdmin)
