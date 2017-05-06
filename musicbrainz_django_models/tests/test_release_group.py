from django.test import TestCase
from ..models import release_group


class test_release_group(TestCase):
    def setUp(self):
        self.subject = release_group(name='Name')

    def test__release_group__instance(self):
        self.assertIsInstance(self.subject, release_group)

    def test__release_group__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
