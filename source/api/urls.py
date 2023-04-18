from django.urls import path

from api.views.issues import IssueDetailView, IssueUpdateView, IssueDeleteView
from api.views.projects import ProjectDetailView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail_api'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update_api'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete_api'),
    path('issue/<int:pk>', IssueDetailView.as_view(), name='issue_detail_api'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update_api'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete_api')
]
