from django.contrib import admin
from django.urls import path

from .views import (ProfileUpdate,
                    EmailUpdate,
                    NameUpdate,
                    )

urlpatterns = [
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('profile/name/', NameUpdate.as_view(), name="profile_name"),

]
