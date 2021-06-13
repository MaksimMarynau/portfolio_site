from django.shortcuts import render

from projects.models import Project
# Create your views here.

def home_view(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "home.html", context)

def about_view(request):
    return render(request, "about.html")

def work_view(request):
    return render(request, "work.html")

def contact_view(request):
    return render(request, "contact.html")
