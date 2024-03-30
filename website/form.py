from flask_wtf import FlaskForm
from wtforms import FieldList, SubmitField, FormField, DecimalField

#form to be duplicated for each data point
class SimpleForm(FlaskForm):
  satisfaction = DecimalField("Satisfaction")
  importance = DecimalField("Importance")
  timeInvested = DecimalField("Time Invested")

#full form drawing on the other form
class FullForm(FlaskForm):
  submit = SubmitField("Submit")
  simpleForm = FieldList(FormField(SimpleForm), min_entries=16)