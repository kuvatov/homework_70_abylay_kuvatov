from django.urls import path, include

from webapp.views.issues import IssuesView, IssueDetailsView, IssuesRedirectView, IssueAddView, IssueEditView, \
    IssueDeleteView, IssueConfirmDeleteView

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('', IssuesView.as_view(), name='issues_view'),
    path('issues', IssuesRedirectView.as_view(), name='issues_redirect_view'),
    path('issue/<int:pk>', IssueDetailsView.as_view(), name='issue_details_view'),
    path('issue/add', IssueAddView.as_view(), name='issue_add_view'),
    path('issue/<int:pk>/edit', IssueEditView.as_view(), name='issue_edit_view'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete_view'),
    path('issue/<int:pk>/confirm_delete', IssueConfirmDeleteView.as_view(), name='issue_confirm_delete_view')
]
