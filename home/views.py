from django.shortcuts import render
from .models import Profile, Project, AboutSkill


def home(request):
    profile = Profile.objects.all()
    context = {
        "profile": profile
    }
    return render(request, "home/index.html", context)


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

