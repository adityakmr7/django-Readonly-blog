from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post, Author, Category
# Create your views here.

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains = query) |
            Q(content__icontains = query)
        ).distinct()
    context = {
       'queryset': queryset
    }
    return render(request, 'posts/search_result.html', context)

def index(request):
    featured = Post.objects.filter(featured = True)   #put this on carousel
    latest_post = Post.objects.order_by('-timestamp')[:6]
    startup_post = Post.objects.filter(category__title__iexact='startup')[0:3]
    opinion_post = Post.objects.filter(category__title__iexact='opinion')[0:3]
    # add a video field here
    context = {
        'featured_post': featured,
        'latest_post': latest_post,
        'startup_post': startup_post,
        'opinion_post': opinion_post
    }
    return render(request, 'posts/index.html', context)

def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'posts/blog.html', context)

@login_required
def postDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    latest_post = Post.objects.order_by('-timestamp')[0:4]
    context ={
        'post': post,
        'latest_post': latest_post
    }
    return render(request, 'posts/post_detail.html', context)


def categoryDetail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=category)
    context ={
        'category': category,
        'post': post
    }
    return render(request, 'posts/category_detail.html', context)