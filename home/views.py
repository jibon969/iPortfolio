from django.shortcuts import render
from .models import Profile, Project, AboutSkill


def home(request):
    """
    :param request:
    :return:
    """
    profile = Profile.objects.all()[:1]
    context = {
        "profile": profile
    }
    return render(request, "home/index.html", context)


def about(request):
    """
    :param request:
    :return:
    """
    about_skill = AboutSkill.objects.all()[:1]
    context = {
        'about_skill': about_skill
    }
    return render(request, 'home/about.html', context)


def project(request):
    """
    :param request:
    :return:
    """
    queryset = Project.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'home/project.html', context)
