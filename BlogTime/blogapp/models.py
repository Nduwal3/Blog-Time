from django.db import models
from django.conf import settings

# Create your models here.
from accounts.models import User

class Author(models.Model):
    username = models.CharField(max_length = 250)
    email = models.EmailField()
    password = models.CharField(max_length= 100)

    def __str__(self):
        return '%s' % (self.username)

class Blog(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField()
    # author = models.ForeignKey(Author, on_delete = models.PROTECT, related_name = "author")
    user = models.ForeignKey(User, on_delete = models.PROTECT, related_name = "author" ,default='1')
    created_date = models.DateTimeField(auto_now = True , blank=True)
    img = models.ImageField(upload_to='images/', blank= True, null=True)
    updated = models.DateTimeField(auto_now = True, blank=True)
    is_published = models.BooleanField(default = False)

    def __str__(self):
        return '%s ||  %s' %(self.title, self.user)

