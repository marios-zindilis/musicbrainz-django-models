from django.test import TestCase
from ..models import autoeditor_election


class test_autoeditor_election(TestCase):
    def setUp(self):
        self.subject = autoeditor_election()

    def test__autoeditor_election__instance(self):
        self.assertIsInstance(self.subject, autoeditor_election)

    def test__autoeditor_election__str(self):
        self.assertEqual(str(self.subject), 'Autoeditor Election')
