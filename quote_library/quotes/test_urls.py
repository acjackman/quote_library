from django.core.urlresolvers import reverse, resolve

from test_plus.test import TestCase


class TestAuthorURLs(TestCase):
    """Test URL patterns for users app."""

    def test_list_reverse(self):
        """quotes:list should reverse to /quotes/."""
        self.assertEqual(reverse('quotes:list'), '/quotes/')

    def test_list_resolve(self):
        """/quotes/ should resolve to quotes:list."""
        self.assertEqual(resolve('/quotes/').view_name, 'quotes:list')

    def test_detail_reverse(self):
        """quotes:detail should reverse to /quotes/1/."""
        self.assertEqual(
            reverse('quotes:detail', kwargs={'pk': '1'}),
            '/quotes/1/'
        )

    def test_detail_resolve(self):
        """/quotes/1/ should resolve to quotes:detail."""
        self.assertEqual(resolve('/quotes/1/').view_name, 'quotes:detail')

    def test_create_reverse(self):
        """quotes:create should reverse to /quotes/1/create/."""
        self.assertEqual(
            reverse('quotes:create'),
            '/quotes/create/'
        )

    def test_create_resolve(self):
        """/quotes/1/create/ should resolve to quotes:create."""
        self.assertEqual(
            resolve('/quotes/create/').view_name,
            'quotes:create'
        )

    def test_update_reverse(self):
        """quotes:update should reverse to /quotes/1/update/."""
        self.assertEqual(
            reverse('quotes:update', kwargs={'pk': '1'}),
            '/quotes/1/update/'
        )

    def test_update_resolve(self):
        """/quotes/1/update/ should resolve to quotes:update."""
        self.assertEqual(
            resolve('/quotes/1/update/').view_name,
            'quotes:update'
        )

    def test_delete_reverse(self):
        """quotes:delete should reverse to /quotes/1/delete/."""
        self.assertEqual(
            reverse('quotes:delete', kwargs={'pk': '1'}),
            '/quotes/1/delete/'
        )

    def test_delete_resolve(self):
        """/quotes/1/delete/ should resolve to quotes:delete."""
        self.assertEqual(
            resolve('/quotes/1/delete/').view_name,
            'quotes:delete'
        )
