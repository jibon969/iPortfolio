from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from .views import (
    register_view,
    logout_view,
    login_view,
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
