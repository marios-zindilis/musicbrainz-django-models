from django.test import TestCase
from ..models import release_meta


class test_release_meta(TestCase):
    def setUp(self):
        self.subject = release_meta()

    def test__release_meta__instance(self):
        self.assertIsInstance(self.subject, release_meta)

    def test__release_meta__str(self):
        self.assertEqual(str(self.subject), 'Release Meta')
