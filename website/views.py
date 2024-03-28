import sqlite3
from flask import Blueprint, render_template, request
import pandas as pd
from website.form import FullForm
from website.models import StrategiseYourLife
from website.starting_data import CreateData
from website.visuals import CreateVisual
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
  #connects to the database
  conn = sqlite3.connect('instance/database.db')
  df = pd.read_sql('SELECT * FROM strategise_your_life', conn)

  #check to see if the database is empty
  if len(df) == 0:
    #runs the function to create the starting data
    CreateData()

  cur = conn.cursor()
  cur.execute("SELECT * FROM strategise_your_life")
  data = cur.fetchall()

  #creates the form
  form = FullForm()

  strategicLifeUnits = ['Significant Other','Family','Friends','Physical Health/sports','Mental Health/mindfulness','Spirituality/faith','Community/citizenship','Societal engagement','Job/career','Education/learning','Finances','Hobbies/interests','Online entertainment','Offline entertainment''Physiological needs','Activities of daily living']


  if request.method == 'POST':
      #can get the values back from the form
      print(request.form.get('simpleForm-2-satisfaction'))
      
      #run the python visual code here
      CreateVisual()

  return render_template("home.html", data=data, form=form, strategicLifeUnits=strategicLifeUnits, zip=zip)