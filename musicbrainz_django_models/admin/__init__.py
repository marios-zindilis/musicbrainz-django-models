from django.contrib import admin
from ..models import area
from ..models import area_type
from ..models import artist_alias
from ..models import artist_alias_type
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

admin.site.register(area)
admin.site.register(area_type)
admin.site.register(artist_alias)
admin.site.register(artist_alias_type)
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
__ALL__ = [
    area,
    area_type,
    artist_alias,
    artist_alias_type,
    artist_credit,
    artist_ipi,
    artist_isni,
    artist,
    artist_type,
    gender,
    instrument,
    instrument_type,
    label,
    label_type,
    language,
    recording,
    release_group_primary_type,
    release_group,
    release_group_secondary_type,
    release_packaging,
    release,
    release_status,
    script,
    work,
    work_type,
]
