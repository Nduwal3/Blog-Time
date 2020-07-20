from django.shortcuts import render
# from .models import UserInfo
# from django.shortcuts import get_object_or_404

# Create your views here.

def login(request):
    return render(request, 'user/login.html')


def view_profile(request, user_id):
    print(user_id)
    
    # user_obj = get_object_or_404(UserInfo, id=user_id)
    

    return render(request, 'user/profile.html')

