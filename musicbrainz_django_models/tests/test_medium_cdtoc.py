from django.test import TestCase
from ..models import medium_cdtoc


class test_medium_cdtoc(TestCase):
    def setUp(self):
        self.subject = medium_cdtoc()

    def test__medium_cdtoc__instance(self):
        self.assertIsInstance(self.subject, medium_cdtoc)

    def test__medium_cdtoc__str(self):
        self.assertEqual(str(self.subject), 'Medium CDTOC')
