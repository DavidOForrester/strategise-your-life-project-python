from website.models import StrategiseYourLife
from . import db

def CreateData():
  area = [
    ['Significant Other',	'Relationships'],
    ['Family',	'Relationships'],
    ['Friends',	'Relationships'],
    ['Physical Health/sports',	'Body mind and spirituality'],
    ['Mental Health/mindfulness',	'Body mind and spirituality'],
    ['Spirituality/faith',	'Body mind and spirituality'],
    ['Community/citizenship',	'Community and society'],
    ['Societal engagement',	'Community and society'],
    ['Job/career',	'Job learning and finances'],
    ['Education/learning',	'Job learning and finances'],
    ['Finances',	'Job learning and finances'],
    ['Hobbies/interests',	'Interests and entertainment'],
    ['Online entertainment',	'Interests and entertainment'],
    ['Offline entertainment',	'Interests and entertainment'],
    ['Physiological needs',	'Personal care'],
    ['Activities of daily living',	'Personal care'],
]

  # Iterate over the 2x16 area, considering elements grouped in pairs
  for row in area:
      for i in range(0, len(row), 2):
          pair = row[i:i+2]
          print(pair[1])

          sampleData = StrategiseYourLife(strategicLifeUnits=pair[0], strategicLifeAreas=pair[1], satisfaction=0, importance=0, timeInvested=0)
          db.session.add(sampleData)
          db.session.commit()