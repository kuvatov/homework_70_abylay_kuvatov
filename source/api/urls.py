from django.urls import path

from api.views.projects import ProjectDetailView, ProjectUpdateView

urlpatterns = [
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail_api'),
    path('projects/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update_api')
]
