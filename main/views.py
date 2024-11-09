from django.shortcuts import render
from .models import Project, Skill


def about(request):
    return render(request, 'main/about.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def resume(request):
    return render(request, 'main/resume.html')


def services(request):
    return render(request, 'main/services.html')


def contact(request):
    return render(request, 'main/contact.html')


def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'main/home.html', {'skills': skills, 'projects': projects})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})
