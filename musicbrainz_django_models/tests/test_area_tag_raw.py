from django.test import TestCase
from ..models import area_tag_raw


class test_area_tag_raw(TestCase):
    def setUp(self):
        self.subject = area_tag_raw()

    def test__area_tag_raw__instance(self):
        self.assertIsInstance(self.subject, area_tag_raw)

    def test__area_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Area Tag Raw')
