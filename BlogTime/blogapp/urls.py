from django.urls import path
from .views import home

urlpstterns = [
    path('', home, name="home")
]