# Create your models here.
from django.db import models

# Create your models here.


class Project(models.Model):
    user = models.ForeignKey("users.CustomUser", blank=False, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    user = models.ForeignKey("users.CustomUser", blank=False, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, related_name='hashtags', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class StatusIssue(models.Model):
    class Status(models.IntegerChoices):
        TO_DO = 1, "To Do"
        IN_PROGRESS = 2, "In Progress"
        DONE = 3, "Done"

    status = models.PositiveIntegerField(
        choices=Status.choices,
        default=Status.TO_DO
    )

    class Meta:
        abstract = True


class Issue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Priority(models.IntegerChoices):
        LOW = 1, "Low"
        MEDIUM = 2, "Medium"
        HIGH = 3, "High"

    priority = models.PositiveIntegerField(
        choices=Priority.choices,
        default=Priority.HIGH
    )
    estimate = models.FloatField()

    class Meta:
        abstract = True


class StateIssue(models.Model):
    class State(models.IntegerChoices):
        BACKLOG = 1, "Backlog"
        ACTIVE = 2, "Active"

    state = models.PositiveIntegerField(
        choices=State.choices,
        default=State.BACKLOG
    )

    class Meta:
        abstract = True


class Sprint(StateIssue):
    user = models.ForeignKey("users.CustomUser", blank=False, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    goal = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    project = models.ForeignKey(Project, related_name='sprints', blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Epic(Issue, StatusIssue):
    user = models.ForeignKey("users.CustomUser", blank=False, null=True, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag,
                                related_name='epics', blank=True, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='epics', blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Story(Issue, StatusIssue, StateIssue):
    user = models.ForeignKey("users.CustomUser", blank=False, null=True, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag,
                                related_name='stories', blank=True, null=True, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, related_name='stories', blank=False, null=True, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, related_name='stories', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Bug(Issue, StatusIssue, StateIssue):
    user = models.ForeignKey("users.CustomUser", blank=False, null=True, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag,
                                related_name='bugs', blank=True, null=True, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, related_name='bugs', blank=False, null=True, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(Issue, StatusIssue, StateIssue):
    user = models.ForeignKey("users.CustomUser", blank=False, null=True, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag,
                                related_name='tasks', blank=True, null=True, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, related_name='tasks', blank=False, null=True, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, blank=True, null=True, default='',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subtask(Issue, StatusIssue, StateIssue):
    user = models.ForeignKey("users.CustomUser", blank=False, null=True, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag,
                                related_name='subtasks', blank=True, null=True, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, related_name='subtasks', blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey("users.CustomUser", blank=False, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    project = models.ForeignKey(Project, related_name="comments", blank=True, null=True, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, related_name="comments", blank=True, null=True, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, related_name="comments", blank=True, null=True, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, related_name="comments", blank=True, null=True, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name="comments", blank=True, null=True, on_delete=models.CASCADE)
    subtask = models.ForeignKey(Subtask, related_name="comments", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
