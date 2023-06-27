from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>', views.blog_details, name='blog_details'),
]
