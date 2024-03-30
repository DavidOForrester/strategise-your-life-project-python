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

  #list of the strategic life units to add as the first col of the table
  strategicLifeUnits = ['Significant Other','Family','Friends','Physical Health/sports','Mental Health/mindfulness','Spirituality/faith','Community/citizenship','Societal engagement','Job/career','Education/learning','Finances','Hobbies/interests','Online entertainment','Offline entertainment','Physiological needs','Activities of daily living']


  if request.method == 'POST':
      #can get the values back from the form
      data = request.form

      dataList = list(data)

      grouped_data = [dataList[i:i+3] for i in range(0, len(dataList), 3)]

      # Iterate over groups
      for group in grouped_data[:-1]:
          
          strategicLifeUnit = int(group[0].split('-')[1]) + 1
          satisfaction = data.get(group[0])
          importance = data.get(group[1])
          timeInvested = data.get(group[2])

          if satisfaction == "":
             satisfaction = 0
          elif importance == "":
             importance = 0
          elif timeInvested == "":
             timeInvested = 0

          curs = conn.cursor()
          curs.execute(f"UPDATE strategise_your_life SET satisfaction = {satisfaction}, importance = {importance}, timeInvested = {timeInvested} WHERE id = {strategicLifeUnit}")
          conn.commit()
          

      #run the python visual code here
      CreateVisual()

  return render_template("home.html", data=data, form=form, strategicLifeUnits=strategicLifeUnits, zip=zip)