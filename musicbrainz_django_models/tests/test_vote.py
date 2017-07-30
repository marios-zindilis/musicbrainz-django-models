from django.test import TestCase
from ..models import vote


class test_vote(TestCase):
    def setUp(self):
        self.subject = vote()

    def test__vote__instance(self):
        self.assertIsInstance(self.subject, vote)

    def test__vote__str(self):
        self.assertEqual(str(self.subject), 'Vote')
