from django.test import TestCase
from ..models import release_group_tag_raw


class test_release_group_tag_raw(TestCase):
    def setUp(self):
        self.subject = release_group_tag_raw()

    def test__release_group_tag_raw__instance(self):
        self.assertIsInstance(self.subject, release_group_tag_raw)

    def test__release_group_tag_raw__str(self):
        self.assertEqual(str(self.subject), 'Release Group Tag Raw')
