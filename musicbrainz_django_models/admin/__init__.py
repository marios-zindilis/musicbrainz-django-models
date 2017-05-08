from django.contrib import admin
from ..models import alternative_medium
from ..models import alternative_release
from ..models import alternative_release_type
from .alternative_release_type_admin import alternative_release_type_admin
from ..models import area
from ..models import area_type
from ..models import artist_alias
from ..models import artist_alias_type
from .artist_alias_type_admin import artist_alias_type_admin
from ..models import artist_credit
from ..models import artist_ipi
from ..models import artist_isni
from ..models import artist
from ..models import artist_type
from ..models import gender
from ..models import instrument
from ..models import instrument_type
from ..models import label
from ..models import label_type
from ..models import language
from ..models import medium_format
from ..models import medium
from ..models import recording
from ..models import release_group_primary_type
from ..models import release_group
from ..models import release_group_secondary_type
from ..models import release_packaging
from ..models import release
from ..models import release_status
from ..models import script
from ..models import work
from ..models import work_type

admin.site.register(alternative_medium)
admin.site.register(alternative_release)
admin.site.register(alternative_release_type, alternative_release_type_admin)
admin.site.register(area)
admin.site.register(area_type)
admin.site.register(artist_alias)
admin.site.register(artist_alias_type, artist_alias_type_admin)
admin.site.register(artist_credit)
admin.site.register(artist_ipi)
admin.site.register(artist_isni)
admin.site.register(artist)
admin.site.register(artist_type)
admin.site.register(gender)
admin.site.register(instrument)
admin.site.register(instrument_type)
admin.site.register(label)
admin.site.register(label_type)
admin.site.register(language)
admin.site.register(medium_format)
admin.site.register(medium)
admin.site.register(recording)
admin.site.register(release_group_primary_type)
admin.site.register(release_group)
admin.site.register(release_group_secondary_type)
admin.site.register(release_packaging)
admin.site.register(release)
admin.site.register(release_status)
admin.site.register(script)
admin.site.register(work)
admin.site.register(work_type)
