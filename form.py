from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, InputRequired
from wtforms.widgets import TextArea, SubmitInput

class CafeForm(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired()])
    map_url = StringField('map url', validators=[DataRequired()])
    img_url = StringField('img url', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    seats = StringField('Seat', validators=[DataRequired()])
    coffee_price = StringField('coffee price', validators=[DataRequired()])
    has_toilet = BooleanField('Has Toilet', validators=[DataRequired()])
    has_wifi = BooleanField('Has Wifi', validators=[DataRequired()])
    has_sockets = BooleanField('Has Sockets', validators=[DataRequired()])
    can_take_calls = BooleanField('Can take calls', validators=[DataRequired()])
    
    submit = SubmitField("Add Cafe", widget=SubmitInput(), render_kw={"style": "background-color: #B8621B; color: white;"})
