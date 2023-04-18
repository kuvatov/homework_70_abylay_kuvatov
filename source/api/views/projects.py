from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProjectSerializer
from webapp.models import Project


class ProjectAPIView(APIView):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response({'deleted': pk})
