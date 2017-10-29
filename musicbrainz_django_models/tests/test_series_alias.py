from django.test import TestCase
from ..models import series_alias


class test_series_alias(TestCase):
    def setUp(self):
        self.subject = series_alias(name='Name')

    def test__series_alias__instance(self):
        self.assertIsInstance(self.subject, series_alias)

    def test__series_alias__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
