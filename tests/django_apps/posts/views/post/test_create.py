from django.contrib.auth.models import User
from django.test import tag
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django_apps.posts.serializers import PostSerializer
from django_apps.posts.views.post import PostCreate

from tests.django_apps.custom_auth.user_factory import UserFactory
from tests.django_apps.posts.views.post.post_factory import PostFactory
from tests.general_assert_tests import response_result_compare


@tag('post', 'post_create')
class PostCreateTestCase(APITestCase):
    user: User = None

    post_create_url = reverse('post_create')

    maxDiff = None

    def setUp(self) -> None:
        self.user = UserFactory()
        self.client.force_login(user=self.user)

    def test_correct_post_creation(self):
        post_data = PostSerializer(PostFactory(owner=self.user)).data
        del post_data['id'], post_data['creation_date'], post_data['views'], post_data['owner']

        actual_response = self.client.post(self.post_create_url,
                                           data=post_data)

        response_result_compare(self, actual_response, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(post_data, actual_response.data)

    def test_incorrect_post_creation_with_incorrect_data(self):
        """
            test INcorrect post creation with incorrect data
        """
        fixtures = [{}, 
                    {'title': '1'},
                    {'title': '1' * 1000,
                     'text': '1'},
                    ]

        for fixture in fixtures:
            actual_response = self.client.post(self.post_create_url,
                                               data=fixture)

            response_result_compare(self, actual_response, status.HTTP_400_BAD_REQUEST)

            serializer = PostSerializer(data=fixture)
            serializer.is_valid()

            self.assertEqual(serializer.errors, actual_response.data)

    def test_incorrect_post_creation_without_auth(self):
        self.client.logout()

        post_serializer = PostSerializer(PostFactory(owner=self.user))
        post_data = dict(post_serializer.data)
        del post_data['id'], post_data['creation_date'], post_data['views'], post_data['owner']

        actual_response = self.client.post(self.post_create_url,
                                           data=post_data)

        response_result_compare(self, actual_response, status.HTTP_403_FORBIDDEN)
        self.assertEqual({'detail': 'Authentication credentials were not provided.'}, 
                          actual_response.json())

