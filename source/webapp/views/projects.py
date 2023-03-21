from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, RedirectView

from webapp.forms import ProjectForm, ProjectIssueForm
from webapp.models import Project, Issue


class ProjectsView(ListView):
    template_name = 'project/projects_view.html'
    model = Project
    context_object_name = 'projects'


class ProjectsRedirectView(RedirectView):
    pattern_name = 'projects_view'


class ProjectDetailsView(DetailView):
    template_name = 'project/project_details_view.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['users'] = project.users.all()
        return context


class AddUserView(PermissionRequiredMixin, DetailView):
    permission_required = 'webapp.add_project_users'
    template_name = 'project/project_add_user_view.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        context['users'] = User.objects.exclude(id__in=project.users.all().values_list('id'))
        return context

    def post(self, request: WSGIRequest, pk: int):
        project = get_object_or_404(Project, pk=pk)
        user_id = request.POST.get('user_id')
        user = User.objects.get(pk=user_id)
        project.users.add(user)
        messages.success(request, f'{user} добавлен в проект {project}')
        return redirect('project_details_view', pk=pk)


class DeleteUserView(PermissionRequiredMixin, DetailView):
    permission_required = 'webapp.delete_project_users'
    template_name = 'project/project_delete_user_view.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        context['users'] = project.users.all()
        return context

    def post(self, request: WSGIRequest, pk: int):
        project = get_object_or_404(Project, pk=pk)
        user_id = request.POST.get('user_id')
        user = User.objects.get(pk=user_id)
        project.users.remove(user)
        messages.success(request, f'{user} удален из проекта {project}')
        return redirect('project_details_view', pk=pk)


class ProjectAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_project'
    template_name = 'project/project_add_view.html'
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        project = form.save(commit=False)
        project.created_by = self.request.user
        project.save()
        project.users.add(self.request.user)
        self.object = project
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('project_details_view', kwargs={'pk': self.object.pk})


class ProjectIssueAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_project_issue'
    model = Issue
    template_name = 'project/project_issue_add_view.html'
    form_class = ProjectIssueForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        return redirect('project_details_view', pk=project.pk)
