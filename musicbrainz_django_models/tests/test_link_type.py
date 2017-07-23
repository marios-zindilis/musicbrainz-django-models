from django.test import TestCase
from ..models import link_type


class test_link_type(TestCase):
    def setUp(self):
        self.subject = link_type(name='Name')

    def test__link_type__instance(self):
        self.assertIsInstance(self.subject, link_type)

    def test__link_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
