from django.core.exceptions import ValidationError
from ..models.abstract__model_rating_raw import abstract__model_rating_raw
from ..mixins import ModelMixinTestCase


class test_abstract_model_rating_raw(ModelMixinTestCase):
    mixin = abstract__model_rating_raw

    def setUp(self):
        self.subject = self.model()

    def test__abstract_model_rating_raw__is_instance(self):
        self.assertIsInstance(self.subject, self.model)

    def test__abstract_model_rating_raw__rating_too_low(self):
        self.subject.rating = abstract__model_rating_raw.RATING_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__abstract_model_rating_raw__rating_too_high(self):
        self.subject.rating = abstract__model_rating_raw.RATING_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()
