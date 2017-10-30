from django.test import TestCase
from ..models import area_annotation
from ..models import artist_annotation
from ..models import event_annotation
from ..models import instrument_annotation
from ..models import label_annotation
from ..models import place_annotation
from ..models import recording_annotation
from ..models import release_annotation
from ..models import release_group_annotation
from ..models import series_annotation
from ..models import work_annotation


class test_area_annotation(TestCase):
    def setUp(self):
        self.MODELS = (
            area_annotation,
            artist_annotation,
            event_annotation,
            instrument_annotation,
            label_annotation,
            place_annotation,
            recording_annotation,
            release_annotation,
            release_group_annotation,
            series_annotation,
            work_annotation,)

    def test__model_annotation(self):
        for model in self.MODELS:
            self.subject = model()
            self.assertIsInstance(self.subject, model)

            expected_str = ' '.join([_.title() for _ in model.__name__.split('_')])
            self.assertEqual(str(self.subject), expected_str)
