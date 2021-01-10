from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, ValidationError
from get_top_artists import get_top_artists


class WordSearchForm(FlaskForm):

    """Create the form."""

    word_search = StringField('search', validators=[InputRequired()])

    @staticmethod
    def validate_artist(form, field):
        """Validate artist name against list of artists."""
        if field.data not in get_top_artists():
            raise ValidationError("That artist isn't available.")
