from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import IssueSerializer
from webapp.models import Issue


class IssueDetailView(APIView):
    def get(self, request, pk):
        issue = Issue.objects.get(pk=pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)
