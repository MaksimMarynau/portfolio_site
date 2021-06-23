from django.shortcuts import render, redirect
from django.contrib import messages
import random
from projects.models import Project, ProjectImages
from .models import Tool
from .forms import ContactForm
# Create your views here.

def home_view(request):
    projects = list(Project.objects.all())

    projects_random = random.sample(projects, 3)
    context = {
        "projects_random": projects_random,
    }
    return render(request, "home.html", context)

def about_view(request):
    tools = Tool.objects.all()
    context = {
        "tools": tools,
    }
    return render(request, "about.html", context)

def work_view(request):
    return render(request, "work.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

def success_view(request):
    return render(request, 'success.html')
