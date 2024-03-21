import sqlite3
from flask import Blueprint, render_template, request
import pandas as pd
from website.form import SimpleForm
from website.models import StrategiseYourLife
from website.starting_data import CreateData
from website.visuals import CreateVisual
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
  form = SimpleForm()

  #connects to the database
  conn = sqlite3.connect('instance/database.db')
  df = pd.read_sql('SELECT * FROM strategise_your_life', conn)

  #check to see if the database is empty
  if len(df) == 0:
    #runs the function to create the starting data
    CreateData()

  if request.method == 'POST':
    strageticLifeUnit = request.form.get('strategicLifeUnits')
    satisfaction = request.form.get('satisfaction')
    importance = request.form.get('importance')
    timeInvested = request.form.get('timeinvested')

    if satisfaction == "":
      print('missing satisfaction data')
    elif importance == "":
      print('missing importance data')
    elif timeInvested == "":
      print('missing time invested data')
    #else:
      #newStrategiseYourLife = StrategiseYourLife(strategicLifeUnits=strageticLifeUnit, satisfaction=satisfaction, importance=importance, timeInvested=timeInvested)
      #db.session.add(newStrategiseYourLife)
      #db.session.commit()
      
      #run the python visual code here
      #CreateVisual()

  return render_template("home.html", form=form)