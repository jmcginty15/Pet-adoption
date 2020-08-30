from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding new pets"""

    name = StringField('Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), AnyOf(values=['cat', 'dog', 'porcupine', 'fish', 'horse', 'hedgehog'], message='Please enter either "cat", "dog", "porcupine", "fish", "horse", or "hedgehog"')])
    photo_url = StringField('URL of photo', validators=[Optional(), URL(message='Please enter a valid photo URL')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message='Please enter an age between 0 and 30')])
    notes = TextAreaField('Notes', validators=[Optional()])
