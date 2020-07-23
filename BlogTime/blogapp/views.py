from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
# from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogModelForm


# Create your views here.
def home(request):
    category_list = ['WellBeing', 'Sustainable Living', 'Furniture', 'Travel' , 'Design', "Technology"]
    context={
        'category_list': category_list
    }

    return render(request, 'blogapp/home.html', context)
    

@login_required()
def blog_list(request):
    blog_list = Blog.objects.all()
    print(blog_list)
    # page_number = request.GET.get('page' , 1)
    # paginator = Paginator(blog_list, 2)
    # try:
    #     blog = paginator.page(page_number)
    # except PageNotAnInteger:
    #     blog =  paginator.page(1)
    # except EmptyPage:
    #     blog = paginator.page(paginator.num_pages)
    # page_obj = paginator.get_page(page_number)
    # print(page_obj)
    context={
        'blog_list': blog_list
    }

    return render(request, 'blogapp/blogpage.html', context)


class BlogView(View):

    def get(self, request, *args, **kwargs):
        form = BlogModelForm()
        context = {
            'form' : form
        }
        return render(request, 'blogapp/blogpage.html', context)
    

    def post(self, request, *args, **kwargs):
        form = BlogModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        


