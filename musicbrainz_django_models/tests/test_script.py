from django.test import TestCase
from ..models import script


class test_script(TestCase):
    def setUp(self):
        self.subject = script(name='Name')

    def test__script__instance(self):
        self.assertIsInstance(self.subject, script)

    def test__script__str(self):
        self.assertEqual(str(self.subject), self.subject.name)

    def test__script__unicode(self):
        self.assertEqual(self.subject.__unicode__(), self.subject.name)
