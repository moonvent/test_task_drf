from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django_apps.posts.models import Post
from django_apps.posts.serializers import PostSerializer
from tests.django_apps.custom_auth.user_factory import UserFactory
from tests.django_apps.posts.views.post.post_factory import PostFactory


class PostListTests(APITestCase):
    posts = None
    user = None

    def setUp(self) -> None:
        self.posts = []
        self.user = UserFactory()

        for i in range(10):
            self.posts.append(PostFactory(owner=self.user))

    def test_get_post_list(self):
        url = reverse('post_list')

        actual_response = self.client.get(url)

        self.assertEqual(actual_response.status_code,
                         status.HTTP_200_OK)

        expected_response = PostSerializer(Post.objects.all(), many=True).data

        self.assertEqual(actual_response.data['results'], 
                         expected_response)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')
