from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectsView(ListView):
    template_name = 'project/projects_view.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetailsView(DetailView):
    template_name = 'project/project_details_view.html'
    model = Project


class ProjectAddView(CreateView):
    template_name = 'project/project_add_view.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_details_view', kwargs={'pk': self.object.pk})
