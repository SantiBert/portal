from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

from blog.urls import blog_patterns, blog_admin_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('core.urls')),
    path('blog/', include(blog_patterns)),
    path('', include(blog_admin_patterns)),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
