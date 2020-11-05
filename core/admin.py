from django.contrib import admin

# Register your models here.
from .models import Profile, Description, Quote, OtherSites

admin.site.register(Profile)
admin.site.register(Description)
admin.site.register(Quote)
admin.site.register(OtherSites)
