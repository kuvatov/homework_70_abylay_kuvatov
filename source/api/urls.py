from django.urls import path

from api.views.projects import ProjectDetailView

urlpatterns = [
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail_api'),
]
