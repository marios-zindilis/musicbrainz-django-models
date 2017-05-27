from django.test import TestCase
from ..models import application


class test_application(TestCase):
    def setUp(self):
        self.subject = application(name='Name')

    def test__application__instance(self):
        self.assertIsInstance(self.subject, application)

    def test__application__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
