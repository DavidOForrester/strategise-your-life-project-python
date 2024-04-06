import sqlite3

def CreateData(db):
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
          conn = sqlite3.connect('instance/database.db')

          curs = conn.cursor()

          sql = f"""
          INSERT INTO strategise_your_life (strategicLifeUnits, strategicLifeAreas, satisfaction, importance, timeInvested) 
          VALUES ('{pair[0]}', '{pair[1]}', 50, 50, 0)
          """

          curs.execute(sql)

          conn.commit()
