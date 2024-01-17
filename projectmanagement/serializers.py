from rest_framework import serializers
from .models import *


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['title', 'description']


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['title', 'workspace']


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['title', 'goal', 'workspace']


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epic
        fields = ['created',
                  'title',
                  'description',
                  'start_date',
                  'end_date',
                  'status',
                  'priority',
                  'estimate',
                  'hashtag']
        abstract = True


class EpicSerializer(IssueSerializer):
    class Meta:
        model = Epic
        fields = IssueSerializer.Meta.fields + ['workspace']


class StorySerializer(IssueSerializer):
    class Meta:
        model = Story
        fields = IssueSerializer.Meta.fields + ['epic', 'sprint']


class BugSerializer(IssueSerializer):
    class Meta:
        model = Bug
        fields = IssueSerializer.Meta.fields + ['epic', 'sprint']


class TaskSerializer(IssueSerializer):
    class Meta:
        model = Task
        fields = IssueSerializer.Meta.fields + ['epic', 'sprint']


class SubtaskSerializer(IssueSerializer):
    class Meta:
        model = Subtask
        fields = IssueSerializer.Meta.fields + ['story']
