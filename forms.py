from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class Search(FlaskForm):
    search = StringField("Enter your topic name: ", validators=[(DataRequired())])
    min = IntegerField("Enter minimum Number of words: ", validators=[(DataRequired())])
    max = IntegerField("Enter maximum number of words: ", validators=[(DataRequired())])
    submit = SubmitField('submit')
