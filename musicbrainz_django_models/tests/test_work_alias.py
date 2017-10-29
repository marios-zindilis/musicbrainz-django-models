from django.test import TestCase
from ..models import work_alias


class test_work_alias(TestCase):
    def setUp(self):
        self.subject = work_alias(name='Name')

    def test__work_alias__instance(self):
        self.assertIsInstance(self.subject, work_alias)

    def test__work_alias__str(self):
        self.assertEqual(str(self.subject), self.subject.name)
