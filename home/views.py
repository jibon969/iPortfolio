from django.shortcuts import render


def home(request):
    return render(request, "home/index.html")


def blog(request):
    return render(request, "home/blog.html")

def detail(request):
    return render(request, "home/details.html")


def about(request):
    return render(request, 'home/about.html')


def project(request):
    return render(request, 'home/project.html')

