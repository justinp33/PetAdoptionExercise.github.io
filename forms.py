from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(values=["cat","dog","porcupine"])])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0,max=30)])
    notes = StringField("Notes")

class PetForm(FlaskForm):
    """Form for editing pet."""

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])

    notes = StringField("Notes")

    available = BooleanField("available")


