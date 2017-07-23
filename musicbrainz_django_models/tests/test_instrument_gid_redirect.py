from django.test import TestCase
from ..models import instrument_gid_redirect


class test_instrument_gid_redirect(TestCase):
    def setUp(self):
        self.subject = instrument_gid_redirect()

    def test__instrument_gid_redirect__instance(self):
        self.assertIsInstance(self.subject, instrument_gid_redirect)

    def test__instrument_gid_redirect__str(self):
        self.assertEqual(str(self.subject), 'Instrument GID Redirect')
