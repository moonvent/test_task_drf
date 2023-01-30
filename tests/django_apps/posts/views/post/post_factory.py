import factory
from faker import Factory

from tests.django_apps.custom_auth.user_factory import UserFactory
from django_apps.posts.models import Post


faker = Factory.create()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    owner = factory.SubFactory(UserFactory)
    title = factory.LazyAttribute(lambda _: faker.word())
    text = factory.LazyAttribute(lambda _: faker.text())

