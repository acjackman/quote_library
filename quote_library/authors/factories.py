from datetime import datetime
import factory
from factory.django import DjangoModelFactory
from faker import Faker

from .models import Author

fake = Faker()


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    birth_date = factory.LazyAttribute(lambda x: fake.date_time_this_century(before_now=True))

    profession = fake.job()
    bio = fake.paragraphs(nb=3)
    notes = fake.paragraphs(nb=2)

    @factory.LazyAttribute
    def death_date(self):
        date = fake.date_time_between_dates(datetime_start=self.birth_date)
        if datetime.now() < date:
            return date
        else:
            return None
