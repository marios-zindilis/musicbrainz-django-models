from django.test import TestCase
from ..models import artist_credit_name


class test_artist_credit_name(TestCase):
    def setUp(self):
        self.subject = artist_credit_name(name='Name')

    def test__artist_credit_name__instance(self):
        self.assertIsInstance(self.subject, artist_credit_name)

    def test__artist_credit_name__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
