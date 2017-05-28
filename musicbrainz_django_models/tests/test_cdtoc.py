from django.test import TestCase
from ..models import cdtoc


class test_cdtoc(TestCase):
    def setUp(self):
        self.subject = cdtoc()

    def test__cdtoc__instance(self):
        self.assertIsInstance(self.subject, cdtoc)

    def test__cdtoc__str(self):
        self.assertEqual(str(self.subject), 'CD TOC')
