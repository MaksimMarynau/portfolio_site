from django.shortcuts import render, redirect, get_object_or_404
import random
from projects.models import Project
from utils.utils import paginator_use
from .models import Tool, TravelPhoto
from .forms import ContactForm
# Create your views here.


def home_view(request):

    projects_random = None
    projects = list(Project.objects.all())
    if projects and len(projects)>3 :
        projects_random = random.sample(projects, 3)

    context = {
        "projects_random": projects_random,
    }
    return render(request, "home.html", context)


def about_view(request):

    tools_random = None
    tools = list(Tool.objects.all())
    if tools and len(tools)>=4:
        tools_random = random.sample(tools, 4)
    context = {
        "tools_random": tools_random,
    }
    return render(request, "about.html", context)


def photos_view(request):

    photos_random = None
    photos = list(TravelPhoto.objects.all())
    if photos and len(photos)>=3 :
        photos_random = random.sample(photos, 3)
    context = {
        "photos_random": photos_random,
    }
    return render(request, "photos.html", context)


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'contact.html', context)


def success_view(request):
    return render(request, 'success.html')


def tools_view(request):
    tools = Tool.objects.all().order_by('name', 'tool_num')
    tools = paginator_use(request, tools, num=10)
    context = {
        "tools": tools,
    }
    return render(request, "tools.html", context)


def tool_detail(request, id):
    tool = get_object_or_404(Tool, id=id)
    context = {
        "tool": tool,
    }
    return render(request, "tool_detail.html", context)
