from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()[:3]
    return render(request, 'portf/home.html', {'projects': projects})
