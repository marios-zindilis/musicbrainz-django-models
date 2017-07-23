from django.test import TestCase
from ..models import instrument_annotation


class test_instrument_annotation(TestCase):
    def setUp(self):
        self.subject = instrument_annotation()

    def test__instrument_annotation__instance(self):
        self.assertIsInstance(self.subject, instrument_annotation)

    def test__instrument_annotation__str(self):
        self.assertEqual(str(self.subject), 'Instrument Annotation')
