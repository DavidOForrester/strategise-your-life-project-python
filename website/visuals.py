import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sqlite3
from adjustText import adjust_text


def CreateVisual():
  conn = sqlite3.connect('instance/database.db')

  df = pd.read_sql('SELECT * FROM strategise_your_life', conn)

  #updates the sort order to put the smaller dots on top
  df = df.sort_values(by="timeInvested", ascending=False)

  #resets the data frames index to ensure the labels and points align
  df = df.reset_index(drop=True)

  totalTime = sum(df['timeInvested'])

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
  plt.scatter(df['satisfaction'], df['importance'], df['timeInvested']*300, c=colour_list, edgecolors='white')

  #adds the labels to the points
  texts = []
  
  for i, txt in enumerate(df['strategicLifeUnits']):
    heightAdjust = 0 #(df['timeInvested'][i] / totalTime) * 110 / 2

    texts.append(ax.annotate(txt, 
                (df['satisfaction'][i], 
                 df['importance'][i]+heightAdjust), 
                 xytext=(df['satisfaction'][i]+5, df['importance'][i]), 
                 arrowprops=dict(arrowstyle='-', lw=0.5), 
                 bbox = dict(boxstyle="round", facecolor="white"),
                 **hfont))
    
  adjust_text(texts)

  # Turn off tick labels
  ax.set_yticklabels([])
  ax.set_xticklabels([])

  plt.savefig('website/static/visual.png') 

