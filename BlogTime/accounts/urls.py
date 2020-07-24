from django.urls import path
from .views import LoginView, SignUpView, view_profile, logout_view, Update


# app_name = "accounts"

urlpatterns = [
    # account/login
    path('login/', LoginView.as_view(), name='login'),
    # accounts/register
    path('register/', SignUpView.as_view(), name = 'signup'),
    path('profile/', view_profile ,name="profile"),
    path('profile/update/<int:id>/',Update.as_view(),name='update'),
    path('logout/', logout_view),
]