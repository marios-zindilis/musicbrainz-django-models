from django.test import TestCase
from ..models import release


class test_release(TestCase):
    def setUp(self):
        self.subject = release(name='Name')

    def test__release__instance(self):
        self.assertIsInstance(self.subject, release)

    def test__release__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__release__unicode(self):
        self.assertEqual(self.subject.__unicode__(), self.subject.name)
