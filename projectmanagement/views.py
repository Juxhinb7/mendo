from rest_framework import viewsets

from . import models
from . import serializers


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class HashtagViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HashtagSerializer
    queryset = models.Hashtag.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class SprintViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SprintSerializer
    queryset = models.Sprint.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class EpicViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EpicSerializer
    queryset = models.Epic.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StorySerializer
    queryset = models.Story.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class BugViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BugSerializer
    queryset = models.Bug.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class SubtaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SubtaskSerializer
    queryset = models.Subtask.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


