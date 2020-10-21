from django.contrib import admin
from django.urls import path
from .views import ContactFormView, ContacAdminList, ConctacAdminDetailView

urlpatterns = [
    path('', ContactFormView.as_view(), name="contact_us"),
    path('administration/contac/', ContacAdminList.as_view(), name="admincontact"),
    path('administration/contac/<int:pk>/', ConctacAdminDetailView.as_view(), name="admincontactdetail"),

]
