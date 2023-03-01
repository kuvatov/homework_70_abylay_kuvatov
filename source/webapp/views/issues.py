from django.views.generic import TemplateView

from webapp.models import Issue


class IssuesView(TemplateView):
    template_name = 'issues_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context
