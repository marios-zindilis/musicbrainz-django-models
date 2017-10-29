from django.core.exceptions import ValidationError


def pre_save_model_alias(sender, instance, **kwargs):
    """
    This pre-save check verifies that when the `type` of a model is
    "Search hint", the rest of the attributes have some predefined values.
    This applies to some of the models named `<MODEL>_alias`, namely:

    1.  :class:`artist_alias`
    2.  :class:`event_alias`
    3.  :class:`instrument_alias`
    4.  :class:`label_alias`
    5.  :class:`place_alias`
    6.  :class:`series_alias`
    7.  :class:`work_alias`
    """
    if instance.type and instance.type.name == instance.type.SEARCH_HINT:
        instance.sort_name = instance.name
        instance.begin_date_year = None
        instance.begin_date_month = None
        instance.begin_date_day = None
        instance.end_date_year = None
        instance.end_date_month = None
        instance.end_date_day = None
        instance.primary_for_locale = False
        instance.locale = None


def pre_save_model_alias_type(sender, instance, **kwargs):
    """
    This pre-save check verifies that the `name` attribute of a model is one
    of a predefined list of allowed values. It applies to some of the models
    named `<MODEL>_alias_type`, namely:

    1.  :class:`artist_alias_type`
    2.  :class:`event_alias_type`
    3.  :class:`instrument_alias_type`
    4.  :class:`label_alias_type`
    5.  :class:`place_alias_type`
    6.  :class:`release_alias_type`
    7.  :class:`series_alias_type`
    """
    if instance.name not in sender.NAME_CHOICES_LIST:
        raise ValidationError('Name "{}" not one of {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICES_LIST)))
