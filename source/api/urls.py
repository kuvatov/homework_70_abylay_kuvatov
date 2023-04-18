from django.urls import path

from api.views.projects import ProjectDetailView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail_api'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update_api'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete_api')
]
