from django.test import TestCase
from ..models import area_annotation


class test_area_annotation(TestCase):
    def setUp(self):
        self.subject = area_annotation()

    def test__area_annotation__instance(self):
        self.assertIsInstance(self.subject, area_annotation)

    def test__area_annotation__str(self):
        self.assertEqual(str(self.subject), 'Area Annotation')
