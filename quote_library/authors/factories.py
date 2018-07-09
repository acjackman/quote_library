from datetime import datetime
import factory
from factory.django import DjangoModelFactory
from faker import Faker

from .models import Author

fake = Faker()


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    prefix = ''
    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    middle_name = ''
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    suffix = ''

    profession = factory.LazyAttribute(lambda x: fake.job())
    bio = factory.LazyAttribute(lambda x: '\n'.join(fake.paragraphs(nb=3)))
    notes = factory.LazyAttribute(lambda x: '\n'.join(fake.paragraphs(nb=2)))

    @factory.lazy_attribute
    def birth_date(self):
        date = fake.date_time_this_century(before_now=True)
        return date.date()

    @factory.lazy_attribute
    def death_date(self):
        date = fake.date_time_between_dates(datetime_start=self.birth_date)
        if datetime.now() < date:
            return date.date()
        else:
            return None


class FullAuthorFactory(AuthorFactory):

    birth_date_year = factory.LazyAttribute(lambda x: fake.pybool())

    @factory.lazy_attribute
    def death_date_year(self):
        year_only = fake.pybool()
        return False if self.death_date is None else year_only


class MaleAuthorFactory(FullAuthorFactory):

    prefix = factory.LazyAttribute(lambda x: fake.prefix_male())
    first_name = factory.LazyAttribute(lambda x: fake.first_name_male())
    middle_name = factory.LazyAttribute(lambda x: fake.first_name_male())
    last_name = factory.LazyAttribute(lambda x: fake.last_name_male())
    suffix = factory.LazyAttribute(lambda x: fake.suffix_male())


class FealeAuthorFactory(FullAuthorFactory):

    prefix = factory.LazyAttribute(lambda x: fake.prefix_female())
    first_name = factory.LazyAttribute(lambda x: fake.first_name_female())
    middle_name = factory.LazyAttribute(lambda x: fake.first_name_female())
    last_name = factory.LazyAttribute(lambda x: fake.last_name_female())
    suffix = factory.LazyAttribute(lambda x: fake.suffix_female())
