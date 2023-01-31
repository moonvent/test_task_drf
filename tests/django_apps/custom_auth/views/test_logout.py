from django.contrib.auth.models import User
from django.test import tag
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from django_apps.custom_auth.serializers import LoginSerializer
from services.constants import Errors, Success
from services.response_types import error_response, success_response

from tests.django_apps.custom_auth.user_factory import UserFactory, UserFactoryForTestAuth
from tests.general_assert_tests import response_result_compare


@tag('custom_auth', 'logout')
class LogoutTestCase(APITestCase):
    user: User = None

    logout_url = reverse('custom_logout')

    def setUp(self) -> None:
        self.user = UserFactoryForTestAuth()

    def test_correct_logout(self):
        self.client.login(username=self.user.username,
                          password=self.user.password)
        actual_response = self.client.get(self.logout_url)

        response_result_compare(self, actual_response, status.HTTP_202_ACCEPTED)
        self.assertEqual(actual_response.json(),
                         success_response(description=Success.LOGOUT))

    def test_incorrect_logout(self):
        """
            test error when try to logout if not logged
        """
        actual_response = self.client.get(self.logout_url,)
        response_result_compare(self, actual_response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(actual_response.json(),
                         error_response(description=Errors.NOT_LOGGED))


