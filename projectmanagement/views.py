from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

from django.http import JsonResponse
# Create your views here.


class WorkspaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkspaceSerializer
    queryset = Workspace.objects.all()


class HashtagViewSet(viewsets.ModelViewSet):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()


class SprintViewSet(viewsets.ModelViewSet):
    serializer_class = SprintSerializer
    queryset = Sprint.objects.all()


class EpicViewSet(viewsets.ModelViewSet):
    serializer_class = EpicSerializer
    queryset = Epic.objects.all()


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    queryset = Story.objects.all()


class BugViewSet(viewsets.ModelViewSet):
    serializer_class = BugSerializer
    queryset = Bug.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class SubtaskViewSet(viewsets.ModelViewSet):
    serializer_class = SubtaskSerializer
    queryset = Subtask.objects.all()


def index(request):
    return JsonResponse({'message': 'Hello World!'})
