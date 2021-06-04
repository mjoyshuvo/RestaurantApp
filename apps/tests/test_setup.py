from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetup(APITestCase):

    def setUp(self):
        self.user_url = reverse('api_v1:users_api:users-list')
        self.auth_url = reverse('api_v1:api_token')

        self.user_data = {
            "first_name": "unit",
            "last_name": "test",
            "email": "u_test@gmail.com",
            "username": "u_test",
            "password": "strong_password",
        }
        self.credential = {
            "username": self.user_data['username'],
            "password": self.user_data['password']
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
