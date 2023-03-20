from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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
    queryset = Issue.objects.exclude(is_deleted=True)


class IssueAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_issue'
    template_name = 'issue/issue_add_view.html'
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue_details_view', kwargs={'pk': self.object.pk})


class IssueEditView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_issue'
    template_name = 'issue/issue_edit_view.html'
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue_details_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_issue'
    template_name = 'issue/issue_delete_view.html'
    model = Issue
    context_object_name = 'issue'
    success_url = reverse_lazy('issues_view')
