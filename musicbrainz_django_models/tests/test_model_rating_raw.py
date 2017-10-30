from django.test import TestCase
from ..models import artist_rating_raw
from ..models import event_rating_raw
from ..models import label_rating_raw
from ..models import recording_rating_raw
from ..models import release_group_rating_raw
from ..models import work_rating_raw


class test_release_group_rating_raw(TestCase):
    def setUp(self):
        self.MODELS = (
            artist_rating_raw,
            event_rating_raw,
            label_rating_raw,
            recording_rating_raw,
            release_group_rating_raw,
            work_rating_raw,)

    def test__model_rating_raw(self):
        for model in self.MODELS:
            self.subject = model()
            self.assertIsInstance(self.subject, model)
            expected_str = ' '.join([_.title() for _ in model.__name__.split('_')])
            self.assertEqual(str(self.subject), expected_str)
