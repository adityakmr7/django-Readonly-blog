from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import index,postDetail, categoryDetail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('post/<id>/', postDetail),
    path('category/<slug>/', categoryDetail),
    path('tinymce/', include('tinymce.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)