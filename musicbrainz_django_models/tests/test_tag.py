from django.test import TestCase
from ..models import tag


class test_tag(TestCase):
    def setUp(self):
        self.subject = tag(name='Name')

    def test__tag__instance(self):
        self.assertIsInstance(self.subject, tag)

    def test__tag__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
