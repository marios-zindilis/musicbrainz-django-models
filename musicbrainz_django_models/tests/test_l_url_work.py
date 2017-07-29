from django.test import TestCase
from ..models import l_url_work


class test_l_url_work(TestCase):
    def setUp(self):
        """
        Set up the test subject.
        """
        self.subject = l_url_work()

    def test__l_url_work__instance(self):
        self.assertIsInstance(self.subject, l_url_work)

    def test__l_url_work__str(self):
        self.assertEqual(str(self.subject), 'L Url Work')
