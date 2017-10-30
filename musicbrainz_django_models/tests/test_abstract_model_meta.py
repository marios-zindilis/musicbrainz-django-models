from django.core.exceptions import ValidationError
from ..models.abstract__model_meta import abstract__model_meta
from ..mixins import ModelMixinTestCase


class test_abstract_model_meta(ModelMixinTestCase):
    mixin = abstract__model_meta

    def setUp(self):
        self.subject = self.model.objects.create(pk=1)

    def test__abstract__model_meta__is_instance(self):
        self.assertIsInstance(self.subject, self.model)

    def test__abstract__model_meta__rating_too_low(self):
        self.subject.rating = abstract__model_meta.RATING_MIN - 1
        with self.assertRaises(ValidationError):
            self.subject.save()

    def test__abstract__model_meta__rating_too_high(self):
        self.subject.rating = abstract__model_meta.RATING_MAX + 1
        with self.assertRaises(ValidationError):
            self.subject.save()
