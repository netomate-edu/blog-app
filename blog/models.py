from django.db import models
from django.utils.text import slugify

"""
Post
User
"""

class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100)
    cover = models.ImageField(upload_to='uploads')
    date = models.DateField(auto_created=True)
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title
    
    @property
    def get_cover_url(self):
        if self.cover:
            return self.cover.url
        return "#"


class Author(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    
    def __str__(self):
        return self.name

