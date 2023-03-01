from django.urls import path, include

from webapp.views.issues import IssuesView

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path("", IssuesView.as_view(), name="issues_view")
]
