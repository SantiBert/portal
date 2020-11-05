from django.contrib import admin
from django.urls import path

from .views import (ProfileUpdate,
                    EmailUpdate,
                    NameUpdate,
                    IndexView,
                    AdministrationView,
                    AboutUsFormView,
                    SearchView,
                    OtherSitesCreateView,
                    OtherSitesAdminListView,
                    OtherSitesUpdateView,
                    )

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('administration/', AdministrationView.as_view(), name="administration"),
    path('administration/about_us/<int:pk>/',
         AboutUsFormView.as_view(), name="aboutus"),
    path('administration/othersitecreate/',
         OtherSitesCreateView.as_view(), name="otherSitesCreate"),
    path('administration/othersitelist/',
         OtherSitesAdminListView.as_view(), name="otherSitesList"),
    path('administration/othersiteupdate/<int:pk>/',
         OtherSitesUpdateView.as_view(), name="sitesupdate"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('profile/name/', NameUpdate.as_view(), name="profile_name"),
    path('resultados/', SearchView.as_view(), name='search'),

]
