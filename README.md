# MusicBrainz Django Models #

This project is an attempt to express the database schema of the
[MusicBrainz Server][1] as Django models.

  [1]: https://github.com/metabrainz/musicbrainz-server
    "The MusicBrainz Server GitHub Repository"

## Process ##

1.  Model names use a `lowercase_with_underscores` naming format, for
    consistency with the naming used in the MusicBrainz Server.
2.  The database table name is explicitly defined in the `Meta` class of each
    model, for consistency with the naming used in the MusicBrainz Server.

## License ##

**MusicBrainz Django Models** inherits the license of the MusicBrainz Server,
and is therefore released under GPLv2 or later.
