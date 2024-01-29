from django.test import TestCase
from rest_framework.test import APIClient
import json


MAIN_PATH = "/project_management"
WORKSPACE_LIST_PATH = MAIN_PATH + "/workspaces/"
HASHTAG_LIST_PATH = MAIN_PATH + "/hashtags/"
SPRINT_LIST_PATH = MAIN_PATH + "/sprints/"
EPIC_LIST_PATH = MAIN_PATH + "/epics/"
STORY_LIST_PATH = MAIN_PATH + "/stories/"


class WorkspaceViewTestcase(TestCase):
    def setUp(self):
        self.data = {"title": "Workout", "description": "All about workout"}
        self.client = APIClient()

    def test_workspace_list_all(self):
        response = self.client.get(WORKSPACE_LIST_PATH)
        self.assertEqual(response.status_code, 200)

    def test_add_workspace_item(self):
        response = self.client.post(WORKSPACE_LIST_PATH, self.data)
        json_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(json_data["title"], self.data["title"])
        self.assertEqual(json_data["description"], self.data["description"])

    def test_remove_workspace_item(self):
        post_response = self.client.post(WORKSPACE_LIST_PATH, {"title": "Studying", "description": "Studies"})
        self.assertEqual(post_response.status_code, 201)
        delete_response = self.client.delete(WORKSPACE_LIST_PATH + "1/")
        self.assertEqual(delete_response.status_code, 204)

    def test_update_workspace_item(self):
        post_response = self.client.post(WORKSPACE_LIST_PATH, {"title": "Reading", "description": "About reading"})
        self.assertEqual(post_response.status_code, 201)
        update_response = self.client.put(WORKSPACE_LIST_PATH + "1/", {"title": "Skating", "description": "That"})
        self.assertEqual(update_response.status_code, 200)
        json_data = json.loads(update_response.content.decode("utf-8"))
        self.assertEqual(json_data["title"], "Skating")
        self.assertEqual(json_data["description"], "That")


class HashtagViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_hashtag_list_all(self):
        response = self.client.get(HASHTAG_LIST_PATH)
        self.assertEqual(response.status_code, 200)

    def test_add_hashtag_item(self):
        data = {"title": "Skiing", "workspace": 1}
        add_workspace = self.client.post(WORKSPACE_LIST_PATH, {"title": "Hobbies", "description": "All about hobbies."})
        self.assertEqual(add_workspace.status_code, 201)
        add_hashtag = self.client.post(HASHTAG_LIST_PATH, data)
        json_data = json.loads(add_hashtag.content.decode("utf-8"))
        self.assertEqual(json_data["title"], data["title"])
        self.assertEqual(json_data["workspace"], data["workspace"])

    def test_update_hashtag_item(self):
        data = {"title": "Surfing", "workspace": 1}
        add_workspace = self.client.post(WORKSPACE_LIST_PATH, {"title": "Something else", "description": "Something"})
        self.assertEqual(add_workspace.status_code, 201)
        add_hashtag = self.client.post(HASHTAG_LIST_PATH, data)
        self.assertEqual(add_hashtag.status_code, 201)
        update_response = self.client.put(HASHTAG_LIST_PATH + "1/", {"title": "Watching TV", "workspace": 1})
        self.assertEqual(update_response.status_code, 200)
        json_data = json.loads(update_response.content.decode("utf-8"))
        self.assertEqual(json_data["title"], "Watching TV")
        self.assertEqual(json_data["workspace"], 1)

    def test_remove_hashtag_item(self):
        data = {"title": "Shopping", "workspace": 1}
        add_workspace = self.client.post(WORKSPACE_LIST_PATH, {"title": "Activities",
                                                               "description": "Doing activities"})
        self.assertEqual(add_workspace.status_code, 201)
        add_hashtag = self.client.post(HASHTAG_LIST_PATH, data)
        self.assertEqual(add_hashtag.status_code, 201)
        delete_hashtag = self.client.delete(HASHTAG_LIST_PATH + "1/")
        self.assertEqual(delete_hashtag.status_code, 204)


class SprintViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_sprint_list_all(self):
        response = self.client.get(SPRINT_LIST_PATH)
        self.assertEqual(response.status_code, 200)

    def test_add_sprint_item(self):
        data = {"title": "1st sprint", "goal": "The goal is to complete the 1st sprint", "workspace": 1}
        add_workspace = self.client.post(WORKSPACE_LIST_PATH, {"title": "Boxing", "description": "All about boxing"})
        self.assertEqual(add_workspace.status_code, 201)
        add_sprint = self.client.post(SPRINT_LIST_PATH, data)
        self.assertEqual(add_sprint.status_code, 201)

    def test_update_sprint_item(self):
        data = {"title": "Some sprint", "goal": "The goal of some sprint"}
        add_workspace = self.client.post(WORKSPACE_LIST_PATH, {"title": "Something", "description": "Something"})
        self.assertEqual(add_workspace.status_code, 201)
        add_sprint = self.client.post(SPRINT_LIST_PATH, data)
        self.assertEqual(add_sprint.status_code, 201)
        update_sprint = self.client.put(SPRINT_LIST_PATH + "1/", {"title": "Some sprint2", "goal": "Some sprint2"})
        self.assertEqual(update_sprint.status_code, 200)
        json_data = json.loads(update_sprint.content.decode("utf-8"))
        self.assertEqual(json_data["title"], "Some sprint2")
        self.assertEqual(json_data["goal"], "Some sprint2")

    def test_remove_sprint_item(self):
        data = {"title": "Some another sprint", "goal": "The goal of some another sprint"}
        add_workspace = self.client.post(WORKSPACE_LIST_PATH, {"title": "Somethings", "description": "Some stuff"})
        self.assertEqual(add_workspace.status_code, 201)
        add_sprint = self.client.post(SPRINT_LIST_PATH, data)
        self.assertEqual(add_sprint.status_code, 201)
        delete_sprint = self.client.delete(SPRINT_LIST_PATH + "1/")
        self.assertEqual(delete_sprint.status_code, 204)


class EpicViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_epic_list_all(self):
        response = self.client.get(EPIC_LIST_PATH)
        self.assertEqual(response.status_code, 200)

    def test_add_epic_item(self):
        data = {
            "title": "A part of a project",
            "description": "This is a part of a project",
            "start_date": "2025-04-14 02:40:12",
            "end_date": "2025-06-10 05:16:22",
            "status": 1,
            "priority": 2,
            "estimate": 20.2,
            "hashtag": 1,
            "workspace": 1
        }
        hashtag_data = {"title": "Something", "workspace": 1}
        workspace_data = {"title": "The something workspace", "description": "Workspace about something"}
        add_workspace = self.client.post(WORKSPACE_LIST_PATH, workspace_data)
        self.assertEqual(add_workspace.status_code, 201)
        add_hashtag = self.client.post(HASHTAG_LIST_PATH, hashtag_data)
        self.assertEqual(add_hashtag.status_code, 201)
        add_epic = self.client.post(EPIC_LIST_PATH, data)
        self.assertEqual(add_epic.status_code, 201)
        json_data = json.loads(add_epic.content.decode("utf-8"))
        self.assertEqual(json_data["title"], data["title"])
        self.assertEqual(json_data["description"], data["description"])
        self.assertEqual(json_data["start_date"], "2025-04-14T02:40:12")
        self.assertEqual(json_data["end_date"], "2025-06-10T05:16:22")
        self.assertEqual(json_data["status"], data["status"])
        self.assertEqual(json_data["priority"], data["priority"])
        self.assertEqual(json_data["estimate"], data["estimate"])
        self.assertEqual(json_data["hashtag"], data["hashtag"])
        self.assertEqual(json_data["workspace"], data["workspace"])

    def test_update_epic_item(self):
        data = {
            "title": "Updated title",
            "description": "Updated epic",
            "start_date": "2024-06-09 12:15:20",
            "end_date": "2025-04-10 15:22:04",
            "status": 2,
            "priority": 3,
            "estimate": 14,
            "hashtag": 1,
            "workspace": 1
        }
        hashtag_data = {"title": "Random", "workspace": 1}
        workspace_data = {"title": "Something random", "description": "Workspace about something random"}
        add_workspace = self.client.post(WORKSPACE_LIST_PATH, workspace_data)
        self.assertEqual(add_workspace.status_code, 201)
        add_hashtag =  self.client.post(HASHTAG_LIST_PATH, hashtag_data)
        self.assertEqual(add_hashtag.status_code, 201)
        add_epic = self.client.post(EPIC_LIST_PATH, {
            "title": "Some title",
            "description": "Some description",
            "start_date": "2025-09-11 05:42:20",
            "end_date": "2026-11-08 06:22:15",
            "status": 1,
            "priority": 2,
            "estimate": 10,
            "hashtag": 1,
            "workspace": 1
        })
        self.assertEqual(add_epic.status_code, 201)
        update_epic = self.client.put(EPIC_LIST_PATH + "1/", data)
        self.assertEqual(update_epic.status_code, 200)
        updated_epic_json = json.loads(update_epic.content.decode("utf-8"))
        self.assertEqual(updated_epic_json["title"], data["title"])
        self.assertEqual(updated_epic_json["description"], data["description"])
        self.assertEqual(updated_epic_json["start_date"], "2024-06-09T12:15:20")
        self.assertEqual(updated_epic_json["end_date"], "2025-04-10T15:22:04")
        self.assertEqual(updated_epic_json["status"], data["status"])
        self.assertEqual(updated_epic_json["priority"], data["priority"])
        self.assertEqual(updated_epic_json["estimate"], data["estimate"])
        self.assertEqual(updated_epic_json["hashtag"], data["hashtag"])
        self.assertEqual(updated_epic_json["workspace"], data["workspace"])

    def test_remove_epic_item(self):
        data = {
            "title": "Some epic",
            "description": "Some description about some epic",
            "start_date": "2025-09-10 08:12:22",
            "end_date": "2029-11-11 09:45:11",
            "status": 1,
            "priority": 1,
            "estimate": 10,
            "hashtag": 1,
            "workspace": 1
        }
        add_workspace =  self.client.post(WORKSPACE_LIST_PATH, {"title": "Some workspace", "description": "Something"})
        self.assertEqual(add_workspace.status_code, 201)
        add_hashtag = self.client.post(HASHTAG_LIST_PATH, {"title": "Some hashtag", "workspace": 1})
        self.assertEqual(add_hashtag.status_code, 201)
        add_epic = self.client.post(EPIC_LIST_PATH, data)
        self.assertEqual(add_epic.status_code, 201)
        remove_epic = self.client.delete(EPIC_LIST_PATH + "1/")
        self.assertEqual(remove_epic.status_code, 204)


