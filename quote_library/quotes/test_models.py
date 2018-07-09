from django.test import TestCase

from .models import Quote
from .factories import QuoteFactory, ParagraphQuoteFactory, DetailedQuoteFactory, VerifiedQuoteFactory


class TestQuotesModel(TestCase):

    def test_quotes_model_required_fields(self):
        quote = QuoteFactory()

        # Checks for single object and retrieves it
        db_quote = Quote.objects.get()

        # Check primary keys the same
        self.assertEqual(db_quote.pk, db_quote.pk)

        # Check required fields match
        self.assertEquals(db_quote.text, quote.text)
        self.assertEquals(db_quote.author.pk, quote.author.pk)
        self.assertEquals(db_quote.added, quote.added)
        self.assertEquals(db_quote.verified, quote.verified)

        self.assertFalse(db_quote.verified)

    def test_quotes_model_paragraph(self):
        quote = ParagraphQuoteFactory()

        # Checks for single object and retrieves it
        db_quote = Quote.objects.get()

        # Check primary keys the same
        self.assertEqual(db_quote.pk, db_quote.pk)

        # Check required fields match
        self.assertEquals(db_quote.text, quote.text)
        self.assertEquals(db_quote.author.pk, quote.author.pk)
        self.assertEquals(db_quote.added, quote.added)
        self.assertEquals(db_quote.verified, quote.verified)

        self.assertFalse(db_quote.verified)

    def test_quotes_model_optional_fields(self):
        quote = DetailedQuoteFactory()

        # Checks for single object and retrieves it
        db_quote = Quote.objects.get()

        # Check primary keys the same
        self.assertEqual(db_quote.pk, db_quote.pk)

        # Check required fields match
        self.assertEquals(db_quote.text, quote.text)
        self.assertEquals(db_quote.author.pk, quote.author.pk)
        self.assertEquals(db_quote.added, quote.added)
        self.assertEquals(db_quote.verified, quote.verified)
        self.assertFalse(db_quote.verified)

        # Check required fields match
        self.assertEquals(db_quote.source, quote.source)
        self.assertEquals(db_quote.reference, quote.reference)
        self.assertEquals(db_quote.rating, quote.rating)

    def test_quote_model_verified(self):
        quote = VerifiedQuoteFactory()

        # Checks for single object and retrieves it
        db_quote = Quote.objects.get()

        # Check primary keys the same
        self.assertEqual(db_quote.pk, quote.pk)

        # Check reference verified is true
        self.assertEqual(db_quote.verified, quote.verified)
        self.assertTrue(db_quote.verified)
