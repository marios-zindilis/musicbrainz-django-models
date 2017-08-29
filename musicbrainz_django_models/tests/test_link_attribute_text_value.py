from django.test import TestCase
from ..models import link_attribute_text_value


class test_link_attribute_text_value(TestCase):
    def setUp(self):
        self.subject = link_attribute_text_value()

    def test__link_attribute_text_value__instance(self):
        self.assertIsInstance(self.subject, link_attribute_text_value)

    def test__link_attribute_text_value__str(self):
        self.assertEqual(str(self.subject), 'Link Attribute Text Value')
