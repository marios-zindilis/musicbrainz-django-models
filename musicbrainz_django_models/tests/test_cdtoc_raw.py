from django.test import TestCase
from ..models import cdtoc_raw


class test_cdtoc_raw(TestCase):
    def setUp(self):
        self.subject = cdtoc_raw(discid='Disc ID')

    def test__cdtoc_raw__instance(self):
        self.assertIsInstance(self.subject, cdtoc_raw)

    def test__cdtoc_raw__str(self):
        self.assertEqual(str(self.subject), self.subject.discid)
