from test_plus.test import TestCase

from .factories import QuoteFactory
from ..users.factories import StaffFactory


class QuoteViewTestCase(TestCase):

    def setUp(self):
        self.Quote = QuoteFactory()


class TestQuoteDetailView(QuoteViewTestCase):

    def test_view_Quote(self):
        self.assertGoodView('quotes:detail', pk=self.Quote.pk)


class TestQuoteListView(QuoteViewTestCase):

    def test_list_no_Quotes(self):
        self.Quote.delete()
        self.assertGoodView('quotes:list')

    def test_list_one_Quote(self):
        self.Quote.delete()
        self.assertGoodView('quotes:list')

    def test_list_five_Quotes(self):
        quotes = []
        for i in range(4):
            quotes.append(QuoteFactory())


class QuoteModifyViewTestCase(QuoteViewTestCase):

    def setUp(self):
        self.staff_user = StaffFactory(password='password')
        super(QuoteModifyViewTestCase, self).setUp()


class TestQuoteCreateView(QuoteModifyViewTestCase):

    def test_annon_user_blocked(self):
        response = self.get('quotes:create')
        self.response_302(response)

    def test_staff_user_acccess(self):
        with self.login(username=self.staff_user.username):
            self.assertGoodView('quotes:create')


class TestQuoteUpdateView(QuoteModifyViewTestCase):

    def test_annon_user_blocked(self):
        response = self.get('quotes:update', pk=self.Quote.pk)
        self.response_302(response)

    def test_staff_user_acccess(self):
        with self.login(username=self.staff_user.username):
            self.assertGoodView('quotes:update', pk=self.Quote.pk)


class TestQuoteDeleteView(QuoteModifyViewTestCase):

    def test_annon_user_blocked(self):
        response = self.get('quotes:delete', pk=self.Quote.pk)
        self.response_302(response)

    def test_staff_user_acccess(self):
        with self.login(username=self.staff_user.username):
            self.assertGoodView('quotes:delete', pk=self.Quote.pk)
