from django.shortcuts import render
from .models import Post


def index(request):
    blog_posts = Post.objects.all()
    context = {
        'posts': blog_posts
    }
    return render(request, template_name='blog/index.html', context=context)


def blog_details(request, slug):
    post = None
    post_qs = Post.objects.filter(slug=slug)
    if post_qs.exists():
        post = post_qs[0]

    context = {
        'post': post
    }

    return render(request, template_name='blog/blog-details.html', context=context)