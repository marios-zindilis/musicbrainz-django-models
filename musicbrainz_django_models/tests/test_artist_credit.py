from django.test import TestCase
from ..models import artist_credit


class test_artist_credit(TestCase):
    def setUp(self):
        self.subject = artist_credit(name='Bob Squarepants')

    def test__artist_credit__instance(self):
        self.assertIsInstance(self.subject, artist_credit)

    def test__artist_credit__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
