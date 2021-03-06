import uuid
from django.contrib import admin
from django.urls import path
from .views import (BookEntryCreateView,
                    BookListView,
                    BookEntryDeleteView,
                    BookEntryUpdateView,
                    BookAdminListView,
                    BookChageStateView)

urlpatterns = [
    path('', BookListView.as_view(), name="mybooks"),
    path('bookcreate/', BookEntryCreateView.as_view(), name="bookentry"),
    path('update/<int:pk>/', BookEntryUpdateView.as_view(), name='bookupdate'),
    path('delete/<str:book_id>/', BookChageStateView.as_view(), name='bookdelete'),
    path('adminbook/', BookAdminListView.as_view(), name='adminbook')


]
