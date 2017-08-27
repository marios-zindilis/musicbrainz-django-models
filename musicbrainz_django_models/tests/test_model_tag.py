from django.test import TestCase
from ..models import area_tag
from ..models import artist_tag
from ..models import event_tag
from ..models import instrument_tag
from ..models import label_tag
from ..models import place_tag
from ..models import recording_tag
from ..models import release_tag
from ..models import release_group_tag
from ..models import series_tag
from ..models import work_tag


class test_label_tag(TestCase):
    def setUp(self):
        self.MODELS = (
            area_tag,
            artist_tag,
            event_tag,
            instrument_tag,
            label_tag,
            place_tag,
            recording_tag,
            release_tag,
            release_group_tag,
            series_tag,
            work_tag)

    def test_model_tag(self):
        for model in self.MODELS:
            self.subject = model()
            self.assertIsInstance(self.subject, model)

            expected_str = '{} Tag'.format(  # model.__name__.split('_')[0].title())
                ' '.join([_.title() for _ in model.__name__.split('_')[:-1]]))
            self.assertEqual(str(self.subject), expected_str)
