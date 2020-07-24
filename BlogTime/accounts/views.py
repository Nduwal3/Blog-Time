from django.shortcuts import render, redirect
# from .models import UserInfo
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

# from django.urls import reverse_lazy
from django.views import View
from accounts.forms import LoginForm, RegisterForm
from .forms import UserModelForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.views.generic import UpdateView, DetailView

# Create your views here.

USER = get_user_model()



class LoginView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/blogs/blogs')
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
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
       
class SignUpView(View):

    def get(self, request, *args, **kwargs):
        form  = UserModelForm()    
        context ={
            'form' : form
        }
        return render(request, 'accounts/register.html', context)    

    def post(self, request, *args, **kwargs):
        form = UserModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

            html_file = get_template('accounts/email_template.html')
            html_content = html_file.render()
            subject = "Account Activation Required"
            from_email = 'blogTime@mail.com'
            recipients = [form.cleaned_data['email']]
            msg = EmailMultiAlternatives(subject=subject, from_email=from_email, to=recipients)
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

            return redirect('/accounts/login/') 
        else:
            print("form is invalid")

# def register(request):
#     if request.method == "POST":
#         form = UserModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()

#             html_file = get_template('accounts/email_template.html')
#             html_content = html_file.render()
#             subject = "Account Activation Required"
#             # message = "You have successfully created account"
#             from_email = 'blogTime@mail.com'
#             recipients = [form.cleaned_data['email']]
#             msg = EmailMultiAlternatives(subject=subject, from_email=from_email, to=recipients)
#             msg.attach_alternative(html_content, 'text/html')
#             msg.send()

#             return redirect('/accounts/login/') 
#         else:
#             print("form is invalid")
#     elif request.method == "GET":
#         form  = UserModelForm()    
#         context ={
#             'form' : form
#         }
#         return render(request, 'accounts/register.html', context)

class Update(UpdateView):
    form_class = UserModelForm
    template_name = 'accounts/update.html'
    model = USER
    pk_url_kwarg = 'id'
    # success_url = reverse_lazy('accounts:profile')
    success_url = ('/accounts/profile')

# class Detail(DetailView):
#     form_class = UserModelForm
#     template_name = 'accounts/profile.html'
#     model = USER
#     pk_url_kwarg = 'id'
    
    # print(user_id)    
    # user_obj = get_object_or_404(UserInfo, id=user_id) 
    # return render(request, 'accounts/profile.html')

def view_profile(request):
    # print(user_id)    
    # user_obj = get_object_or_404(UserInfo, id=user_id) 
    return render(request, 'accounts/profile.html')


def logout_view(request):
    logout(request)
    return redirect('/')

