from flask import Blueprint
nutrition = Blueprint('nutrition',__name__)
from . import views,forms