from django.contrib import admin

# Register your models here.
from .models import BlogCategory, BlogEntry

admin.site.register(BlogEntry)
admin.site.register(BlogCategory)
