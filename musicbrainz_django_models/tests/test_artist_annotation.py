from django.test import TestCase
from ..models import artist_annotation


class test_artist_annotation(TestCase):
    def setUp(self):
        self.subject = artist_annotation()

    def test__artist_annotation__instance(self):
        self.assertIsInstance(self.subject, artist_annotation)

    def test__artist_annotation__str(self):
        self.assertEqual(str(self.subject), 'Artist Annotation')
