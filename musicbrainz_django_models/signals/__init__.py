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


def pre_save_name_is_member_of_name_choices_list(sender, instance, **kwargs):
    """
    This pre-save check verifies that the `name` attribute of a model is one
    of a predefined list of allowed values.

    It applies to some of the models named `<MODEL>_alias_type`, namely:

    1.  :class:`artist_alias_type`
    2.  :class:`event_alias_type`
    3.  :class:`instrument_alias_type`
    4.  :class:`label_alias_type`
    5.  :class:`place_alias_type`
    6.  :class:`release_alias_type`
    7.  :class:`series_alias_type`

    It also applies to models named `<MODEL>_type`.
    """
    if instance.name not in sender.NAME_CHOICES_LIST:
        raise ValidationError('Name "{}" not one of {}'.format(
            instance.name,
            ', '.join(sender.NAME_CHOICES_LIST)))


def pre_save_model_attribute(sender, instance, **kwargs):
    """
    This pre-save check verifies that either the <MODEL>_attribute_type_allowed_value
    or the <MODEL>_attribute_text fields of a model have a value, but not both.

    This applies to models named `<MODEL>_attribute`, namely:

    1.  :class:`area_attribute`
    2.  :class:`artist_attribute`
    3.  :class:`event_attribute`
    4.  :class:`instrument_attribute`
    5.  :class:`label_attribute`
    6.  :class:`media_attribute`
    7.  :class:`place_attribute`
    8.  :class:`recording_attribute`
    9.  :class:`release_attribute`
    10. :class:`release_group_attribute`
    11. :class:`series_attribute`
    12. :class:`work_attribute`
    """

    # The `sender` name is <MODEL>_attribute, figure out the <MODEL> part:
    model = sender.__name__[:len(sender.__name__)-len('_attribute')]

    instance_attribute_type_allowed_value = getattr(
        instance, '{model}_attribute_type_allowed_value'.format(model=model))
    instance_attribute_text = getattr(instance, '{model}_attribute_text'.format(model=model))

    # Neither the instance_attribute_type_allowed_value nor the
    # instance_attribute_text have a value:
    if not any((instance_attribute_type_allowed_value, instance_attribute_text)):
        raise ValidationError(
            '{model}__attribute_type_allowed_value and {model}_attribute_text '
            'are both empty'.format(model=model))

    # Both the instance_attribute_type_allowed_value and the
    # instance_attribute_text have a value:
    if all((instance_attribute_type_allowed_value, instance_attribute_text)):
        raise ValidationError(
            '{model}__attribute_type_allowed_value and {model}_attribute_text '
            'cannot both have a value.'.format(model=model))
