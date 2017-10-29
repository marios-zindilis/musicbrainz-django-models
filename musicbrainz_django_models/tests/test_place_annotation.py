from django.test import TestCase
from ..models import place_annotation


class test_place_annotation(TestCase):
    def setUp(self):
        self.subject = place_annotation()

    def test__place_annotation__instance(self):
        self.assertIsInstance(self.subject, place_annotation)

    def test__place_annotation__str(self):
        self.assertEqual(str(self.subject), 'Place Annotation')
