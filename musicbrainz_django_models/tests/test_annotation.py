from django.test import TestCase
from ..models import annotation


class test_annotation(TestCase):
    def setUp(self):
        self.subject = annotation()

    def test__annotation__instance(self):
        self.assertIsInstance(self.subject, annotation)

    def test__annotation__str(self):
        self.assertEqual(str(self.subject), 'Annotation')
