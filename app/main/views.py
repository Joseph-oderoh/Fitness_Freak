from flask import render_template, request
from . import main
from flask_login import login_required



# Views
@main.route('/')
def index():
 
    title = 'Fitness_Freak | Stay Healthy'
    return render_template('index.html', title=title)