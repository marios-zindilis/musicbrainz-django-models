from django.test import TestCase
from ..models import l_work_work


class test_l_work_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_work_work()

    def test__l_work_work__instance(self):
        self.assertIsInstance(self.subject, l_work_work)

    def test__l_work_work__str(self):
        self.assertEqual(str(self.subject), 'L Work Work')
