from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Workspace)
admin.site.register(models.Hashtag)
admin.site.register(models.Sprint)
admin.site.register(models.Epic)
admin.site.register(models.Story)
admin.site.register(models.Bug)
admin.site.register(models.Task)
admin.site.register(models.Subtask)