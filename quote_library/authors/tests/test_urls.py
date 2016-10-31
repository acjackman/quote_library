from django.core.urlresolvers import reverse, resolve

from test_plus.test import TestCase


class TestUserURLs(TestCase):
    """Test URL patterns for users app."""

    def test_list_reverse(self):
        """authors:list should reverse to /authors/."""
        self.assertEqual(reverse('authors:list'), '/authors/')

    def test_list_resolve(self):
        """/authors/ should resolve to authors:list."""
        self.assertEqual(resolve('/authors/').view_name, 'authors:list')

    def test_detail_reverse(self):
        """authors:detail should reverse to /authors/1/."""
        self.assertEqual(
            reverse('authors:detail', kwargs={'pk': '1'}),
            '/authors/1/'
        )

    def test_detail_resolve(self):
        """/authors/1/ should resolve to authors:detail."""
        self.assertEqual(resolve('/authors/1/').view_name, 'authors:detail')

    def test_update_reverse(self):
        """authors:update should reverse to /authors/~update/."""
        self.assertEqual(
            reverse('authors:update', kwargs={'pk': '1'}),
            '/authors/1/update/'
        )

    def test_update_resolve(self):
        """/authors/~update/ should resolve to authors:update."""
        self.assertEqual(
            resolve('/authors/1/update/').view_name,
            'authors:update'
        )
