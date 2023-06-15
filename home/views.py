from django.shortcuts import render
from .models import Project, AboutSkill


def home(request):
    return render(request, "home/index.html")


def about(request):
    about_skill = AboutSkill.objects.all()
    context = {
        'about_skill': about_skill
    }
    return render(request, 'home/about.html', context)


def project(request):
    queryset = Project.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'home/project.html', context)

