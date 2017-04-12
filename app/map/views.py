from . import food_map

from flask import render_template


@food_map.route("/")
def show_map():
	return render_template('food-map.html')
