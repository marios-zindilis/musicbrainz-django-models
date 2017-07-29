from django.test import TestCase
from ..models import l_series_work


class test_l_series_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_series_work()

    def test__l_series_work__instance(self):
        self.assertIsInstance(self.subject, l_series_work)

    def test__l_series_work__str(self):
        self.assertEqual(str(self.subject), 'L Series Work')
