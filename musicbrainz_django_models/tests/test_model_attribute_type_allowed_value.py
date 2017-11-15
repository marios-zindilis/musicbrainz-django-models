from django.test import TestCase
from ..models import area_attribute_type_allowed_value
from ..models import artist_attribute_type_allowed_value
from ..models import event_attribute_type_allowed_value
from ..models import instrument_attribute_type_allowed_value
from ..models import label_attribute_type_allowed_value
from ..models import medium_attribute_type_allowed_value
from ..models import place_attribute_type_allowed_value
from ..models import recording_attribute_type_allowed_value
from ..models import release_attribute_type_allowed_value
from ..models import release_group_attribute_type_allowed_value
from ..models import series_attribute_type_allowed_value
from ..models import work_attribute_type_allowed_value


class test_area_attribute_type_allowed_value(TestCase):
    def setUp(self):
        self.models = (
            area_attribute_type_allowed_value,
            artist_attribute_type_allowed_value,
            event_attribute_type_allowed_value,
            instrument_attribute_type_allowed_value,
            label_attribute_type_allowed_value,
            medium_attribute_type_allowed_value,
            place_attribute_type_allowed_value,
            recording_attribute_type_allowed_value,
            release_attribute_type_allowed_value,
            release_group_attribute_type_allowed_value,
            series_attribute_type_allowed_value,
            work_attribute_type_allowed_value,)

    def test__model_area_attribute_type_allowed_value(self):
        for model in self.models:
            self.subject = model()

            self.assertIsInstance(self.subject, model)

            expected_str = ' '.join([_.title() for _ in model.__name__.split('_')])
            self.assertEqual(str(self.subject), expected_str)
