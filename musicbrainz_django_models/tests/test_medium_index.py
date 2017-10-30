from django.test import TestCase
from ..models import medium_index


class test_medium_index(TestCase):
    def setUp(self):
        self.subject = medium_index()

    def test__medium_index__instance(self):
        self.assertIsInstance(self.subject, medium_index)

    def test__medium_index__str(self):
        self.assertEqual(str(self.subject), 'Medium Index')
