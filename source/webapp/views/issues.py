from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView

from webapp.forms import IssueForm
from webapp.models import Issue


class IssuesView(ListView):
    template_name = 'issues_view.html'
    context_object_name = 'issues'
    paginate_by = 10
    paginate_orphans = 1

    def get_queryset(self):
        return Issue.objects.all().order_by('-created_at')


class IssueDetailsView(TemplateView):
    template_name = 'issue_details_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class IssuesRedirectView(RedirectView):
    pattern_name = 'issues_view'


class IssueAddView(TemplateView):
    template_name = 'issue_add_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IssueForm()
        return context

    def post(self, request: WSGIRequest, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issues_view')
        return render(request, 'issue_add_view.html', context={
            'form': form
        })


class IssueEditView(TemplateView):
    template_name = 'issue_edit_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        context['form'] = IssueForm(instance=context['issue'])
        return context

    def post(self, request: WSGIRequest, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_details_view', pk=issue.pk)
        return render(request, 'issue_edit_view.html', context={
            'form': form,
            'issue': issue
        })


class IssueDeleteView(TemplateView):
    template_name = 'issue_delete_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class IssueConfirmDeleteView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('issues_view')
