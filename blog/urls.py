import uuid

from django.urls import path

from .views import (BlogEntryListView,
                    BlogEntryDetailView,
                    BlogEntryUpdateView,
                    BlogEntryCreateView,
                    BlogEntryDeleteView,
                    BlogCategoryCreate,
                    BlogCategoryListView,
                    BlogCategoryUpdateView,
                    BlogCategoryChangeState,
                    BlogAdminListView,
                    )


blog_patterns = ([
    path('', BlogEntryListView.as_view(), name='blogs'),
    path('<int:pk>/<slug:slug>/', BlogEntryDetailView.as_view(), name='blog'),
    path('create/', BlogEntryCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogEntryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',  BlogEntryDeleteView.as_view(), name='delete'),
    path('category/',  BlogCategoryCreate.as_view(), name='category'),
    path('categories/', BlogCategoryListView.as_view(), name='categories'),
    path('category/update/<str:slug>/',
         BlogCategoryUpdateView.as_view(), name='categoryUpdate'),
    path('categories/delete/<str:category_id>/',
         BlogCategoryChangeState.as_view(), name='categoriesChangeState'),

], 'blog')

blog_admin_patterns = ([
    path('administration/blogs/', BlogAdminListView.as_view(), name='blogAdminList'),

], 'blogAdmin')
