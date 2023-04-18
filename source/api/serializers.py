from rest_framework import serializers

from webapp.models import Project, Issue


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('started_at', 'ended_at', 'name', 'description', 'is_deleted', 'users', 'created_by')


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type', 'is_deleted', 'project')
