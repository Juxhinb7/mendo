from rest_framework import serializers
from . import models
from . import custom_validators
from .custom_serializer_fields import *


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.Comment
        fields = ['id', 'user', 'title', 'text', 'project', 'epic', 'story', 'bug', 'task', 'subtask']
        extra_kwargs = {'user': {'read_only': True}}


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    hashtags = BasicIdAndTitleField(
        many=True,
        read_only=True
    )

    sprints = BasicIdAndTitleField(
        many=True,
        read_only=True
    )

    epics = BasicIdAndTitleField(
        many=True,
        read_only=True
    )

    comments = CommentField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Project
        fields = ['id', 'user', 'title', 'description', 'hashtags', 'sprints', 'epics', 'comments']
        extra_kwargs = {'user': {'read_only': True}}


class HashtagSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

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

    comments = CommentField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Hashtag
        fields = ['id', 'user', 'title', 'project', 'epics', 'stories', 'bugs', 'tasks', 'subtasks', 'comments']
        extra_kwargs = {'user': {'read_only': True}}


class SprintSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    stories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = models.Sprint
        fields = ['id', 'user', 'title', 'goal', 'start_date', 'end_date', 'project', 'stories']
        extra_kwargs = {'user': {'read_only': True}}


class IssueSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    start_date = serializers.DateTimeField(validators=[custom_validators.validate_date])
    end_date = serializers.DateTimeField(validators=[custom_validators.validate_date])

    class Meta:
        model = models.Epic
        fields = ['id',
                  'created',
                  'title',
                  'description',
                  'start_date',
                  'end_date',
                  'status',
                  'priority',
                  'estimate']
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

    comments = CommentField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Epic
        fields = IssueSerializer.Meta.fields + ['user', 'hashtag', 'project', 'stories', 'bugs', 'tasks', 'comments']
        extra_kwargs = {'user': {'read_only': True}}


class StorySerializer(IssueSerializer):
    subtasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    comments = CommentField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Story
        fields = IssueSerializer.Meta.fields + ['user', 'hashtag', 'epic', 'sprint', 'subtasks', 'comments']
        extra_kwargs = {'user': {'read_only': True}}


class BugSerializer(IssueSerializer):
    comments = CommentField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Bug
        fields = IssueSerializer.Meta.fields + ['user', 'hashtag', 'epic', 'sprint', 'comments']
        extra_kwargs = {'user': {'read_only': True}}


class TaskSerializer(IssueSerializer):
    comments = CommentField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Task
        fields = IssueSerializer.Meta.fields + ['user', 'hashtag', 'epic', 'sprint', 'comments']
        extra_kwargs = {'user': {'read_only': True}}


class SubtaskSerializer(IssueSerializer):
    comments = CommentField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Subtask
        fields = IssueSerializer.Meta.fields + ['user', 'hashtag', 'story', 'comments']
        extra_kwargs = {'user': {'read_only': True}}
