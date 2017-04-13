from flask import render_template

from app.restaurant.models import Restaurant
from . import food_map
from .. import MAP_CLIENT_ID


@food_map.route('/')
def show_map():
	restaurants = Restaurant.objects()
	return render_template('food-map.html', map_client_id=MAP_CLIENT_ID, restaurants=restaurants)
