import uuid

from django.urls import path

from .views import (BlogEntryDetailView,
                    BlogEntryUpdateView,
                    BlogEntryCreateView,
                    BlogEntryDeleteView,
                    BlogCategoryCreate,
                    BlogCategoryListView,
                    BlogCategoryUpdateView,
                    BlogCategoryChangeState,
                    BlogAdminListView,
                    BlogChangeStateView,
                    BlogEntryCategoryList,
                    BlogChangeFeaturedView,
                    SearchTagView,
                    )

blog_patterns = ([
     path('<int:pk>/<slug:slug>/', BlogEntryDetailView.as_view(), name='blog'),
     path('create/', BlogEntryCreateView.as_view(), name='create'),
     path('update/<int:pk>/', BlogEntryUpdateView.as_view(), name='update'),
     path('delete/<int:pk>/',  BlogEntryDeleteView.as_view(), name='delete'),
     path('category/',  BlogCategoryCreate.as_view(), name='category'),
     path('categories/', BlogCategoryListView.as_view(), name='listcategories'),
     path('category/update/<str:slug>/',
         BlogCategoryUpdateView.as_view(), name='categoryUpdate'),
     path('categories/delete/<str:category_id>/',
         BlogCategoryChangeState.as_view(), name='categoriesChangeState'),
     path('categories/<str:slug>/',
         BlogEntryCategoryList.as_view(), name='categories'),
     path('tags/<str:tag>', SearchTagView.as_view(), name='searchTags'),


], 'blog')

blog_admin_patterns = ([
    path('administration/blogs/', BlogAdminListView.as_view(), name='blogAdminList'),
    path('administration/blogs/alter-state/<int:blog_id>',
         BlogChangeStateView.as_view(), name='BlogChangeState'),
    path('administration/blogs/featured-state/<int:blog_id>',
         BlogChangeFeaturedView.as_view(), name='BlogFeatured'),
     
], 'blogAdmin')
