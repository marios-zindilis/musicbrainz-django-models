from django.test import TestCase
from ..models import l_label_work


class test_l_label_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_label_work()

    def test__l_label_work__instance(self):
        self.assertIsInstance(self.subject, l_label_work)

    def test__l_label_work__str(self):
        self.assertEqual(str(self.subject), 'L Label Work')
