from django.shortcuts import render
from django.contrib import messages


def home(request):
    return render(request, "home/index.html")


def about_me(request):
    return render(request, 'home/about-me.html')
