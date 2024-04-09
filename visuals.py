import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from adjustText import adjust_text
from io import BytesIO


def CreateVisual(df):
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

  fig = plt.figure(figsize=(8,8))
  ax = fig.add_subplot(111)

  #Setting up the text on the plot
  plt.xlabel('Satisfaction', **hfont)
  plt.ylabel('Importance', **hfont)

  #x and y limits
  plt.xlim((-1,11))
  plt.ylim((-1,11))

  #adding the 4 quadrant lines
  plt.plot([5,5],[-1,11], linewidth=1, color='grey', linestyle="dashed", zorder=1)
  plt.plot([-1,11],[5,5], linewidth=1, color='grey', linestyle="dashed", zorder=1)

  #Plots the data points
  plt.scatter(df['satisfaction'], df['importance'], df['timeInvested']*300, c=colour_list, edgecolors='white')

  #adds the labels to the points
  texts = []
  
  for i, txt in enumerate(df['strategicLifeUnits']):
    heightAdjust = 0 #(df['timeInvested'][i] / totalTime) * 110 / 2

    if df['satisfaction'][i] > 7:
      labelOffset = -1.5
    else:
      labelOffset = 0.5

    texts.append(ax.annotate(txt, 
                (df['satisfaction'][i], 
                 df['importance'][i]+heightAdjust), 
                 xytext=(df['satisfaction'][i]+labelOffset, df['importance'][i]), 
                 arrowprops=dict(arrowstyle='-', lw=1), 
                 bbox = dict(boxstyle="round", facecolor="white"),
                 **hfont))
    
  adjust_text(texts)

  #adding high and low text and arrows
  #y axis
  ax.annotate("HIGH", (-0,1.1), xytext=(-1.3, 10.4), rotation=90)
  ax.annotate("LOW", (-1,-1), xytext=(-1.3,-0.8), rotation=90)

  #x axis
  ax.annotate("HIGH", (-1,-1), xytext=(10.4,-1.3))
  ax.annotate("LOW", (-1,-1), xytext=(-0.9,-1.3))

  #adding top left rec to help call out
  recTL = plt.Rectangle((-1,5), 6, 11, color="#ebebeb", zorder=0)
  ax.add_patch(recTL)

  recTR = plt.Rectangle((5,5), 6, 11, color="#f5f5f5", zorder=0)
  ax.add_patch(recTR)

  recBL = plt.Rectangle((-1,-1), 6, 6, color="#f5f5f5", zorder=0)
  ax.add_patch(recBL)

  recBR = plt.Rectangle((5,-1), 6, 6, color="#f5f5f5", zorder=0)
  ax.add_patch(recBR)

  # Turn off tick labels
  ax.set_xticks([])
  ax.set_yticks([])
  ax.spines['top'].set_visible(False)
  ax.spines['bottom'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.spines['right'].set_visible(False)

  buf = BytesIO()
  plt.savefig(buf, format="png", bbox_inches='tight')

  return(buf)