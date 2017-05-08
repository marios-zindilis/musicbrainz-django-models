from django.test import TestCase
from ..models import medium


class test_medium(TestCase):
    def setUp(self):
        self.subject = medium(name='Name')

    def test__medium__instance(self):
        self.assertIsInstance(self.subject, medium)

    def test__medium__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
