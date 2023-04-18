from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import IssueSerializer
from webapp.models import Issue


class IssueAPIView(APIView):
    def get(self, request, pk):
        issue = Issue.objects.get(pk=pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)

    def put(self, request, pk):
        issue = Issue.objects.get(pk=pk)
        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        issue = Issue.objects.get(pk=pk)
        issue.delete()
        return Response({'deleted': pk})
