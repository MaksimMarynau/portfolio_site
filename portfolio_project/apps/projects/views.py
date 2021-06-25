from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImages
from utils.utils import paginator_use

def project_index(request):
    projects = Project.objects.all()
    projects = paginator_use(request, projects, num=6)
    context = {
        'projects': projects,
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    filter = Project.objects.filter(pk=pk)
    project = get_object_or_404(filter, pk=pk)
    images = ProjectImages.objects.filter(project=project)
    context = {
        'project': project,
        'images': images,
    }
    return render(request, 'project_detail.html', context)
