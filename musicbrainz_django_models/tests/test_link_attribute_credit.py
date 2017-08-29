from django.test import TestCase
from ..models import link_attribute_credit


class test_link_attribute_credit(TestCase):
    def setUp(self):
        self.subject = link_attribute_credit()

    def test__link_attribute_credit__instance(self):
        self.assertIsInstance(self.subject, link_attribute_credit)

    def test__link_attribute_credit__str(self):
        self.assertEqual(str(self.subject), 'Link Attribute Credit')
