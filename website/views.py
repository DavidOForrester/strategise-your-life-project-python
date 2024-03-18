from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    strageticLifeUnit = request.form.get('strategic-life-unit')
    satisfaction = request.form.get('satisfaction')
    importance = request.form.get('importance')
    timeInvested = request.form.get('time-invested')


    #you can add error checking here.

  return render_template("home.html")