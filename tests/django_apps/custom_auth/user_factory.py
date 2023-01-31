from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from factory import faker
import factory
from faker import Factory


User = get_user_model()

faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User    

    username = factory.LazyAttribute(lambda _: faker.name())
    password = factory.LazyAttribute(lambda _: faker.password())

