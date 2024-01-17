from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from . import serializers

from django.http import JsonResponse
# Create your views here.


class WorkspaceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WorkspaceSerializer
    queryset = models.Workspace.objects.all()

    @action(detail=True, methods=['GET'], name='List all hashtags')
    def list_hashtags(self, request, pk=None):
        self.serializer_class = serializers.HashtagSerializer
        workspace = models.Workspace.objects.get(pk=pk)
        hashtags = models.Hashtag.objects.filter(workspace=workspace)
        serializer = self.get_serializer(hashtags, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'], name='List all epics')
    def list_epics(self, request, pk=None):
        self.serializer_class = serializers.EpicSerializer
        workspace = models.Workspace.objects.get(pk=pk)
        epics = models.Epic.objects.filter(workspace=workspace)
        serializer = self.get_serializer(epics, many=True)
        return Response(serializer.data)


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


def index(request):
    return JsonResponse({'message': 'Hello World!'})
