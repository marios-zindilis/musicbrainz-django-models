from django.test import TestCase
from ..models import work_language


class test_work_language(TestCase):
    def setUp(self):
        self.subject = work_language()

    def test__work_language__instance(self):
        self.assertIsInstance(self.subject, work_language)

    def test__work_language__str(self):
        self.assertEqual(str(self.subject), 'Work Language')
