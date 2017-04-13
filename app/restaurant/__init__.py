from flask import Blueprint

food_restaurant = Blueprint('restaurant', __name__, template_folder='templates')

from . import views