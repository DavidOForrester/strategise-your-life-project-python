import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sqlite3


def CreateVisual():
  conn = sqlite3.connect('instance/database.db')

  df = pd.read_sql('SELECT * FROM strategise_your_life', conn)
  
  #defining the colours for the categories

  fig = plt.figure(figsize=(10,10))
  ax = fig.add_subplot(111)

  #Setting up the text on the plot
  plt.title('Strategise Your Life')
  plt.xlabel('Satisfaction')
  plt.ylabel('Importance')

  #x and y limits
  plt.xlim((0,10))
  plt.ylim((0,10))

  #adding the 4 quadrant lines
  plt.plot([5,5],[0,11], linewidth=1, color='grey' )
  plt.plot([0,11],[5,5], linewidth=1, color='grey' )

  #Plots the data points
  plt.scatter(df['satisfaction'], df['importance'], df['timeInvested']*100),# c=colour_list)

  #adds the labels to the points
  for i, txt in enumerate(df['strategicLifeUnits']):
    ax.annotate(txt, (df['satisfaction'][i], df['importance'][i]), xytext=(df['satisfaction'][i]+0.3, df['importance'][i]+0.3), arrowprops=dict(arrowstyle='-'))

  # Turn off tick labels
  ax.set_yticklabels([])
  ax.set_xticklabels([])

  plt.savefig('website/static/visual.png') 

