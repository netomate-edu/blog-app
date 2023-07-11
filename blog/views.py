from django.shortcuts import render
from .models import Post


posts_database = [
    {
        "id": 1,
        "title": "Post One",
        "slug": "post-one",
        "content": "This is post one",
        "author": "Omole Ifedayo"
    },
    {
        "id": 2,
        "title": "Post Two",
        "slug": "post-two",
        "content": "This is post two",
        "author": "Jeffrey E."
    },
]


def index(request):
    blog_posts = Post.objects.all()
    context = {
        'posts': blog_posts
    }
    return render(request, template_name='blog/index.html', context=context)


def blog_details(request, slug):
    post = Post.objects.filter(slug=slug)[0]

    context = {
        'post': post
    }

    return render(request, template_name='blog/blog-details.html', context=context)