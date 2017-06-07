from django.test import TestCase
from ..models import series


class test_series(TestCase):
    def setUp(self):
        self.subject = series(name='Name')

    def test__series__instance(self):
        self.assertIsInstance(self.subject, series)

    def test__series__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
