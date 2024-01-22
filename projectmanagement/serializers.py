from rest_framework import serializers
from . import models
from . import custom_validators


class WorkspaceSerializer(serializers.ModelSerializer):
    hashtags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    sprints = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    epics = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = models.Workspace
        fields = ['title', 'description', 'hashtags', 'sprints', 'epics']


class HashtagSerializer(serializers.ModelSerializer):
    epics = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    stories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    bugs = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    tasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    subtasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = models.Hashtag
        fields = ['title', 'workspace', 'epics', 'stories', 'bugs', 'tasks', 'subtasks']


class SprintSerializer(serializers.ModelSerializer):

    stories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = models.Sprint
        fields = ['title', 'goal', 'workspace', 'stories']


class IssueSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(validators=[custom_validators.validate_date])
    end_date = serializers.DateTimeField(validators=[custom_validators.validate_date])

    class Meta:
        model = models.Epic
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

    stories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    bugs = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    tasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = models.Epic
        fields = IssueSerializer.Meta.fields + ['hashtag', 'workspace', 'stories', 'bugs', 'tasks']


class StorySerializer(IssueSerializer):
    subtasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = models.Story
        fields = IssueSerializer.Meta.fields + ['hashtag', 'epic', 'sprint', 'subtasks']


class BugSerializer(IssueSerializer):
    class Meta:
        model = models.Bug
        fields = IssueSerializer.Meta.fields + ['hashtag', 'epic', 'sprint']


class TaskSerializer(IssueSerializer):
    class Meta:
        model = models.Task
        fields = IssueSerializer.Meta.fields + ['hashtag', 'epic', 'sprint']


class SubtaskSerializer(IssueSerializer):
    class Meta:
        model = models.Subtask
        fields = IssueSerializer.Meta.fields + ['hashtag', 'story']
