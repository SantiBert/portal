from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Contact
# Register your models here.


class ContactResourseces(resources.ModelResource):
    class Meta:
        model = Contact


class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'lastname', 'state', 'email')
    search_fields = ['name', 'lastname', 'email', ]
    resource_class = ContactResourseces


admin.site.register(Contact, ContactAdmin)
