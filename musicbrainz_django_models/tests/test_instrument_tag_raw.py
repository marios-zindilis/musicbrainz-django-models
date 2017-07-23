from django.test import TestCase
from ..models import instrument_tag_raw


class test_instrument_tag_raw(TestCase):
    def setUp(self):
        self.subject = instrument_tag_raw()

    def test__instrument_tag_raw__instance(self):
        self.assertIsInstance(self.subject, instrument_tag_raw)

    def test__instrument_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Instrument Tag Raw')
