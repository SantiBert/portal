from django.contrib import admin
from django.urls import path
from .views import LinkAdminListView, LinkUpdateView

urlpatterns = [
    path('administration/social/', LinkAdminListView.as_view(), name="social_list"),
    path('administration/socialupdate/<str:pk>/',
         LinkUpdateView.as_view(), name="socialUpdate"),


]
