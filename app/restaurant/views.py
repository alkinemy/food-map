from . import food_restaurant
from .models import Restaurant, Comment

from flask import render_template, redirect, request


@food_restaurant.route('/restaurants/<restaurant_id>/feedback/good', methods=['POST'])
def give_good_feedback(restaurant_id):
	print(request.remote_addr)
	restaurant = Restaurant.objects().get(id=restaurant_id)
	Restaurant.objects(id=restaurant.id).update_one(inc__good=1)
	restaurant.reload('good')
	return str(restaurant.good)


@food_restaurant.route('/restaurants/<restaurant_id>/feedback/bad', methods=['POST'])
def give_bad_feedback(restaurant_id):
	print(request.remote_addr)
	restaurant = Restaurant.objects().get(id=restaurant_id)
	Restaurant.objects(id=restaurant.id).update_one(inc__bad=1)
	restaurant.reload('bad')
	return str(restaurant.bad)


@food_restaurant.route('/restaurants/<restaurant_id>')
def detail(restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	return render_template('restaurant-detail.html', restaurant=restaurant)
