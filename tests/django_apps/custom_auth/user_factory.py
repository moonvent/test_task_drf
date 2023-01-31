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

    username = factory.LazyAttribute(lambda _: faker.word())
    password = factory.LazyAttribute(lambda _: faker.password())


class UserFactoryForTestAuth(factory.django.DjangoModelFactory):
    class Meta:
        model = User    

    username = factory.LazyAttribute(lambda _: faker.word())
    password = factory.LazyAttribute(lambda _: faker.password())

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """
            Need for setup password with needed heshing for correct test custom auth
        """
        uncrtypted_pass = instance.password
        instance.set_password(uncrtypted_pass)
        instance.save()
        instance.password = uncrtypted_pass

        if create and results:
            instance.save()

