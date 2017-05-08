from django.test import TestCase
from ..models import alternative_medium


class test_alternative_medium(TestCase):
    def setUp(self):
        self.subject = alternative_medium(name='Name')

    def test__alternative_medium__instance(self):
        self.assertIsInstance(self.subject, alternative_medium)

    def test__alternative_medium__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
