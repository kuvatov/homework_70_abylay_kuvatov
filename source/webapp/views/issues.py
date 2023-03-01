from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

from webapp.models import Issue


class IssuesView(TemplateView):
    template_name = 'issues_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all().order_by('pk')
        return context


class IssueDetailsView(TemplateView):
    template_name = 'issue_details_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class IssuesRedirectView(RedirectView):
    pattern_name = 'issues_view'
