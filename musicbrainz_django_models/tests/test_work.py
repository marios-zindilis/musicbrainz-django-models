from django.test import TestCase
from ..models import work


class test_work(TestCase):
    def setUp(self):
        self.subject = work(name='La la la')

    def test__work__instance(self):
        self.assertIsInstance(self.subject, work)

    def test__work__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
