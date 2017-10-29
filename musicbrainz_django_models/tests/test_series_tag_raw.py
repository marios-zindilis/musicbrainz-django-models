from django.test import TestCase
from ..models import series_tag_raw


class test_series_tag_raw(TestCase):
    def setUp(self):
        self.subject = series_tag_raw()

    def test__series_tag_raw__instance(self):
        self.assertIsInstance(self.subject, series_tag_raw)

    def test__series_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Series Tag Raw')
