import json
from django.contrib.auth.models import User
from django.test import tag
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django_apps.posts.models import Post
from django_apps.posts.serializers import PostSerializer
from tests.django_apps.custom_auth.user_factory import UserFactory

from tests.django_apps.posts.views.post.post_factory import PostFactory
from tests.django_apps.posts.views.post.test_list import add_comments, serialize_all_post
from tests.general_assert_tests import response_result_compare


@tag('post_detail')
class PostDetailTestCase(APITestCase):
    user: User = None

    post_detail_url = None

    maxDiff = None

    def setUp(self) -> None:
        self.user = UserFactory()
        PostFactory(owner=self.user)

        self.client.force_login(self.user)

        self.post_detail_url = reverse('post_detail',
                                       kwargs=dict(pk=Post.objects.first().id))

    def _test_retrieve_post(self):
        """
            Test getting post with other conditions
        """
        post_data = serialize_all_post(detail_view=True)[0]

        actual_response = self.client.get(self.post_detail_url)

        response_result_compare(self, actual_response, status.HTTP_200_OK)
        self.assertEqual(post_data, 
                         actual_response.data)

    def _test_patch_post(self, 
                         fixtures: tuple[dict, ...]):
        """
            Test patch the post with needed_fixtures
        """
        for fixture in fixtures:
            actual_response = self.client.patch(self.post_detail_url,
                                                data=fixture)

            response_result_compare(self, actual_response, status.HTTP_200_OK)

            post_data = serialize_all_post(detail_view=True)[0]

            self.assertEqual(post_data, 
                             actual_response.data)

    def test_correct_retrieve_post(self):
        """
            Test check detail about post
        """
        self._test_retrieve_post()

    def test_correct_retrieve_post_with_comments(self):
        """
            Test check detail about post with comments
        """
        add_comments(user=self.user,
                     amount_comments=50)
        self._test_retrieve_post()

    def test_update_post(self):
        """
            Test correct update post
        """
        fixtures = ({},
                    {'title': '1'},
                    {'title': '1',
                     'text': '2'},
                    {'title': '3',
                     'text': '4',
                     'views': 22, },
                    {'title': 'asd',
                     'text': 'asdiasd',
                     'views': 'asd',            # this value not set, it's normal without errors
                     },
                    )
        
        self._test_patch_post(fixtures=fixtures)

    def test_correct_delete_post(self):
        """
            Test correct post deletion
        """
        actual_response = self.client.delete(self.post_detail_url)

        response_result_compare(self, actual_response, status.HTTP_204_NO_CONTENT)

    def test_incorrect_delete_post(self):
        """
            Test post deletion
        """
        Post.objects.all().delete()

        actual_response = self.client.delete(self.post_detail_url)

        response_result_compare(self, actual_response, status.HTTP_404_NOT_FOUND)

    def test_manipulate_without_auth(self):
        """
            Test manipulate without auth
        """
        self.client.logout()

        response_data = (self.client.patch(self.post_detail_url,
                                           data={'title': '1'}),
                         self.client.delete(self.post_detail_url),)

        
        for response in response_data:
            response_result_compare(self, response, status.HTTP_403_FORBIDDEN)

            self.assertEqual({'detail': 'Authentication credentials were not provided.'}, 
                              response.json())

    def test_manipulate_without_owner_rights(self):
        """
            Test manipulate without owner rights
        """
        self.client.logout()

        user = UserFactory()
        self.client.force_login(user)

        response_data = (self.client.patch(self.post_detail_url,
                                           data={'title': '1'}),
                         self.client.delete(self.post_detail_url),)
        
        for response in response_data:
            response_result_compare(self, response, status.HTTP_403_FORBIDDEN)

            self.assertEqual({'detail': 'You do not have permission to perform this action.'}, 
                              response.json())



