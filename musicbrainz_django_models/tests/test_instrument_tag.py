from django.test import TestCase
from ..models import instrument_tag


class test_instrument_tag(TestCase):
    def setUp(self):
        self.subject = instrument_tag()

    def test__instrument_tag__instance(self):
        self.assertIsInstance(self.subject, instrument_tag)

    def test__instrument_tag__str(self):
        self.assertEqual(str(self.subject), 'Instrument Tag')
