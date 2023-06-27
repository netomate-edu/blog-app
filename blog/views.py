from django.shortcuts import render


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
    context = {
        'posts': posts_database
    }
    return render(request, template_name='blog/index.html', context=context)


def blog_details(request, slug):
    blog_post = {}
    for post in posts_database:
        if post.get('slug') == slug:
            blog_post = post
    
    context = {
        'post': blog_post
    }

    return render(request, template_name='blog/blog-details.html', context=context)