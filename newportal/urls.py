
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

from blog.urls import blog_patterns, blog_admin_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('contact_us/', include('contac.urls')),
    path('book/', include('books.urls')),
    path('blog/', include(blog_patterns)),
    path('administration/', include(blog_admin_patterns)),

]
handler404 = 'core.views.handler404'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
