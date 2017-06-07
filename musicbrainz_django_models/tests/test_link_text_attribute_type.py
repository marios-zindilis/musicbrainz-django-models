from django.test import TestCase
from ..models import link_text_attribute_type
from ..models import link_attribute_type


class test_link_text_attribute_type(TestCase):
    def setUp(self):
        self.subject = link_text_attribute_type()
        self.subject_link_attribute_type_name = 'LAT Name'
        self.subject_link_attribute_type = link_attribute_type(name=self.subject_link_attribute_type_name)
        self.subject_link_attribute_type.save()

    def test__link_text_attribute_type__instance(self):
        self.assertIsInstance(self.subject, link_text_attribute_type)

    def test__link_text_attribute_type__str(self):
        # The str() of the subject `link_text_attribute_type` should be 
        # the same as that of the referenced `link_attribute_type`:
        self.subject.attribute_type = self.subject_link_attribute_type
        self.assertEqual(str(self.subject), str(self.subject_link_attribute_type_name))
