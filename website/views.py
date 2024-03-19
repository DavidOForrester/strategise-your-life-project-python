from flask import Blueprint, render_template, request
from .models import StrategiseYourLife
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    strageticLifeUnit = request.form.get('strategic-life-unit')
    satisfaction = request.form.get('satisfaction')
    importance = request.form.get('importance')
    timeInvested = request.form.get('time-invested')

    #if strageticLifeUnit == ""
    newStrategiseYourLife = StrategiseYourLife(strategicLifeUnits=strageticLifeUnit, satisfaction=satisfaction, importance=importance, timeInvested=timeInvested)
    db.session.add(newStrategiseYourLife)
    db.session.commit()

    #run the python visual code here
    print('data saved')

  return render_template("home.html")