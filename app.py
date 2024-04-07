from flask import Flask, render_template, request
import pandas as pd
from form import FullForm
from visuals import CreateVisual
import base64

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
      for group in grouped_data[:-1]:
        #extracts the data from the dic
        strategicLifeUnit = int(group[0].split('-')[1])
        satisfaction = float(data.get(group[0]))
        importance = float(data.get(group[1]))
        timeInvested = data.get(group[2])

        #determines the time total
        #timeTotal = timeTotal + float(timeInvested)

        #checks if the user has left cells blank
        if satisfaction == "":
            satisfaction = 0
        elif importance == "":
            importance = 0
        elif timeInvested == "" or timeInvested == '0':
            timeInvested = 0.1

        #updates the data frame
        df.loc[strategicLifeUnit, 'satisfaction'] = satisfaction
        df.loc[strategicLifeUnit, 'importance'] = importance
        df.loc[strategicLifeUnit, 'timeInvested'] = float(timeInvested)

      #run the python visual code here
      buf = CreateVisual(df)
      visualData = base64.b64encode(buf.getbuffer()).decode("ascii")

  return render_template("home.html", 
                         data=data, 
                         form=form, 
                         strategicLifeUnits=strategicLifeUnits, 
                         zip=zip, 
                         timeTotal=timeTotal, 
                         tableCellColour=tableCellColour,
                         visual=visualData)

if __name__ == '__main__':
  app.run(debug=True)