from flask_wtf import FlaskForm
from wtforms import FieldList, SubmitField, FormField, DecimalField

class SimpleForm(FlaskForm):
  satisfaction = DecimalField("Satisfaction")
  importance = DecimalField("Importance")
  timeInvested = DecimalField("Time Invested")

class FullForm(FlaskForm):
  submit = SubmitField("Submit")
  simpleForm = FieldList(FormField(SimpleForm), min_entries=16)