from . import db

class StrategiseYourLife(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  strategicLifeUnits = db.Column(db.String(100))
  satisfaction = db.Column(db.Integer)
  importance = db.Column(db.Integer)
  timeInvested = db.Column(db.Integer)
