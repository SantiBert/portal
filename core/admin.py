from django.contrib import admin

# Register your models here.
from .models import Profile, Description

admin.site.register(Profile)
admin.site.register(Description)
