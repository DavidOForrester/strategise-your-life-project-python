from flask import Flask, render_template, request, send_file, session
import pandas as pd
from form import FullForm
from visuals import CreateVisual
import base64
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdjkslrewpfjdsklsdfjker'

@app.route('/', methods=['GET', 'POST'])
def home():
  intData = {
     'strategicLifeUnits':['Partner','Family','Friends','Exercise','Mental health','Faith','Community','Volunteering','Career','Education','Finances','Hobbies','Online entmt','Offline entmt','Eating/Sleeping','Daily living'],
     'strategicLifeAreas':['Relationships','Relationships','Relationships','Body mind and spirituality','Body mind and spirituality','Body mind and spirituality','Community and society','Community and society','Job learning and finances','Job learning and finances','Job learning and finances','Interests and entertainment','Interests and entertainment','Interests and entertainment','Personal care','Personal care'],
     'satisfaction':[50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0],
     'importance':[50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0],
     'timeInvested':[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  }
  
  df = pd.DataFrame(intData)

  #creates the form
  form = FullForm()

  #set total time to 0
  timeTotal = 0

  data = ""
  visualData = ""

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

      # Iterate over groups
      for group in grouped_data:
        #extracts the data from the dic
        strategicLifeUnit = int(group[0].split('-')[1])
        satisfaction = float(data.get(group[0]))
        importance = float(data.get(group[1]))
        timeInvested = data.get(group[2])

        #checks if the user has left cells blank
        if timeInvested == "":
           timeInvested = 0.1
           timeTotal = timeTotal + 0
        elif timeInvested == '0':
            timeInvested = 0.1
            timeTotal = timeTotal + 0
        else:
            timeTotal = timeTotal + float(timeInvested)

        #updates the data frame
        df.loc[strategicLifeUnit, 'satisfaction'] = round(satisfaction, 2)
        df.loc[strategicLifeUnit, 'importance'] = round(importance, 2)
        df.loc[strategicLifeUnit, 'timeInvested'] = float(timeInvested)

      #run the python visual code here
      buf = CreateVisual(df)
      visualData = base64.b64encode(buf.getbuffer()).decode("ascii")

      #saves the data frame into the session
      session["data"] = df.to_json()

  return render_template("home.html", 
                         data=data, 
                         form=form, 
                         strategicLifeUnits=strategicLifeUnits, 
                         zip=zip, 
                         timeTotal=timeTotal, 
                         tableCellColour=tableCellColour,
                         visual=visualData)

@app.route('/download_csv')
def download_csv():
  #gets the json data from from the session
  df = session.get('data')
  df = pd.read_json(df, dtype=False)

  #sets up data frame into a csv steam
  buf = BytesIO()
  df.to_csv(buf)
  buf.seek(0)

  return send_file(buf,download_name="data.csv",mimetype="text/csv")

if __name__ == '__main__':
  app.run(debug=True)