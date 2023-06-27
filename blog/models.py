from django.db import models
from django.utils.text import slugify

"""
Post
User
"""

class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100)
    content = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)