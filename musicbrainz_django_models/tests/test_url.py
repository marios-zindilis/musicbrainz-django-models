from django.test import TestCase
from ..models import url


class test_url(TestCase):
    def setUp(self):
        self.subject = url(url='URL')

    def test__url__instance(self):
        self.assertIsInstance(self.subject, url)

    def test__url__str(self):
        self.assertEqual(str(self.subject), self.subject.url)
