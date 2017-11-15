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
from ..models import area_attribute
from ..models import area_attribute_type_allowed_value
from ..models import area_attribute_type
from ..models import area_gid_redirect
from ..models import area
from ..models import area_tag
from ..models import area_tag_raw
from ..models import area_type
from ..models import artist_alias
from ..models import artist_alias_type
from .artist_alias_type_admin import artist_alias_type_admin
from ..models import artist_annotation
from ..models import artist_attribute
from ..models import artist_attribute_type_allowed_value
from ..models import artist_attribute_type
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
from ..models import editor_collection_area
from ..models import editor_collection_artist
from ..models import editor_collection_deleted_entity
from ..models import editor_collection_event
from ..models import editor_collection_instrument
from ..models import editor_collection_label
from ..models import editor_collection_place
from ..models import editor_collection
from ..models import editor_collection_recording
from ..models import editor_collection_release_group
from ..models import editor_collection_release
from ..models import editor_collection_series
from ..models import editor_collection_type
from ..models import editor_collection_work
from ..models import editor_language
from ..models import editor_oauth_token
from ..models import editor_preference
from ..models import editor
from ..models import editor_subscribe_artist_deleted
from ..models import editor_subscribe_artist
from ..models import editor_subscribe_collection
from ..models import editor_subscribe_editor
from ..models import editor_subscribe_label_deleted
from ..models import editor_subscribe_label
from ..models import editor_subscribe_series_deleted
from ..models import editor_subscribe_series
from ..models import editor_watch_artist
from ..models import editor_watch_preferences
from ..models import editor_watch_release_group_type
from ..models import editor_watch_release_status
from ..models import edit_place
from ..models import edit
from ..models import edit_recording
from ..models import edit_release_group
from ..models import edit_release
from ..models import edit_series
from ..models import edit_url
from ..models import edit_work
from ..models import event_alias
from ..models import event_alias_type
from ..models import event_annotation
from ..models import event_attribute
from ..models import event_attribute_type_allowed_value
from ..models import event_attribute_type
from ..models import event_gid_redirect
from ..models import event_meta
from ..models import event
from ..models import event_rating_raw
from ..models import event_tag
from ..models import event_tag_raw
from ..models import event_type
from ..models import gender
from ..models import instrument_alias
from ..models import instrument_alias_type
from ..models import instrument_annotation
from ..models import instrument_attribute
from ..models import instrument_attribute_type_allowed_value
from ..models import instrument_attribute_type
from ..models import instrument_gid_redirect
from ..models import instrument
from ..models import instrument_tag
from ..models import instrument_tag_raw
from ..models import instrument_type
from ..models import iso_3166_1
from ..models import iso_3166_2
from ..models import iso_3166_3
from ..models import isrc
from ..models import iswc
from ..models import label_alias
from ..models import label_alias_type
from ..models import label_annotation
from ..models import label_attribute
from ..models import label_attribute_type_allowed_value
from ..models import label_attribute_type
from ..models import label_gid_redirect
from ..models import label_ipi
from ..models import label_isni
from ..models import label_meta
from ..models import label
from ..models import label_rating_raw
from ..models import label_tag
from ..models import label_tag_raw
from ..models import label_type
from ..models import language
from ..models import l_area_area
from ..models import l_area_artist
from ..models import l_area_event
from ..models import l_area_instrument
from ..models import l_area_label
from ..models import l_area_place
from ..models import l_area_recording
from ..models import l_area_release_group
from ..models import l_area_release
from ..models import l_area_series
from ..models import l_area_url
from ..models import l_area_work
from ..models import l_artist_artist
from ..models import l_artist_event
from ..models import l_artist_instrument
from ..models import l_artist_label
from ..models import l_artist_place
from ..models import l_artist_recording
from ..models import l_artist_release_group
from ..models import l_artist_release
from ..models import l_artist_series
from ..models import l_artist_url
from ..models import l_artist_work
from ..models import l_event_event
from ..models import l_event_instrument
from ..models import l_event_label
from ..models import l_event_place
from ..models import l_event_recording
from ..models import l_event_release_group
from ..models import l_event_release
from ..models import l_event_series
from ..models import l_event_url
from ..models import l_event_work
from ..models import link_attribute_credit
from ..models import link_attribute
from ..models import link_attribute_text_value
from ..models import link_attribute_type
from ..models import link_creditable_attribute_type
from ..models import link
from ..models import link_text_attribute_type
from ..models import link_type_attribute_type
from ..models import link_type
from ..models import l_instrument_instrument
from ..models import l_instrument_label
from ..models import l_instrument_place
from ..models import l_instrument_recording
from ..models import l_instrument_release_group
from ..models import l_instrument_release
from ..models import l_instrument_series
from ..models import l_instrument_url
from ..models import l_instrument_work
from ..models import l_label_label
from ..models import l_label_place
from ..models import l_label_recording
from ..models import l_label_release_group
from ..models import l_label_release
from ..models import l_label_series
from ..models import l_label_url
from ..models import l_label_work
from ..models import l_place_place
from ..models import l_place_recording
from ..models import l_place_release_group
from ..models import l_place_release
from ..models import l_place_series
from ..models import l_place_url
from ..models import l_place_work
from ..models import l_recording_recording
from ..models import l_recording_release_group
from ..models import l_recording_release
from ..models import l_recording_series
from ..models import l_recording_url
from ..models import l_recording_work
from ..models import l_release_group_release_group
from ..models import l_release_group_series
from ..models import l_release_group_url
from ..models import l_release_group_work
from ..models import l_release_release_group
from ..models import l_release_release
from ..models import l_release_series
from ..models import l_release_url
from ..models import l_release_work
from ..models import l_series_series
from ..models import l_series_url
from ..models import l_series_work
from ..models import l_url_url
from ..models import l_url_work
from ..models import l_work_work
from ..models import medium_attribute
from ..models import medium_attribute_type_allowed_format
from ..models import medium_attribute_type_allowed_value_allowed_format
from ..models import medium_attribute_type_allowed_value
from ..models import medium_attribute_type
from ..models import medium_cdtoc
from ..models import medium_format
from ..models import medium_index
from ..models import medium
from ..models import old_editor_name
from ..models import orderable_link_type
from ..models import place_alias
from ..models import place_alias_type
from ..models import place_annotation
from ..models import place_attribute
from ..models import place_attribute_type_allowed_value
from ..models import place_attribute_type
from ..models import place_gid_redirect
from ..models import place
from ..models import place_tag
from ..models import place_tag_raw
from ..models import place_type
from ..models import recording_alias
from ..models import recording_alias_type
from ..models import recording_annotation
from ..models import recording_attribute
from ..models import recording_attribute_type_allowed_value
from ..models import recording_attribute_type
from ..models import recording_gid_redirect
from ..models import recording_meta
from ..models import recording
from ..models import recording_rating_raw
from ..models import recording_tag
from ..models import recording_tag_raw
from ..models import release_alias
from ..models import release_alias_type
from ..models import release_annotation
from ..models import release_attribute
from ..models import release_attribute_type_allowed_value
from ..models import release_attribute_type
from ..models import release_country
from ..models import release_coverart
from ..models import release_gid_redirect
from ..models import release_group_alias
from ..models import release_group_alias_type
from ..models import release_group_annotation
from ..models import release_group_attribute
from ..models import release_group_attribute_type_allowed_value
from ..models import release_group_attribute_type
from ..models import release_group_gid_redirect
from ..models import release_group_meta
from ..models import release_group_primary_type
from ..models import release_group
from ..models import release_group_rating_raw
from ..models import release_group_secondary_type_join
from ..models import release_group_secondary_type
from ..models import release_group_tag
from ..models import release_group_tag_raw
from ..models import release_label
from ..models import release_meta
from ..models import release_packaging
from ..models import release
from ..models import release_raw
from ..models import release_status
from ..models import release_tag
from ..models import release_tag_raw
from ..models import release_unknown_country
from ..models import replication_control
from ..models import script
from ..models import series_alias
from ..models import series_alias_type
from ..models import series_annotation
from ..models import series_attribute
from ..models import series_attribute_type_allowed_value
from ..models import series_attribute_type
from ..models import series_gid_redirect
from ..models import series_ordering_type
from ..models import series
from ..models import series_tag
from ..models import series_tag_raw
from ..models import series_type
from ..models import tag
from ..models import tag_relation
from ..models import track_gid_redirect
from ..models import track
from ..models import track_raw
from ..models import url_gid_redirect
from ..models import url
from ..models import vote
from ..models import work_alias
from ..models import work_alias_type
from ..models import work_annotation
from ..models import work_attribute
from ..models import work_attribute_type_allowed_value
from ..models import work_attribute_type
from ..models import work_gid_redirect
from ..models import work_language
from ..models import work_meta
from ..models import work
from ..models import work_rating_raw
from ..models import work_tag
from ..models import work_tag_raw
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
admin.site.register(area_attribute)
admin.site.register(area_attribute_type_allowed_value)
admin.site.register(area_attribute_type)
admin.site.register(area_gid_redirect)
admin.site.register(area)
admin.site.register(area_tag)
admin.site.register(area_tag_raw)
admin.site.register(area_type)
admin.site.register(artist_alias)
admin.site.register(artist_alias_type, artist_alias_type_admin)
admin.site.register(artist_annotation)
admin.site.register(artist_attribute)
admin.site.register(artist_attribute_type_allowed_value)
admin.site.register(artist_attribute_type)
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
admin.site.register(editor_collection_area)
admin.site.register(editor_collection_artist)
admin.site.register(editor_collection_deleted_entity)
admin.site.register(editor_collection_event)
admin.site.register(editor_collection_instrument)
admin.site.register(editor_collection_label)
admin.site.register(editor_collection_place)
admin.site.register(editor_collection)
admin.site.register(editor_collection_recording)
admin.site.register(editor_collection_release_group)
admin.site.register(editor_collection_release)
admin.site.register(editor_collection_series)
admin.site.register(editor_collection_type)
admin.site.register(editor_collection_work)
admin.site.register(editor_language)
admin.site.register(editor_oauth_token)
admin.site.register(editor_preference)
admin.site.register(editor)
admin.site.register(editor_subscribe_artist_deleted)
admin.site.register(editor_subscribe_artist)
admin.site.register(editor_subscribe_collection)
admin.site.register(editor_subscribe_editor)
admin.site.register(editor_subscribe_label_deleted)
admin.site.register(editor_subscribe_label)
admin.site.register(editor_subscribe_series_deleted)
admin.site.register(editor_subscribe_series)
admin.site.register(editor_watch_artist)
admin.site.register(editor_watch_preferences)
admin.site.register(editor_watch_release_group_type)
admin.site.register(editor_watch_release_status)
admin.site.register(edit_place)
admin.site.register(edit)
admin.site.register(edit_recording)
admin.site.register(edit_release_group)
admin.site.register(edit_release)
admin.site.register(edit_series)
admin.site.register(edit_url)
admin.site.register(edit_work)
admin.site.register(event_alias)
admin.site.register(event_alias_type)
admin.site.register(event_annotation)
admin.site.register(event_attribute)
admin.site.register(event_attribute_type_allowed_value)
admin.site.register(event_attribute_type)
admin.site.register(event_gid_redirect)
admin.site.register(event_meta)
admin.site.register(event)
admin.site.register(event_rating_raw)
admin.site.register(event_tag)
admin.site.register(event_tag_raw)
admin.site.register(event_type)
admin.site.register(gender)
admin.site.register(instrument_alias)
admin.site.register(instrument_alias_type)
admin.site.register(instrument_annotation)
admin.site.register(instrument_attribute)
admin.site.register(instrument_attribute_type_allowed_value)
admin.site.register(instrument_attribute_type)
admin.site.register(instrument_gid_redirect)
admin.site.register(instrument)
admin.site.register(instrument_tag)
admin.site.register(instrument_tag_raw)
admin.site.register(instrument_type)
admin.site.register(iso_3166_1)
admin.site.register(iso_3166_2)
admin.site.register(iso_3166_3)
admin.site.register(isrc)
admin.site.register(iswc)
admin.site.register(label_alias)
admin.site.register(label_alias_type)
admin.site.register(label_annotation)
admin.site.register(label_attribute)
admin.site.register(label_attribute_type_allowed_value)
admin.site.register(label_attribute_type)
admin.site.register(label_gid_redirect)
admin.site.register(label_ipi)
admin.site.register(label_isni)
admin.site.register(label_meta)
admin.site.register(label)
admin.site.register(label_rating_raw)
admin.site.register(label_tag)
admin.site.register(label_tag_raw)
admin.site.register(label_type)
admin.site.register(language)
admin.site.register(l_area_area)
admin.site.register(l_area_artist)
admin.site.register(l_area_event)
admin.site.register(l_area_instrument)
admin.site.register(l_area_label)
admin.site.register(l_area_place)
admin.site.register(l_area_recording)
admin.site.register(l_area_release_group)
admin.site.register(l_area_release)
admin.site.register(l_area_series)
admin.site.register(l_area_url)
admin.site.register(l_area_work)
admin.site.register(l_artist_artist)
admin.site.register(l_artist_event)
admin.site.register(l_artist_instrument)
admin.site.register(l_artist_label)
admin.site.register(l_artist_place)
admin.site.register(l_artist_recording)
admin.site.register(l_artist_release_group)
admin.site.register(l_artist_release)
admin.site.register(l_artist_series)
admin.site.register(l_artist_url)
admin.site.register(l_artist_work)
admin.site.register(l_event_event)
admin.site.register(l_event_instrument)
admin.site.register(l_event_label)
admin.site.register(l_event_place)
admin.site.register(l_event_recording)
admin.site.register(l_event_release_group)
admin.site.register(l_event_release)
admin.site.register(l_event_series)
admin.site.register(l_event_url)
admin.site.register(l_event_work)
admin.site.register(link_attribute_credit)
admin.site.register(link_attribute)
admin.site.register(link_attribute_text_value)
admin.site.register(link_attribute_type)
admin.site.register(link_creditable_attribute_type)
admin.site.register(link)
admin.site.register(link_text_attribute_type)
admin.site.register(link_type_attribute_type)
admin.site.register(link_type)
admin.site.register(l_instrument_instrument)
admin.site.register(l_instrument_label)
admin.site.register(l_instrument_place)
admin.site.register(l_instrument_recording)
admin.site.register(l_instrument_release_group)
admin.site.register(l_instrument_release)
admin.site.register(l_instrument_series)
admin.site.register(l_instrument_url)
admin.site.register(l_instrument_work)
admin.site.register(l_label_label)
admin.site.register(l_label_place)
admin.site.register(l_label_recording)
admin.site.register(l_label_release_group)
admin.site.register(l_label_release)
admin.site.register(l_label_series)
admin.site.register(l_label_url)
admin.site.register(l_label_work)
admin.site.register(l_place_place)
admin.site.register(l_place_recording)
admin.site.register(l_place_release_group)
admin.site.register(l_place_release)
admin.site.register(l_place_series)
admin.site.register(l_place_url)
admin.site.register(l_place_work)
admin.site.register(l_recording_recording)
admin.site.register(l_recording_release_group)
admin.site.register(l_recording_release)
admin.site.register(l_recording_series)
admin.site.register(l_recording_url)
admin.site.register(l_recording_work)
admin.site.register(l_release_group_release_group)
admin.site.register(l_release_group_series)
admin.site.register(l_release_group_url)
admin.site.register(l_release_group_work)
admin.site.register(l_release_release_group)
admin.site.register(l_release_release)
admin.site.register(l_release_series)
admin.site.register(l_release_url)
admin.site.register(l_release_work)
admin.site.register(l_series_series)
admin.site.register(l_series_url)
admin.site.register(l_series_work)
admin.site.register(l_url_url)
admin.site.register(l_url_work)
admin.site.register(l_work_work)
admin.site.register(medium_attribute)
admin.site.register(medium_attribute_type_allowed_format)
admin.site.register(medium_attribute_type_allowed_value_allowed_format)
admin.site.register(medium_attribute_type_allowed_value)
admin.site.register(medium_attribute_type)
admin.site.register(medium_cdtoc)
admin.site.register(medium_format)
admin.site.register(medium_index)
admin.site.register(medium)
admin.site.register(old_editor_name)
admin.site.register(orderable_link_type)
admin.site.register(place_alias)
admin.site.register(place_alias_type)
admin.site.register(place_annotation)
admin.site.register(place_attribute)
admin.site.register(place_attribute_type_allowed_value)
admin.site.register(place_attribute_type)
admin.site.register(place_gid_redirect)
admin.site.register(place)
admin.site.register(place_tag)
admin.site.register(place_tag_raw)
admin.site.register(place_type)
admin.site.register(recording_alias)
admin.site.register(recording_alias_type)
admin.site.register(recording_annotation)
admin.site.register(recording_attribute)
admin.site.register(recording_attribute_type_allowed_value)
admin.site.register(recording_attribute_type)
admin.site.register(recording_gid_redirect)
admin.site.register(recording_meta)
admin.site.register(recording)
admin.site.register(recording_rating_raw)
admin.site.register(recording_tag)
admin.site.register(recording_tag_raw)
admin.site.register(release_alias)
admin.site.register(release_alias_type)
admin.site.register(release_annotation)
admin.site.register(release_attribute)
admin.site.register(release_attribute_type_allowed_value)
admin.site.register(release_attribute_type)
admin.site.register(release_country)
admin.site.register(release_coverart)
admin.site.register(release_gid_redirect)
admin.site.register(release_group_alias)
admin.site.register(release_group_alias_type)
admin.site.register(release_group_annotation)
admin.site.register(release_group_attribute)
admin.site.register(release_group_attribute_type_allowed_value)
admin.site.register(release_group_attribute_type)
admin.site.register(release_group_gid_redirect)
admin.site.register(release_group_meta)
admin.site.register(release_group_primary_type)
admin.site.register(release_group)
admin.site.register(release_group_rating_raw)
admin.site.register(release_group_secondary_type_join)
admin.site.register(release_group_secondary_type)
admin.site.register(release_group_tag)
admin.site.register(release_group_tag_raw)
admin.site.register(release_label)
admin.site.register(release_meta)
admin.site.register(release_packaging)
admin.site.register(release)
admin.site.register(release_raw)
admin.site.register(release_status)
admin.site.register(release_tag)
admin.site.register(release_tag_raw)
admin.site.register(release_unknown_country)
admin.site.register(replication_control)
admin.site.register(script)
admin.site.register(series_alias)
admin.site.register(series_alias_type)
admin.site.register(series_annotation)
admin.site.register(series_attribute)
admin.site.register(series_attribute_type_allowed_value)
admin.site.register(series_attribute_type)
admin.site.register(series_gid_redirect)
admin.site.register(series_ordering_type)
admin.site.register(series)
admin.site.register(series_tag)
admin.site.register(series_tag_raw)
admin.site.register(series_type)
admin.site.register(tag)
admin.site.register(tag_relation)
admin.site.register(track_gid_redirect)
admin.site.register(track)
admin.site.register(track_raw)
admin.site.register(url_gid_redirect)
admin.site.register(url)
admin.site.register(vote)
admin.site.register(work_alias)
admin.site.register(work_alias_type)
admin.site.register(work_annotation)
admin.site.register(work_attribute)
admin.site.register(work_attribute_type_allowed_value)
admin.site.register(work_attribute_type)
admin.site.register(work_gid_redirect)
admin.site.register(work_language)
admin.site.register(work_meta)
admin.site.register(work)
admin.site.register(work_rating_raw)
admin.site.register(work_tag)
admin.site.register(work_tag_raw)
admin.site.register(work_type)
