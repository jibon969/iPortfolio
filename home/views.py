from django.shortcuts import render
from .models import Project


def home(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, 'home/about.html')


def project(request):
    queryset = Project.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'home/project.html', context)

