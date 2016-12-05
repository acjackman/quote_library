import factory
from factory.django import DjangoModelFactory
from faker import Faker

from .models import Quote

from ..authors.factories import AuthorFactory

fake = Faker()


def mod_rating(n):
    rating = n % 10
    return rating if rating != 0 else None


class QuoteFactory(DjangoModelFactory):
    class Meta:
        model = Quote

    text = factory.LazyAttribute(lambda x: fake.sentences(nb=3))
    author = factory.SubFactory(AuthorFactory)
    verified = False


class DetailedQuoteFactory(QuoteFactory):
    date = factory.LazyAttribute(lambda x: fake.date_time())
    source = factory.LazyAttribute(lambda x: fake.sentences(nb=1))
    reference = factory.LazyAttribute(lambda x: fake.sentences(nb=1))
    rating = factory.Sequence(lambda n: mod_rating(n))


class VerifiedQuoteFactory(QuoteFactory):
    verified = True
