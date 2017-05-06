from django.test import TestCase
from ..models import alternative_release


class test_alternative_release(TestCase):
    def setUp(self):
        self.subject = alternative_release(name='Name')

    def test__alternative_release__instance(self):
        self.assertIsInstance(self.subject, alternative_release)

    def test__alternative_release__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
