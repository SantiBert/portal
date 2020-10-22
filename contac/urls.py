from django.contrib import admin
from django.urls import path
from .views import ContactFormView, ContacAdminList, ConctacAdminDetailView, ContactChangeStateView

urlpatterns = [
    path('', ContactFormView.as_view(), name="contact_us"),
    path('administration/contac/', ContacAdminList.as_view(), name="admincontact"),
    path('administration/contac/<int:pk>/', ConctacAdminDetailView.as_view(), name="admincontactdetail"),
    path('administration/contac/alter-state/<int:contact_id>', ContactChangeStateView.as_view(), name="contactchangestate"),

]
