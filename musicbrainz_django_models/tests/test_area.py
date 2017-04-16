from django.test import TestCase
from ..models import area_type, area


class test_area(TestCase):
    def test_str(self):
        subject = area(name='Heaven')
        self.assertEqual(str(subject), subject.name)

    def test_unicode(self):
        subject = area(name='Hell')
        self.assertEqual(subject.__unicode__(), subject.name)

#   def test_end_date_year(self):
#       at = area_type(name='Planet')
#       subject = area(name='Earth', end_date_year=2012, type=at)
#       self.assertTrue(subject.ended)
