from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404

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
                    OtherSitesChageStateView,
                    QuoteAdminListView,
                    QuoteChageStateView,
                    QuoteCreateView,
                    QuoteUpdateView,
                    SuscribeView,
                    SuscritorAdminView,
                    SuscriptorChageStateView,
                    FriendSitesCreateView,
                    FriendSitesUpdateView,
                    FriendSitesAdminView,
                    FriendSitesChageStateView,
                    SuscritorUpdateView,
                    SuscritorDeleteView
                    )

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('administration/', AdministrationView.as_view(), name="administration"),
    path('administration/about_us/<int:pk>/',
         AboutUsFormView.as_view(), name="aboutus"),
    path('administration/othersitecreate/',
         OtherSitesCreateView.as_view(), name="otherSitesCreate"),
    path('administration/othersitedelete/<str:site_id>/',
         OtherSitesChageStateView.as_view(), name="otherSitesChangeState"),
    path('administration/othersitelist/',
         OtherSitesAdminListView.as_view(), name="otherSitesList"),
    path('administration/othersiteupdate/<int:pk>/',
         OtherSitesUpdateView.as_view(), name="sitesupdate"),
    path('administration/quotecreate/',
         QuoteCreateView.as_view(), name="quoteCreate"),
    path('administration/quotelist/',
         QuoteAdminListView.as_view(), name="quoteAdminList"),
    path('administration/quoteupdate/<int:pk>/',
         QuoteUpdateView.as_view(), name="quoteUpdate"),
    path('administration/quotedelete/<str:quote_id>/',
         QuoteChageStateView.as_view(), name="quoteDelete"),
    path('administration/suscritorslist/',
         SuscritorAdminView.as_view(), name='suscriptoradminlist'),
    path('administration/suscriptorstate/<str:subcritor_id>/',
         SuscriptorChageStateView.as_view(), name='suscriptorChangeState'),
    path('administration/suscripdelete/<int:pk>/',
         SuscritorDeleteView.as_view(), name='suscriptorDelete'),
    path('administration/update/<int:pk>/',
         SuscritorUpdateView.as_view(), name='suscriptorUpdate'),
    path('administration/friendsitescreate/',
         FriendSitesCreateView.as_view(), name="friendSiteCreate"),
    path('administration/friendsiteupdate/<int:pk>/',
         FriendSitesUpdateView.as_view(), name='friendSiteUpdate'),

    path('administration/friendsitelist/',
         FriendSitesAdminView.as_view(), name='friendSiteList'),

    path('administration/friendsitestate/<str:friendsite_id>/',
         FriendSitesChageStateView.as_view(), name='friendSiteChangeState'),

    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('profile/name/', NameUpdate.as_view(), name="profile_name"),
    path('resultados/', SearchView.as_view(), name='search'),
    path('subscribe/', SuscribeView.as_view(), name='suscribe'),



]
