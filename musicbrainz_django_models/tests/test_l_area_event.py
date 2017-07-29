from django.test import TestCase
from ..models import l_area_event


class test_l_area_event(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_area_event()

    def test__l_area_event__instance(self):
        self.assertIsInstance(self.subject, l_area_event)

    def test__l_area_event__str(self):
        self.assertEqual(str(self.subject), 'L Area Event')
