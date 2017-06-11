from django.contrib import admin
from ..models import alternative_medium
from ..models import alternative_medium_track
from ..models import alternative_release
from ..models import alternative_release_type
from .alternative_release_type_admin import alternative_release_type_admin
from ..models import alternative_track
from ..models import annotation
from ..models import application
from ..models import area_alias
from ..models import area_alias_type
from ..models import area_annotation
from ..models import area_gid_redirect
from ..models import area
from ..models import area_tag
from ..models import area_tag_raw
from ..models import area_type
from ..models import artist_alias
from ..models import artist_alias_type
from .artist_alias_type_admin import artist_alias_type_admin
from ..models import artist_annotation
from ..models import artist_credit_name
from ..models import artist_credit
from ..models import artist_gid_redirect
from ..models import artist_ipi
from ..models import artist_isni
from ..models import artist_meta
from ..models import artist
from ..models import artist_rating_raw
from ..models import artist_tag
from ..models import artist_tag_raw
from ..models import artist_type
from ..models import autoeditor_election
from ..models import autoeditor_election_vote
from ..models import cdtoc
from ..models import cdtoc_raw
from ..models import country_area
from ..models import deleted_entity
from ..models import edit_area
from ..models import edit_artist
from ..models import edit_data
from ..models import edit_event
from ..models import edit_instrument
from ..models import edit_label
from ..models import edit_note
from ..models import edit_note_recipient
from ..models import editor_collection
from ..models import editor_collection_type
from ..models import editor_language
from ..models import editor_preference
from ..models import editor
from ..models import editor_subscribe_artist_deleted
from ..models import editor_subscribe_artist
from ..models import editor_subscribe_collection
from ..models import edit_place
from ..models import edit
from ..models import edit_recording
from ..models import edit_release_group
from ..models import edit_release
from ..models import edit_series
from ..models import edit_url
from ..models import edit_work
from ..models import event
from ..models import event_type
from ..models import gender
from ..models import instrument
from ..models import instrument_type
from ..models import label
from ..models import label_type
from ..models import language
from ..models import link_attribute_type
from ..models import link_text_attribute_type
from ..models import medium_format
from ..models import medium
from ..models import place
from ..models import place_type
from ..models import recording
from ..models import release_group_primary_type
from ..models import release_group
from ..models import release_group_secondary_type
from ..models import release_packaging
from ..models import release
from ..models import release_raw
from ..models import release_status
from ..models import script
from ..models import series_ordering_type
from ..models import series
from ..models import series_type
from ..models import tag
from ..models import track
from ..models import url
from ..models import work
from ..models import work_type

admin.site.register(alternative_medium)
admin.site.register(alternative_medium_track)
admin.site.register(alternative_release)
admin.site.register(alternative_release_type, alternative_release_type_admin)
admin.site.register(alternative_track)
admin.site.register(annotation)
admin.site.register(application)
admin.site.register(area_alias)
admin.site.register(area_alias_type)
admin.site.register(area_annotation)
admin.site.register(area_gid_redirect)
admin.site.register(area)
admin.site.register(area_tag)
admin.site.register(area_tag_raw)
admin.site.register(area_type)
admin.site.register(artist_alias)
admin.site.register(artist_alias_type, artist_alias_type_admin)
admin.site.register(artist_annotation)
admin.site.register(artist_credit_name)
admin.site.register(artist_credit)
admin.site.register(artist_gid_redirect)
admin.site.register(artist_ipi)
admin.site.register(artist_isni)
admin.site.register(artist_meta)
admin.site.register(artist)
admin.site.register(artist_rating_raw)
admin.site.register(artist_tag)
admin.site.register(artist_tag_raw)
admin.site.register(artist_type)
admin.site.register(autoeditor_election)
admin.site.register(autoeditor_election_vote)
admin.site.register(cdtoc)
admin.site.register(cdtoc_raw)
admin.site.register(country_area)
admin.site.register(deleted_entity)
admin.site.register(edit_area)
admin.site.register(edit_artist)
admin.site.register(edit_data)
admin.site.register(edit_event)
admin.site.register(edit_instrument)
admin.site.register(edit_label)
admin.site.register(edit_note)
admin.site.register(edit_note_recipient)
admin.site.register(editor_collection)
admin.site.register(editor_collection_type)
admin.site.register(editor_language)
admin.site.register(editor_preference)
admin.site.register(editor)
admin.site.register(editor_subscribe_artist_deleted)
admin.site.register(editor_subscribe_artist)
admin.site.register(editor_subscribe_collection)
admin.site.register(edit_place)
admin.site.register(edit)
admin.site.register(edit_recording)
admin.site.register(edit_release_group)
admin.site.register(edit_release)
admin.site.register(edit_series)
admin.site.register(edit_url)
admin.site.register(edit_work)
admin.site.register(event)
admin.site.register(event_type)
admin.site.register(gender)
admin.site.register(instrument)
admin.site.register(instrument_type)
admin.site.register(label)
admin.site.register(label_type)
admin.site.register(language)
admin.site.register(link_attribute_type)
admin.site.register(link_text_attribute_type)
admin.site.register(medium_format)
admin.site.register(medium)
admin.site.register(place)
admin.site.register(place_type)
admin.site.register(recording)
admin.site.register(release_group_primary_type)
admin.site.register(release_group)
admin.site.register(release_group_secondary_type)
admin.site.register(release_packaging)
admin.site.register(release)
admin.site.register(release_raw)
admin.site.register(release_status)
admin.site.register(script)
admin.site.register(series_ordering_type)
admin.site.register(series)
admin.site.register(series_type)
admin.site.register(tag)
admin.site.register(track)
admin.site.register(url)
admin.site.register(work)
admin.site.register(work_type)
