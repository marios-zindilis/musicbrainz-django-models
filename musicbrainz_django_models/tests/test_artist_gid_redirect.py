from django.test import TestCase
from ..models import artist_gid_redirect


class test_artist_gid_redirect(TestCase):
    def setUp(self):
        self.subject = artist_gid_redirect()

    def test__artist_gid_redirect__instance(self):
        self.assertIsInstance(self.subject, artist_gid_redirect)

    def test__artist_gid_redirect__str(self):
        self.assertEqual(str(self.subject), 'Artist GID Redirect')
