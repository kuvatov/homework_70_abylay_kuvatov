from django.urls import path, include

from webapp.views.issues import IssuesView, IssueDetailsView, IssueAddView, IssueEditView, IssueDeleteView
from webapp.views.projects import ProjectsView, ProjectDetailsView, ProjectAddView, ProjectsRedirectView, \
    ProjectIssueAddView

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('', ProjectsView.as_view(), name='projects_view'),
    path('issues', IssuesView.as_view(), name='issues_view'),
    path('issue/<int:pk>', IssueDetailsView.as_view(), name='issue_details_view'),
    path('issue/add', IssueAddView.as_view(), name='issue_add_view'),
    path('issue/<int:pk>/edit', IssueEditView.as_view(), name='issue_edit_view'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete_view'),
    path('projects', ProjectsRedirectView.as_view(), name='projects_redirect_view'),
    path('project/<int:pk>', ProjectDetailsView.as_view(), name='project_details_view'),
    path('project/add', ProjectAddView.as_view(), name='project_add_view'),
    path('project/<int:pk>/issues/add', ProjectIssueAddView.as_view(), name='project_issue_add_view')
]
