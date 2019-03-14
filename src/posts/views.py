from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Category
# Create your views here.
def index(request):
    featured = Post.objects.filter(featured = True)   #put this on carousel
    latest_post = Post.objects.order_by('-timestamp')[:6]
    startup_post = Post.objects.filter(category__title__iexact='startup')[0:3]
    opinion_post = Post.objects.filter(category__title__iexact='opinion')[0:3]
    # add a video field here
    context = {
        'object_list': featured,
        'latest_post': latest_post,
        'startup_post': startup_post,
        'opinion_post': opinion_post
    }
    return render(request, 'index.html', context)

def postDetail(request, id):
    post = get_object_or_404(Post, id=id)
    context ={
        'post': post
    }
    return render(request, 'post_detail.html', context)