from django.test import TestCase
from ..models import release_coverart


class test_release_coverart(TestCase):
    def setUp(self):
        self.subject = release_coverart()

    def test__release_coverart__instance(self):
        self.assertIsInstance(self.subject, release_coverart)

    def test__release_coverart__str(self):
        self.assertEqual(str(self.subject), 'Release CoverArt')
