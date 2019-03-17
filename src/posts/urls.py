from django.urls import path, include
from django.conf.urls.static import static

from posts.views import index,postDetail, categoryDetail, blog, search



urlpatterns = [
    path('', index, name="home"),
    path('blog/', blog, name="blog"),
    path('search/', search, name='search'),
    path('post/<slug>/', postDetail, name='post-detail'),
    path('category/<slug>/', categoryDetail, name='category-detail'),    
]
