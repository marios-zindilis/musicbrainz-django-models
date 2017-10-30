from django.test import TestCase
from ..models import release_group_secondary_type_join


class test_release_group_secondary_type_join(TestCase):
    def setUp(self):
        self.subject = release_group_secondary_type_join()

    def test__release_group_secondary_type_join__instance(self):
        self.assertIsInstance(self.subject, release_group_secondary_type_join)

    def test__release_group_secondary_type_join__str(self):
        self.assertEqual(str(self.subject), 'Release Group Secondary Type Join')
