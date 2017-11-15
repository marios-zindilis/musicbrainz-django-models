from django.test import TestCase
from ..models import artist_attribute_type


class test_artist_attribute_type(TestCase):
    def setUp(self):
        self.subject = artist_attribute_type(name='Name')

    def test__artist_attribute_type__instance(self):
        self.assertIsInstance(self.subject, artist_attribute_type)

    def test__artist_attribute_type__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
