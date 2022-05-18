from . import health
from flask import render_template
@health.route('/')
def index():
    title = 'Health and Wellness'
    return render_template('health.html', title=title)