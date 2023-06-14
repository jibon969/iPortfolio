from django.shortcuts import render


def home(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, 'home/about.html')


def project(request):
    return render(request, 'home/project.html')

