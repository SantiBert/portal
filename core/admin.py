from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Profile, Description, Quote, OtherSites, Suscriptor, FriendSites


class ProfileResourseces(resources.ModelResource):
    class Meta:
        model = Profile


class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['user']
    resource_class = ProfileResourseces


class DescriptionResourseces(resources.ModelResource):
    class Meta:
        model = Description


class DescriptionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ['user']
    resource_class = DescriptionResourseces


class QuoteResourseces(resources.ModelResource):
    class Meta:
        model = Quote


class QuoteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'active', 'autor', 'book')
    search_fields = ['text']
    resource_class = QuoteResourseces


class OtherSitesResourseces(resources.ModelResource):
    class Meta:
        model = OtherSites


class OtherSitesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ['name']
    resource_class = OtherSitesResourseces


class SuscriptorResourseces(resources.ModelResource):
    class Meta:
        model = Suscriptor


class SuscriptorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('email', 'date')
    search_fields = ['email']
    resource_class = SuscriptorResourseces


class FriendSitesResourseces(resources.ModelResource):
    class Meta:
        model = FriendSites


class FriendSitesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'site_name', 'date')
    search_fields = ['name', 'site_name']
    resource_class = FriendSitesResourseces


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(OtherSites, OtherSitesAdmin)
admin.site.register(Suscriptor, SuscriptorAdmin)
admin.site.register(FriendSites, FriendSitesAdmin)
