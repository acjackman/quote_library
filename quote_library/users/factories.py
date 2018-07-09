import factory
from faker import Factory as FakerFactory

from .models import User

# Generate fake data to populate database
faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    """Create Users for testing."""
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    password = factory.LazyAttribute(lambda x: faker.password())
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    email = factory.LazyAttribute(lambda x: faker.email())

    @classmethod
    def _create(cls, model_class, *args, **kwargs):

        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class StaffFactory(UserFactory):

    class Meta:
        model = User

    is_staff = True
