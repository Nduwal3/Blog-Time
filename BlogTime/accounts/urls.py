from django.urls import path
from .views import LoginView, register, view_profile, logout_view

urlpatterns = [
    # user/login/
    # path('login/', login_view, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name = 'register'),
    path('profile/', view_profile),
    path('logout/', logout_view),
]