from django.shortcuts import render
from .models import Post, Author, Category
# Create your views here.
def index(request):
    featured = Post.objects.filter(featured = True)
    context = {
        'object_list': featured
    }
    return render(request, 'index.html', context)