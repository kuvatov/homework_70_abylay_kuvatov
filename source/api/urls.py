from django.urls import path

from api.views.issues import IssueAPIView
from api.views.projects import ProjectAPIView

urlpatterns = [
    path('project/<int:pk>', ProjectAPIView.as_view(), name='project_api'),
    path('issue/<int:pk>', IssueAPIView.as_view(), name='issue_api')
]
