from django.test import TestCase
from ..models import release_tag_raw


class test_release_tag_raw(TestCase):
    def setUp(self):
        self.subject = release_tag_raw()

    def test__release_tag_raw__instance(self):
        self.assertIsInstance(self.subject, release_tag_raw)

    def test__release_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Release Tag Raw')
