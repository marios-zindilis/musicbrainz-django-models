from django.test import TestCase
from ..models import place


class test_place(TestCase):
    def setUp(self):
        self.subject = place(name='Name')

    def test__place__instance(self):
        self.assertIsInstance(self.subject, place)

    def test__place__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
