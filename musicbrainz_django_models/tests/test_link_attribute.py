from django.test import TestCase
from ..models import link_attribute


class test_link_attribute(TestCase):
    def setUp(self):
        self.subject = link_attribute()

    def test__link_attribute__instance(self):
        self.assertIsInstance(self.subject, link_attribute)

    def test__link_attribute__str(self):
        self.assertEqual(str(self.subject), 'Link Attribute')
