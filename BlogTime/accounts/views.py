from django.shortcuts import render, redirect
# from .models import UserInfo
# from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from accounts.forms import LoginForm
# Create your views here.

def login_view(request):
    if request.method == "POST":
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            # login
            print(form.cleaned_data)
            user = authenticate(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password'])
            if user:
                print(user)
                login(request, user)
                return redirect('/blogs/blogs')
            else:
                print("credentials do not match")
    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/blogs/blogs')
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request, user)
            return redirect('blog_list')
    

    else:
        form  = UserCreationForm()
    
    context ={
        'form' : form
    }
    return render(request, 'accounts/register.html', context)


def view_profile(request):
    # print(user_id)    
    # user_obj = get_object_or_404(UserInfo, id=user_id)   

    return render(request, 'accounts/profile.html')


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')

