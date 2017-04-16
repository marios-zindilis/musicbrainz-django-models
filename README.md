# MusicBrainz Django Models #

This project is an attempt to express the database schema of the
[MusicBrainz Server][1] as Django models. The purpose is purely academic,
aiming to help gain a deeper understanding of the MusicBrainz Schema, as well
as dive into Django Models.

  [1]: https://github.com/metabrainz/musicbrainz-server
    "The MusicBrainz Server GitHub Repository"

The documentation generated from the Django models is [available online][2].

  [2]: https://zindilis.com/projects/musicbrainz-django-models/_docs/
    "Documentation of the MusicBrainz Django Models"

## Process ##

1.  Model names use a `lowercase_with_underscores` naming format, for
    consistency with the naming used in the MusicBrainz Server.
2.  The database table name is explicitly defined in the `Meta` class of each
    model, for consistency with the naming used in the MusicBrainz Server.

## License ##

**MusicBrainz Django Models** inherits the license of the MusicBrainz Server,
and is therefore released under GPLv2 or later.
