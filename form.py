from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from get_top_artists import get_top_artists


class WordSearchForm(FlaskForm):

    """Create the form."""

    word_search = StringField('Search', validators=[InputRequired()])
    submit = SubmitField('Search')

    #
    # @staticmethod
    # def validate_artist(form, field):
    #     """Validate artist name against list of artists."""
    #     if field.data not in get_top_artists():
    #         raise ValidationError("That artist isn't available.")
