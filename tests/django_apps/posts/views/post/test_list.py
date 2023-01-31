import math
from typing import OrderedDict
from django.contrib.auth.models import User
from django.test import tag
from django.test.client import JSON_CONTENT_TYPE_RE
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django_apps.posts.models import Post
from django_apps.posts.serializers import PostSerializer
from services.constants import CONTENT_TYPE_JSON, POSTS_PAGE_SIZE
from tests.django_apps.custom_auth.user_factory import UserFactory
from tests.django_apps.posts.views.post.post_factory import PostFactory
from tests.general_assert_tests import response_result_compare


def serialize_all_post(page_number: int = 0,
                       page_size: int = POSTS_PAGE_SIZE) -> list[OrderedDict]:
    """
        Serialize post objects for test
        :param page_number: if 0 return all objects, else return object with specify page
        :return: return serialized posts objects
    """
    result = None

    if not page_number:
        result = PostSerializer(Post.objects.all(), 
                                many=True).data

    else:
        offset_from, limit_to = (page_number - 1) * page_size, page_number * page_size
        result = PostSerializer(Post.objects.all()[offset_from:limit_to], 
                                many=True).data

    return result


@tag('post_list')
class PostListTests(APITestCase):
    user: User = None
    post_list_url = reverse('post_list')

    def setUp(self) -> None:
        self.user = UserFactory()

        for _ in range(10):
            PostFactory(owner=self.user)

    def test_get_post_list(self):
        """
            Test getting post list
        """
        actual_response = self.client.get(self.post_list_url)

        response_result_compare(self, 
                                actual_response,
                                status.HTTP_200_OK)

        expected_response = serialize_all_post()

        self._compare_actual_and_expected_response_results(actual_response,
                                                           expected_response)

    def test_get_no_post(self):
        """
            Test getting post list with zero post
        """
        Post.objects.all().delete()

        actual_response = self.client.get(self.post_list_url)

        response_result_compare(self, 
                                actual_response,
                                status.HTTP_200_OK)

        expected_response = serialize_all_post()

        self._compare_actual_and_expected_response_results(actual_response,
                                                           expected_response)

    def test_get_post_list_with_pagination(self):
        """
            Test getting post list with pagination
        """

        general_amount_posts = 37

        for _ in range(general_amount_posts - Post.objects.count()):
            PostFactory(owner=self.user)

        for page_number in range(1, math.ceil(general_amount_posts / 10) + 1):
            actual_response = self.client.get(self.post_list_url + f'?page={page_number}')

            response_result_compare(self, 
                                    actual_response,
                                    status.HTTP_200_OK)

            expected_response = serialize_all_post(page_number=page_number)

            self._compare_actual_and_expected_response_results(actual_response,
                                                               expected_response)


    def _compare_actual_and_expected_response_results(self, 
                                                      actual_response,
                                                      expected_response):
        """
            Comparing responses data results (only data)
        """
        self.assertEqual(actual_response.data['results'], 
                         expected_response)


