import uuid
from django.contrib import admin
from django.urls import path
from .views import BookEntryCreateView, BookListView, BookEntryDeleteView, BookEntryUpdateView, BookAdminListView

urlpatterns = [
    path('', BookListView.as_view(), name="mybooks"),
    path('bookcreate/', BookEntryCreateView.as_view(), name="bookentry"),
    path('update/<int:pk>/', BookEntryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookEntryDeleteView.as_view(), name='delete'),
    path('adminbook/', BookAdminListView.as_view(), name='adminbook')


]
