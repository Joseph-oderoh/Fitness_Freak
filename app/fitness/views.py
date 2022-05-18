from flask import Blueprint
fitness = Blueprint('fitness', __name__)
from . import views, forms