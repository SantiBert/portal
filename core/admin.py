from django.contrib import admin

# Register your models here.
from .models import Profile, Description, Quote, OtherSites, Suscriptor, FriendSites

admin.site.register(Profile)
admin.site.register(Description)
admin.site.register(Quote)
admin.site.register(OtherSites)
admin.site.register(Suscriptor)
admin.site.register(FriendSites)
