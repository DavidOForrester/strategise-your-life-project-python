from flask import Blueprint, render_template, request
from website.form import SimpleForm
from website.visuals import CreateVisual
from .models import StrategiseYourLife
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
  form = SimpleForm()

  if request.method == 'POST':
    strageticLifeUnit = request.form.get('opts')
    satisfaction = request.form.get('satisfaction')
    importance = request.form.get('importance')
    timeInvested = request.form.get('timeinvested')

    if satisfaction == "":
      print('missing satisfaction data')
    elif importance == "":
      print('missing importance data')
    elif timeInvested == "":
      print('missing time invested data')
    else:
      newStrategiseYourLife = StrategiseYourLife(strategicLifeUnits=strageticLifeUnit, satisfaction=satisfaction, importance=importance, timeInvested=timeInvested)
      db.session.add(newStrategiseYourLife)
      db.session.commit()
      
      #run the python visual code here
      print('data saved')
      CreateVisual()

  return render_template("home.html", form=form)