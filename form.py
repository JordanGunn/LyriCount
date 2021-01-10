from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from get_top_artists import get_top_artists


def validate_artist(artist_name):

    """Validate artist name against list of artists."""

    if artist_name not in get_top_artists():
        raise Val


class WordSearchForm(FlaskForm):

    """Create the form."""

    word_search = StringField('search', )

    def validate_artist(FlaskForm, artist_name):
        """Validate artist name against list of artists."""

        if artist_name not in get_top_artists():
            raise Valida