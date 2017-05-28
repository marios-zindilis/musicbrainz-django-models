from django.test import TestCase
from ..models import release_raw


class test_release_raw(TestCase):
    def setUp(self):
        self.subject = release_raw(title='Title')

    def test__release_raw__instance(self):
        self.assertIsInstance(self.subject, release_raw)

    def test__release_raw__str(self):
        self.assertEqual(str(self.subject), self.subject.title)
