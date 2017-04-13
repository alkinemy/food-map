from . import food_restaurant

from flask import redirect


@food_restaurant.route('/restaurants/<restaurant_id>/feedback/good')
def give_good_feedback(restaurant_id):
	# TODO 구현
	return redirect('/')


@food_restaurant.route('/restaurant/<restaurant_id>/feedback/bac')
def give_bad_feedback(restaurant_id):
	# TODO 구현
	return redirect('/')
