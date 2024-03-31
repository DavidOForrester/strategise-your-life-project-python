from website.models import StrategiseYourLife
from . import db

def CreateData():
  area = [
    ['Partner',	'Relationships'],
    ['Family',	'Relationships'],
    ['Friends',	'Relationships'],
    ['Exercise',	'Body mind and spirituality'],
    ['Mental health',	'Body mind and spirituality'],
    ['Faith',	'Body mind and spirituality'],
    ['Community',	'Community and society'],
    ['Volunteering',	'Community and society'],
    ['Career',	'Job learning and finances'],
    ['Education',	'Job learning and finances'],
    ['Finances',	'Job learning and finances'],
    ['Hobbies',	'Interests and entertainment'],
    ['Online entmt',	'Interests and entertainment'],
    ['Offline entmt',	'Interests and entertainment'],
    ['Eating/Sleeping',	'Personal care'],
    ['Daily living',	'Personal care'],
]

  # Iterate over the 2x16 area, considering elements grouped in pairs
  for row in area:
      for i in range(0, len(row), 2):
          pair = row[i:i+2]

          #pre loads the database
          sampleData = StrategiseYourLife(strategicLifeUnits=pair[0], strategicLifeAreas=pair[1], satisfaction=0, importance=0, timeInvested=0)
          db.session.add(sampleData)
          db.session.commit()