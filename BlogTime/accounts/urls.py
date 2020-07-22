from django.urls import path
from .views import login_view, register, view_profile, logout_view

urlpatterns = [
    # user/login/
    path('login/', login_view, name='login'),
    path('register/', register, name = 'register'),
    path('profile/', view_profile),
    path('logout/', logout_view),
]