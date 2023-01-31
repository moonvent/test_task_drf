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


@tag('custom_auth', 'login')
class LoginTestCase(APITestCase):
    user: User = None

    login_url = reverse('custom_login')

    def setUp(self) -> None:
        self.user = UserFactoryForTestAuth()
        # self.client.force_login(self.user)

    def _test_correct_login(self):
        actual_response = self.client.post(self.login_url,
                                           data=dict(username=self.user.username,
                                                     password=self.user.password),
                                           format='json')

        response_result_compare(self, actual_response, status.HTTP_202_ACCEPTED)
        self.assertEqual(actual_response.json(),
                         success_response(description=Success.LOGGED))

    def test_correct_login(self):
        self._test_correct_login()
        
    def test_incorrect_login(self):
        fixtures = ({},
                    {'username': '1',},
                    {'username': '1',
                     'password': '2'
                     },
                    )

        for fixture in fixtures:
            actual_response = self.client.post(self.login_url,
                                               data=fixture,
                                               format='json')

            response_result_compare(self, actual_response, status.HTTP_400_BAD_REQUEST)

    def test_auth_with_get_method(self):
        actual_response = self.client.get(self.login_url)
        response_result_compare(self, actual_response, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_repeated_auth(self):
        self._test_correct_login()

        actual_response = self.client.post(self.login_url,
                                           data=dict(username=self.user.username,
                                                     password=self.user.password),
                                           format='json')

        response_result_compare(self, actual_response, status.HTTP_400_BAD_REQUEST)


