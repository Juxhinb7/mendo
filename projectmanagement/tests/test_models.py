from django.test import TestCase
from projectmanagement import models

# Create your tests here.


class WorkspaceModelTestCase(TestCase):
    def setUp(self):
        self.workspace = models.Workspace.objects.create(title="Workout", description="This is about workout.")
        self.workspace.save()

    def tearDown(self):
        self.workspace.delete()

    def test_model_content(self):
        self.assertEqual(self.workspace.title, "Workout")
        self.assertEqual(self.workspace.description, "This is about workout.")


class HashtagModelTestCase(TestCase):
    def setUp(self):
        self.title = "Gym"
        self.desription = "Everything about working out."
        self.workspace = models.Workspace.objects.create(title=self.title,
                                                         description=self.desription)
        self.workspace.save()
        self.hashtag = models.Hashtag.objects.create(title="Working out", workspace=self.workspace)
        self.hashtag.save()

    def tearDown(self):
        self.workspace.delete()
        self.hashtag.delete()

    def test_hashtag_content(self):
        self.assertEqual(self.hashtag.title, "Working out")
        self.assertEqual(self.hashtag.workspace.title, self.title)
        self.assertEqual(self.hashtag.workspace.description, self.desription)


class SprintModelTestCase(TestCase):
    def setUp(self):
        self.title = "Work sprint"
        self.goal = "Work for 2 weeks extremely hard"
        self.workspace = models.Workspace.objects.create(title="Work", description="About working")
        self.workspace.save()
        self.sprint = models.Sprint.objects.create(title=self.title, goal=self.goal, workspace=self.workspace)
        self.sprint.save()

    def tearDown(self):
        self.workspace.delete()
        self.sprint.delete()

    def test_sprint_content(self):
        self.assertEqual(self.sprint.title, "Work sprint")
        self.assertEqual(self.sprint.goal, "Work for 2 weeks extremely hard")
        self.assertEqual(self.sprint.workspace.title, "Work")
        self.assertEqual(self.sprint.workspace.description, "About working")


class EpicModelTestCase(TestCase):
    def setUp(self):
        self.title = "Developing muscles"
        self.description = "This project part is about developing muscles"
        self.start_date = "2024-04-06 02:24:30"
        self.end_date = "2025-06-10 02:15:12"
        self.status = 1
        self.priority = 1
        self.estimate = 4
        self.hashtag = models.Hashtag.objects.create(title="Working out")
        self.hashtag.save()
        self.workspace = models.Workspace.objects.create(title="Fitness", description="All about fitness.")
        self.workspace.save()
        self.epic = models.Epic.objects.create(
            title=self.title,
            description=self.description,
            start_date=self.start_date,
            end_date=self.end_date,
            status=self.status,
            priority=self.priority,
            estimate=self.estimate,
            hashtag=self.hashtag,
            workspace=self.workspace
        )
        self.epic.save()

    def tearDown(self):
        self.epic.delete()
        self.hashtag.delete()
        self.workspace.delete()

    def test_epic_content(self):
        self.assertEqual(self.epic.title, self.title)
        self.assertEqual(self.epic.description, self.description)
        self.assertEqual(self.epic.start_date, self.start_date)
        self.assertEqual(self.epic.end_date, self.end_date)
        self.assertEqual(self.epic.status, self.status)
        self.assertEqual(self.epic.priority, self.priority)
        self.assertEqual(self.epic.estimate, self.estimate)
        self.assertEqual(self.epic.hashtag.title, self.hashtag.title)
        self.assertEqual(self.epic.workspace.title, self.workspace.title)


class StoryModelTestCase(TestCase):
    def setUp(self):
        self.title = "Do Bench press"
        self.description = "As a human being that wants to be healthy i would like to bench press"
        self.start_date = "2024-06-11 14:36:14"
        self.end_date = "2024-09-12 15:40:20"
        self.status = 2
        self.priority = 1
        self.estimate = 7.5
        self.hashtag = models.Hashtag.objects.create(title="Exercising")
        self.hashtag.save()
        self.workspace = models.Workspace.objects.create(title="Fitness", description="About working out.")
        self.workspace.save()
        self.sprint = models.Sprint.objects.create(title="Fitness sprint",
                                                   goal="Working out a couple weeks",
                                                   workspace=self.workspace)
        self.sprint.save()
        self.epic = models.Epic.objects.create(title="Exercising Project",
                                               description="All about exercising for about a few months",
                                               start_date="2024-06-15 10:50:12",
                                               end_date="2024-09-26 08:34:21",
                                               status=1,
                                               priority=3,
                                               estimate=120,
                                               workspace=self.workspace,
                                               )
        self.epic.save()
        self.story = models.Story.objects.create(title=self.title,
                                                 description=self.description,
                                                 start_date=self.start_date,
                                                 end_date=self.end_date,
                                                 status=self.status,
                                                 priority=self.priority,
                                                 estimate=self.estimate,
                                                 hashtag=self.hashtag,
                                                 epic=self.epic)
        self.story.save()

    def tearDown(self):
        self.story.delete()
        self.epic.delete()
        self.workspace.delete()
        self.hashtag.delete()

    def test_story_content(self):
        self.assertEqual(self.story.title, self.title)
        self.assertEqual(self.story.description, self.description)
        self.assertEqual(self.story.start_date, self.start_date)
        self.assertEqual(self.story.end_date, self.end_date)
        self.assertEqual(self.story.status, self.status)
        self.assertEqual(self.story.priority, self.priority)
        self.assertEqual(self.story.estimate, self.estimate)
        self.assertEqual(self.story.hashtag.title, self.hashtag.title)
        self.assertEqual(self.story.epic.title, self.epic.title)


class BugTestCase(TestCase):
    def setUp(self):
        self.title = "Procrastination"
        self.description = "I tend to procrastinate a lot though!"
        self.start_date = "2024-05-12 15:54:27"
        self.end_date = "2025-06-08 09:18:20"
        self.status = 1
        self.priority = 2
        self.estimate = 20.2
        self.workspace = models.Workspace.objects.create(title="Self help", description="All about self help.")
        self.workspace.save()
        self.epic = models.Epic.objects.create(title="Build Discipline",
                                               description="Find ways to build discipline.",
                                               start_date="2025-04-09 10:12:24",
                                               end_date="2025-05-09 10:12:24",
                                               status=1,
                                               priority=2,
                                               estimate=12,
                                               workspace=self.workspace)
        self.epic.save()
        self.bug = models.Bug.objects.create(title=self.title,
                                             description=self.description,
                                             start_date=self.start_date,
                                             end_date=self.end_date,
                                             status=self.status,
                                             priority=self.priority,
                                             estimate=self.estimate,
                                             epic=self.epic)
        self.bug.save()

    def tearDown(self):
        self.bug.delete()
        self.epic.delete()

    def test_bug_content(self):
        self.assertEqual(self.bug.title, self.title)
        self.assertEqual(self.bug.description, self.description)
        self.assertEqual(self.bug.start_date, self.start_date)
        self.assertEqual(self.bug.end_date, self.end_date)
        self.assertEqual(self.bug.status, self.status)
        self.assertEqual(self.bug.priority, self.priority)
        self.assertEqual(self.bug.estimate, self.estimate)


class Task(TestCase):
    def setUp(self):
        self.title = "Take out trash!"
        self.description = "I will have to take trash today."
        self.start_date = "2024-04-10 10:23:20"
        self.end_date = "2024-05-12 11:25:22"
        self.status = 2
        self.priority = 3
        self.estimate = 22.4
        self.taskHashtag = models.Hashtag.objects.create(title="House Cleaning")
        self.taskHashtag.save()
        self.hashtag = models.Hashtag.objects.create(title="Cleaning house")
        self.hashtag.save()
        self.epic = models.Epic.objects.create(
            title="House work",
            description="This is all about working around the house.",
            start_date="2024-03-15 11:30:10",
            end_date="2026-04-20 15:25:20",
            status=1,
            priority=2,
            estimate=234.2,
            hashtag=self.hashtag
        )
        self.epic.save()
        self.task = models.Task.objects.create(
            title=self.title,
            description=self.description,
            start_date=self.start_date,
            end_date=self.end_date,
            status=self.status,
            priority=self.priority,
            estimate=self.estimate,
            hashtag=self.taskHashtag,
            epic=self.epic,
        )
        self.task.save()

    def tearDown(self):
        self.task.delete()
        self.epic.delete()
        self.hashtag.delete()
        self.taskHashtag.delete()

    def test_task_content(self):
        self.assertEqual(self.task.title, self.title)
        self.assertEqual(self.task.description, self.description)
        self.assertEqual(self.task.start_date, self.start_date)
        self.assertEqual(self.task.end_date, self.end_date)
        self.assertEqual(self.task.status, self.status)
        self.assertEqual(self.task.priority, self.priority)
        self.assertEqual(self.task.estimate, self.estimate)
        self.assertEqual(self.task.hashtag.title, self.taskHashtag.title)
        self.assertEqual(self.task.epic.title, self.epic.title)


class Subtask(TestCase):
    def setUp(self):
        self.title = "Collect trash"
        self.description = "I have to collect trash, to throw it out."
        self.start_date = "2024-04-11 09:22:35"
        self.end_date = "2024-05-12 10:22:10"
        self.status = 1
        self.priority = 3
        self.estimate = 32
        self.hashtag = models.Hashtag.objects.create(title="Doing chores")
        self.hashtag.save()
        self.workspace = models.Workspace.objects.create(
            title="Work",
            description="All about work."
        )
        self.workspace.save()
        self.epic = models.Epic.objects.create(
            title="Do the job",
            description="A big part of doing the job that needs to be done",
            start_date="2024-03-10 11:25:11",
            end_date="2025-04-05 12:40:15",
            status=2,
            priority=3,
            estimate=52,
            workspace=self.workspace
        )
        self.epic.save()
        self.story = models.Story.objects.create(
            title="Clean the house",
            description="I have to do the house chores",
            start_date="2025-05-12 09:51:24",
            end_date="2025-6-11 09:52:32",
            status=2,
            estimate=11,
            epic=self.epic
        )
        self.story.save()
        self.subtask = models.Subtask.objects.create(
            title=self.title,
            description=self.description,
            start_date=self.start_date,
            end_date=self.end_date,
            status=self.status,
            estimate=self.estimate,
            hashtag=self.hashtag,
            story=self.story
        )
        self.subtask.save()

    def tearDown(self):
        self.subtask.delete()
        self.story.delete()
        self.epic.delete()
        self.workspace.delete()
        self.hashtag.delete()

    def test_subtask_content(self):
        self.assertEqual(self.subtask.title, self.title)
        self.assertEqual(self.subtask.description, self.description)
        self.assertEqual(self.subtask.start_date, self.start_date)
        self.assertEqual(self.subtask.status, self.status)
        self.assertEqual(self.subtask.estimate, self.estimate)
        self.assertEqual(self.subtask.hashtag.title, self.hashtag.title)
        self.assertEqual(self.subtask.story.title, self.story.title)
