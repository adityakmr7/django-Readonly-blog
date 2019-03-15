from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.auth import views as auth_views
# from users import views as user_views
from posts.views import index,postDetail, categoryDetail, blog, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('blog/', blog, name="blog"),
    path('search/', search, name='search'),
    path('<slug>/', postDetail, name='post-detail'),
    path('category/<slug>/', categoryDetail, name='category-detail'),
    # path('register/', user_views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('tinymce/', include('tinymce.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)