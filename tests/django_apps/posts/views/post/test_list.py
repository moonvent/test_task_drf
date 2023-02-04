import math
from random import randint
from typing import OrderedDict
from django.contrib.auth.models import User
from django.test import tag
from django.test.client import JSON_CONTENT_TYPE_RE
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django_apps.posts.models import Post
from django_apps.posts.serializers import PostSerializer
from services.constants import CONTENT_TYPE_JSON, POSTS_PAGE_SIZE, RETURN_ALL_COMMENTS_FLAG
from tests.django_apps.custom_auth.user_factory import UserFactory
from tests.django_apps.posts.views.comment.comment_factory import CommentFactory
from tests.django_apps.posts.views.post.post_factory import PostFactory
from tests.general_assert_tests import response_result_compare


def serialize_all_post(page_number: int = 0,
                       page_size: int = POSTS_PAGE_SIZE,
                       detail_view: bool = False) -> list[OrderedDict]:
    """
        Serialize post objects for test
        :param page_number: if 0 return all objects, else return object with specify page
        :param detail_view: add extra data to create serialized object
        :return: return serialized posts objects
    """
    result = None
    context = {}

    if detail_view:
        context[RETURN_ALL_COMMENTS_FLAG] = True

    if not page_number:
        result = PostSerializer(Post.objects.all(), 
                                many=True,
                                context=context).data

    else:
        offset_from, limit_to = (page_number - 1) * page_size, page_number * page_size
        result = PostSerializer(Post.objects.all()[offset_from:limit_to], 
                                many=True,
                                context=context).data

    return result


def add_comments(user: User, 
                 amount_comments: int = None):
    """
        Generate a little comment for tests
        :param amount_comments: if not none generate {amount_comments} below every posts
    """
    for post in Post.objects.all():

        amount_comments_to_generate = randint(1, 5) if not amount_comments else amount_comments

        for _ in range(amount_comments_to_generate):
            CommentFactory(owner=user,
                           post=post)


@tag('post')
class PostListTests(APITestCase):
    user: User = None
    post_create_url = post_list_url = reverse('post_list')

    def setUp(self) -> None:
        self.user = UserFactory()

        for _ in range(10):
            PostFactory(owner=self.user)

    @tag('post_list')
    def test_get_post_list(self):
        self._get_and_compare_result()

    @tag('post_list')
    def test_get_post_list_with_comments(self):
        add_comments(user=self.user)

        self._get_and_compare_result()

    @tag('post_list')
    def test_get_posts_list_without_posts(self):
        """
            Test getting post list with zero post
        """
        Post.objects.all().delete()

        self._get_and_compare_result()
        
    @tag('post_list')
    def test_get_post_list_with_pagination(self):

        general_amount_posts = 37

        for _ in range(general_amount_posts - Post.objects.count()):
            PostFactory(owner=self.user)

        for page_number in range(1, math.ceil(general_amount_posts / 10) + 1):
            self._get_and_compare_result(url=self.post_list_url + f'?page={page_number}',
                                         page_number=page_number)
            
    def _get_and_compare_result(self, 
                                url: str = post_list_url,
                                page_number: int = 0):
        """
            DRY, for compare all calculation and result in one place
        """
        actual_response = self.client.get(url)

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

    @tag('post_create')
    def test_correct_post_creation(self):
        self.client.force_login(user=self.user)
        post_data = PostSerializer(PostFactory(owner=self.user)).data
        del post_data['id'], post_data['creation_date'], post_data['views'], post_data['owner']

        actual_response = self.client.post(self.post_create_url,
                                           data=post_data)

        response_result_compare(self, actual_response, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(post_data, actual_response.data)

    @tag('post_create')
    def test_incorrect_post_creation_with_incorrect_data(self):
        """
            test INcorrect post creation with incorrect data
        """
        self.client.force_login(user=self.user)
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

    @tag('post_create')
    def test_incorrect_post_creation_without_auth(self):
        # self.client.logout()

        post_serializer = PostSerializer(PostFactory(owner=self.user))
        post_data = dict(post_serializer.data)
        del post_data['id'], post_data['creation_date'], post_data['views'], post_data['owner']

        actual_response = self.client.post(self.post_create_url,
                                           data=post_data)

        response_result_compare(self, actual_response, status.HTTP_403_FORBIDDEN)
        self.assertEqual({'detail': 'Authentication credentials were not provided.'}, 
                          actual_response.json())