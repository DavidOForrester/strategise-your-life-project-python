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

  #creates the form
  form = FullForm()

  #list of the strategic life units to add as the first col of the table
  strategicLifeUnits = ['Partner','Family','Friends','Exercise','Mental health','Faith','Community','Volunteering','Career','Education','Finances','Hobbies','Online entmt','Offline entmt','Eating/Sleeping','Daily living']
  
  #table background colours
  tableCellColour = ['#fcedf0','#fcedf0','#fcedf0','#e3f4fa','#e3f4fa','#e3f4fa','#fef7e3','#fef7e3','#ecf6ee','#ecf6ee','#ecf6ee','#f5eafa','#f5eafa','#f5eafa','#f3f6f8','#f3f6f8']

  if request.method == 'POST':
      #loads the immutable dic
      data = request.form

      #turns the dic into a list
      dataList = list(data)

      #groups the dic in rows
      grouped_data = [dataList[i:i+3] for i in range(0, len(dataList), 3)]

      #set total time to 0
      timeTotal = 0

      # Iterate over groups
      for group in grouped_data[:-1]:
        #extracts the data from the dic
        strategicLifeUnit = int(group[0].split('-')[1]) + 1
        satisfaction = data.get(group[0])
        importance = data.get(group[1])
        timeInvested = data.get(group[2])

        #determines the time total
        timeTotal = timeTotal + float(timeInvested)

        #checks if the user has left cells blank
        if satisfaction == "":
            satisfaction = 0
        elif importance == "":
            importance = 0
        elif timeInvested == "" or timeInvested == '0':
            timeInvested = 0.1

        #updates the records in the database
        curs = conn.cursor()
        curs.execute(f"UPDATE strategise_your_life SET satisfaction = {satisfaction}, importance = {importance}, timeInvested = {timeInvested} WHERE id = {strategicLifeUnit}")
        conn.commit()

      #run the python visual code here
      CreateVisual()

  return render_template("home.html", 
                         data=data, 
                         form=form, 
                         strategicLifeUnits=strategicLifeUnits, 
                         zip=zip, 
                         timeTotal=timeTotal, 
                         tableCellColour=tableCellColour)