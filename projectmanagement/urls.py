from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'workspaces', WorkspaceViewSet, basename='workspace')
router.register(r'hashtags', HashtagViewSet, basename='hashtag')
router.register(r'sprints', SprintViewSet, basename='sprint')
router.register(r'epics', EpicViewSet, basename='epic')
router.register(r'stories', StoryViewSet, basename='story')
router.register(r'bugs', BugViewSet, basename='bug')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'subtasks', SubtaskViewSet, basename='subtask')

urlpatterns = router.urls

"""
urlpatterns = [
    path('hello/', index, name='index'),
]
"""
