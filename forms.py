from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Pet Species", choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Pet Photo", validators=[Optional(), URL()])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url = StringField("Pet Photo", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available for Adoption", validators=[Optional()])

    # name = StringField("Snack Name", validators=[InputRequired()])
    # price = FloatField("Price in USD")
    # quantity = IntegerField("How many")
    # is_healthy = BooleanField("This is a healthy snack")
    # category = RadioField("Category", choices=[('ic', 'Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy/Sweets')])
    # select = SelectField("Category", choices=[(1, 'Ice Cream'), (2, 'Potato Chips'), (3, 'Candy/Sweets')], coerce=int)