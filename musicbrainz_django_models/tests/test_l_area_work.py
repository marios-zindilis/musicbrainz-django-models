from django.test import TestCase
from ..models import l_area_work


class test_l_area_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_work()

    def test__l_area_work__instance(self):
        self.assertIsInstance(self.subject, l_area_work)

    def test__l_area_work__str(self):
        self.assertEqual(str(self.subject), 'L Area Work')
