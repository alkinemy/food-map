from flask import Blueprint

food_map = Blueprint('food_map', __name__, template_folder='templates')

from . import views
