from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Workspace(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=50)
    workspace = models.ForeignKey(Workspace, blank=False, null=True, on_delete=models.CASCADE)

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
    hashtag = models.ForeignKey(Hashtag, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Sprint(models.Model):
    title = models.CharField(max_length=50)
    goal = models.CharField(max_length=100)
    workspace = models.ForeignKey(Workspace, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Epic(Issue):
    workspace = models.ForeignKey(Workspace, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Story(Issue):
    epic = models.ForeignKey(Epic, blank=False, null=True, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Bug(Issue):
    epic = models.ForeignKey(Epic, blank=False, null=True, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(Issue):
    epic = models.ForeignKey(Epic, blank=False, null=True, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, blank=True, null=True, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subtask(Issue):
    story = models.ForeignKey(Story, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
