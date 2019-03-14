from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import index,postDetail, categoryDetail, blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('blog/', blog, name="blog"),
    path('<slug>/', postDetail, name='post-detail'),
    path('category/<slug>/', categoryDetail, name='category-detail'),
    path('tinymce/', include('tinymce.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)