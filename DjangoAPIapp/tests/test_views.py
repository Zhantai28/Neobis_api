from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class RegisterTests(APITestCase):
    """RegisterTests."""

    def test_create(self):
        """create."""
        url = reverse("register")
        data = {
            "email": "zhantai.ismailov@gmail.com",
            "username": "zhantai",
            "password": "1234567",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "zhantai")
