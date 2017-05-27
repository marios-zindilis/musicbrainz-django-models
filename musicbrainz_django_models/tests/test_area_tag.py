from django.test import TestCase
from ..models import area_tag


class test_area_tag(TestCase):
    def setUp(self):
        self.subject = area_tag()

    def test__area_tag__instance(self):
        self.assertIsInstance(self.subject, area_tag)

    def test__area_tag__str(self):
        self.assertEqual(str(self.subject), 'Area Tag')
