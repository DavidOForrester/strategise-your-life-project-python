import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sqlite3


def CreateVisual():
  conn = sqlite3.connect('instance/database.db')

  df = pd.read_sql('SELECT * FROM strategise_your_life', conn)

  #loading the font
  hfont = {'fontname':'Helvetica'}
  
  #defining the colours for the categories
  colours = {
    'Relationships': '#c92f16', 
    'Body mind and spirituality': '#3374c1', 
    'Community and society': '#f5bf32',
    'Job learning and finances': '#469c34',
    'Interests and entertainment': '#8e22c9',
    'Personal care': '#434c4f'
  }

  colour_list = [colours[group] for group in df['strategicLifeAreas']]

  fig = plt.figure(figsize=(10,10))
  ax = fig.add_subplot(111)

  #Setting up the text on the plot
  plt.title('Strategise Your Life', **hfont)
  plt.xlabel('Satisfaction', **hfont)
  plt.ylabel('Importance', **hfont)

  #x and y limits
  plt.xlim((-10,110))
  plt.ylim((-10,110))

  #adding the 4 quadrant lines
  plt.plot([50,50],[-10,110], linewidth=1, color='grey' )
  plt.plot([-10,110],[50,50], linewidth=1, color='grey' )

  #Plots the data points
  plt.scatter(df['satisfaction'], df['importance'], df['timeInvested']*100, c=colour_list)

  #adds the labels to the points
  for i, txt in enumerate(df['strategicLifeUnits']):
    ax.annotate(txt, (df['satisfaction'][i], df['importance'][i]), xytext=(df['satisfaction'][i]+3, df['importance'][i]+3), arrowprops=dict(arrowstyle='-'), **hfont)

  # Turn off tick labels
  ax.set_yticklabels([])
  ax.set_xticklabels([])

  plt.savefig('website/static/visual.png') 

