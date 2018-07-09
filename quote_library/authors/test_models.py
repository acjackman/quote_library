from django.test import TestCase

from .models import Author
from .factories import AuthorFactory, MaleAuthorFactory


class TestAuthorModel(TestCase):

    def test_author_model(self):
        author = AuthorFactory()

        # Checks for single object and retrieves it
        db_author = Author.objects.get()

        # Check primary keys the same
        self.assertEqual(db_author.pk, db_author.pk)

        # Check required fields match
        self.assertEquals(db_author.last_name, author.last_name)

    def test_male_author(self):
        author = AuthorFactory()

        # Checks for single object and retrieves it
        db_author = Author.objects.get()

        # Check primary keys the same
        self.assertEqual(db_author.pk, db_author.pk)

        # Check fields match
        self.assertEquals(db_author.prefix, author.prefix)
        self.assertEquals(db_author.first_name, author.first_name)
        self.assertEquals(db_author.middle_name, author.middle_name)
        self.assertEquals(db_author.last_name, author.last_name)
        self.assertEquals(db_author.suffix, author.suffix)
        self.assertEquals(db_author.birth_date, author.birth_date)
        self.assertEquals(db_author.death_date, author.death_date)
        self.assertEquals(db_author.birth_date_year, author.birth_date_year)
        self.assertEquals(db_author.death_date_year, author.death_date_year)
        self.assertEquals(db_author.profession, author.profession)
        self.assertEquals(db_author.bio, author.bio)
        self.assertEquals(db_author.notes, author.notes)


class TestAuthorNameFunctions(TestCase):

    def test_short_name_last_name_only(self):
        author = AuthorFactory(first_name='')

        self.assertEquals(author.short_name(), author.last_name)

    def test_short_name_first_and_last_name(self):
        author = MaleAuthorFactory()

        self.assertEquals(author.short_name(), author.first_name + " " + author.last_name)

    def test_full_name_last_name_only(self):
        author = AuthorFactory(first_name='')

        self.assertEquals(author.full_name(), author.last_name)

    def test_full_name_first_and_last_name(self):
        author = MaleAuthorFactory(prefix='', middle_name='', suffix='')

        correct = author.first_name + " " + author.last_name
        self.assertEquals(author.full_name(), correct)

    def test_full_name_prefix(self):
        author = MaleAuthorFactory(middle_name='', suffix='')

        correct = ' '.join([author.prefix, author.first_name, author.last_name])
        self.assertEquals(author.full_name(), correct)

    def test_full_name_suffix(self):
        author = MaleAuthorFactory(prefix='', middle_name='')

        correct = ' '.join([author.first_name, author.last_name, author.suffix])
        self.assertEquals(author.full_name(), correct)

    def test_full_name_middle(self):
        author = MaleAuthorFactory(prefix='', suffix='')

        correct = ' '.join([author.first_name, author.middle_name, author.last_name])
        self.assertEquals(author.full_name(), correct)

    def test_full_name_all_parts(self):
        author = MaleAuthorFactory()

        correct = ' '.join([author.prefix, author.first_name, author.middle_name, author.last_name, author.suffix])
        self.assertEquals(author.full_name(), correct)
