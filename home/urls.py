from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-me/', views.about_me, name="about-me"),
]