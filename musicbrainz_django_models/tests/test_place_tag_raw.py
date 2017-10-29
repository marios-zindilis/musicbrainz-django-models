from django.test import TestCase
from ..models import place_tag_raw


class test_place_tag_raw(TestCase):
    def setUp(self):
        self.subject = place_tag_raw()

    def test__place_tag_raw__instance(self):
        self.assertIsInstance(self.subject, place_tag_raw)

    def test__place_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Place Tag Raw')
