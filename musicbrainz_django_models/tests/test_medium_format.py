from django.test import TestCase
from ..models import medium_format


class test_medium_format(TestCase):
    def setUp(self):
        self.subject = medium_format(name='Name')

    def test__medium_format__instance(self):
        self.assertIsInstance(self.subject, medium_format)

    def test__medium_format__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
