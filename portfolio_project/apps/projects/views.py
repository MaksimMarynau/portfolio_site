from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project

def project_index(request):
    projects = Project.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(projects, 3)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    context = {
        'projects': projects,
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    filter = Project.objects.filter(pk=pk)
    project = get_object_or_404(filter, pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
