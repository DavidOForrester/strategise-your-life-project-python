from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms_sqlalchemy.fields import QuerySelectField
from website.models import StrategiseYourLife

def form_query():
  return StrategiseYourLife.query

class SimpleForm(FlaskForm):
  strategicLifeUnits = QuerySelectField(query_factory=form_query, allow_blank=True, get_label='strategicLifeUnits')
  satisfaction = IntegerField("Satisfaction")
  importance = IntegerField("Importance")
  timeInvested = IntegerField("Time Invested")