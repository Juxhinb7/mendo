# Create your models here.
from django.db import models
import datetime
from django.core.validators import ValidationError
from . import custom_validators

# Create your models here.


class Workspace(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=50)
    workspace = models.ForeignKey(Workspace, related_name='hashtags', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Issue(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Status(models.IntegerChoices):
        TO_DO = 1, "To Do"
        IN_PROGRESS = 2, "In Progress"
        DONE = 3, "Done"

    class Priority(models.IntegerChoices):
        LOW = 1, "Low"
        MEDIUM = 2, "Medium"
        HIGH = 3, "High"

    status = models.PositiveIntegerField(
        choices=Status.choices,
        default=Status.TO_DO
    )
    priority = models.PositiveIntegerField(
        choices=Priority.choices,
        default=Priority.HIGH
    )
    estimate = models.FloatField()

    class Meta:
        abstract = True


class Sprint(models.Model):
    title = models.CharField(max_length=50)
    goal = models.CharField(max_length=100)
    workspace = models.ForeignKey(Workspace, related_name='sprints', blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Epic(Issue):
    hashtag = models.ForeignKey(Hashtag,
                                related_name='epics', blank=True, null=True, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, related_name='epics', blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Story(Issue):
    hashtag = models.ForeignKey(Hashtag,
                                related_name='stories', blank=True, null=True, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, related_name='stories', blank=False, null=True, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, related_name='stories', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Bug(Issue):
    hashtag = models.ForeignKey(Hashtag,
                                related_name='bugs', blank=True, null=True, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, related_name='bugs', blank=False, null=True, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(Issue):
    hashtag = models.ForeignKey(Hashtag,
                                related_name='tasks', blank=True, null=True, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, related_name='tasks', blank=False, null=True, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, blank=True, null=True, default='',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subtask(Issue):
    hashtag = models.ForeignKey(Hashtag,
                                related_name='subtasks', blank=True, null=True, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, related_name='subtasks', blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
