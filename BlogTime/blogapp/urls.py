from django.urls import path
from .views import home, blog_list, BlogView


urlpatterns = [
    # path('', home, name="home"),
    path('blogs/', blog_list, name="blog_list"),
    path('blogs/create', BlogView.as_view(), name="create_blog")
]

