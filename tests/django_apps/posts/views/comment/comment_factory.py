import factory
from faker import Factory

from tests.django_apps.custom_auth.user_factory import UserFactory
from django_apps.posts.models import Comment, Post
from tests.django_apps.posts.views.post.post_factory import PostFactory


faker = Factory.create()


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    owner = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    text = factory.LazyAttribute(lambda _: faker.text())

