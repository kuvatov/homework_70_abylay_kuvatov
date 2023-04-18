from rest_framework import serializers

from webapp.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('started_at', 'ended_at', 'name', 'description', 'is_deleted')
