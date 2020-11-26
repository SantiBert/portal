
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.urls import blog_patterns, blog_admin_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('contact_us/', include('contac.urls')),
    path('book/', include('books.urls')),
    path('social/', include('social.urls')),
    path('blog/', include(blog_patterns)),
    path('administration/', include(blog_admin_patterns)),
    path('ckeditor', include('ckeditor_uploader.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
