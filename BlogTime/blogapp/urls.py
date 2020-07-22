from django.urls import path
from .views import home, blog_list


urlpatterns = [
    path('', home, name="home"),
    path('blogs/', blog_list, name="blog_list")
]

