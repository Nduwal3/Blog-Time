from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    category_list = ['WellBeing', 'Sustainable Living', 'Furniture', 'Travel' , 'Design', "Technology"]
    context={
        'category_list': category_list
    }

    return render(request, 'home.html', context)
    

def blog_list(request):
    blog_list = Blog.objects.all()
    print(blog_list)
    context={
        'blog_list': blog_list
    }

    return render(request, 'blogpage.html', context)

