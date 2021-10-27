from django.test import TestCase
from .models import Project, UserProfile
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

# Create your tests here.

User = get_user_model()

class ProjectTestCase(TestCase):
    def test_project_created(self):
        User.objects.create(username="John", password="password")
        self.user = User.objects.get(username="John")
        project = Project.objects.create(
            user=self.user,
            name="Capstone Project",
            slug="capstone-project",
            description="Create an AI model which uses facial recognition to sift through a set of pictures and annotate correctly",
            completed=True,
            duration=7,
        )

        self.assertEqual(self.user.username, "John")
        self.assertEqual(project.user, self.user)

    def get_client(self):
        User.objects.create(username="John", password="password")
        self.user = User.objects.get(username="John")
        client = APIClient()
        client.login(username=self.user.username, password="password")
        return client

    def test_api_login(self):
        client = self.get_client()
        response = client.get("/api")
        self.assertEqual(response.status_code, 200)
        