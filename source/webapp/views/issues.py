from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, CreateView, DetailView

from webapp.forms import IssueForm, SearchForm
from webapp.models import Issue


class IssuesView(ListView):
    model = Issue
    template_name = 'issue/issues_view.html'
    context_object_name = 'issues'
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)

        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class IssueDetailsView(DetailView):
    template_name = 'issue/issue_details_view.html'
    model = Issue


class IssueAddView(CreateView):
    template_name = 'issue/issue_add_view.html'
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue_details_view', kwargs={'pk': self.object.pk})


class IssueEditView(TemplateView):
    template_name = 'issue/issue_edit_view.html'

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
        return render(request, 'issue/issue_edit_view.html', context={
            'form': form,
            'issue': issue
        })


class IssueDeleteView(TemplateView):
    template_name = 'issue/issue_delete_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class IssueConfirmDeleteView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('issues_view')
