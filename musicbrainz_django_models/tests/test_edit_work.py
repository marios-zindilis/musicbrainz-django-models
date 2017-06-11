from django.test import TestCase
from ..models import edit_work


class test_edit_work(TestCase):
    def setUp(self):
        self.subject = edit_work()

    def test__edit_work__instance(self):
        self.assertIsInstance(self.subject, edit_work)

    def test__edit_work__str(self):
        self.assertEqual(str(self.subject), 'Edit Work')
