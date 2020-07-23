from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django import forms

# Create your models here.

class User(AbstractUser):
    # password = models.CharField(max_length=128, default="12345", widget=forms.PasswordInput())
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    profile_img = models.ImageField(upload_to='profile_img/', null=True, blank=True)

    groups = None
    user_permissions = None
