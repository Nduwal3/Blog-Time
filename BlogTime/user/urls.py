from django.urls import path
from .views import login, view_profile

urlpatterns = [
    # user/login/
    path('login/', login),
    path('detail/<int:user_id>/', view_profile)
]