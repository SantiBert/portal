from django.contrib import admin
from django.urls import path

from .views import (ProfileUpdate,
                    EmailUpdate,
                    NameUpdate,
                    IndexView,
                    AdministrationView,
                    AboutUsFormView,
                    SearchView,
                    )

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('administration/', AdministrationView.as_view(), name="administration"),
    path('administration/about_us/<int:pk>/',
         AboutUsFormView.as_view(), name="aboutus"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('profile/name/', NameUpdate.as_view(), name="profile_name"),
    path('resultados/', SearchView.as_view(), name='search'),

]
