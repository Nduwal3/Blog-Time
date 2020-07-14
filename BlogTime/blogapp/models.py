from django.db import models

# Create your models here.

class Author(models.Model):
    username = models.CharField(max_length = 250)
    email = models.EmailField()
    password = models.CharField(max_length= 100)

class Blog(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField()
    author = models.OneToOneField(Author, on_delete = models.PROTECT, related_name = "author")
    created_date = models.DateTimeField(auto_now = False, auto_now_add = False)
    updated = models.DateTimeField(auto_now = False, auto_now_add = False)
    is_published = models.BooleanField(default = False)

