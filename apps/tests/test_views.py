from .test_setup import TestSetup
from apps.user.models import UserProfile, Role, Permission
from rest_framework import status


class TestUserAPI(TestSetup):
    """
        Test: User Registration with given data
    """

    def get_token(self):
        # Create a user is a workaround in order to authentication works
        password = 'strong_password'
        data_list = [{"pk": 1, "name": "User Management", "code": "user_management", "active": True}]
        obj_list = [Permission(**data_dict) for data_dict in data_list]
        permissions = Permission.objects.bulk_create(obj_list)
        role = Role.objects.create(pk=1, name="General User", code="general_user", active=True)
        role.permission.set([1])
        user = UserProfile.objects.create(first_name="abcd", last_name="abcd", username='abcd',
                                          email='abcd@mail.com', password=password, role_id=1)
        user.set_password(user.password)
        user.save()
        self.assertEqual(user.is_active, 1, 'Active User')
        # Post to get token
        credential = {
            "username": user.username,
            "password": password
        }
        response = self.client.post(self.auth_url, credential, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.data['token']
        return token

    def test_user_cannot_register_with_no_data(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        response = self.client.post(self.user_url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_register(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        response = self.client.post(self.user_url, self.user_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_list_authenticated(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
