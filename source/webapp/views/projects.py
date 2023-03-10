from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from webapp.models import Project


class ProjectsView(ListView):
    template_name = 'project/projects_view.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetailsView(DetailView):
    template_name = 'project/project_details_view.html'
    model = Project
