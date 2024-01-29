from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
# Create your views here.


class WorkspaceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WorkspaceSerializer
    queryset = models.Workspace.objects.all()


class HashtagViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HashtagSerializer
    queryset = models.Hashtag.objects.all()


class SprintViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SprintSerializer
    queryset = models.Sprint.objects.all()


class EpicViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EpicSerializer
    queryset = models.Epic.objects.all()


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StorySerializer
    queryset = models.Story.objects.all()


class BugViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BugSerializer
    queryset = models.Bug.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class SubtaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SubtaskSerializer
    queryset = models.Subtask.objects.all()


