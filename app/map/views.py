from flask import render_template, request, redirect

import collections

from app.restaurant.models import Restaurant
from . import food_map
from .. import MAP_CLIENT_ID


@food_map.route('/')
def show_map():
	categories = request.args.getlist('categories')

	category_all = ['한식', '중식', '일식', '동남아식', '뷔페', '커피', '패스트푸드', '기타']

	if not categories:
		restaurants = Restaurant.objects().exclude('comments')
		return render_template('food-map.html', map_client_id=MAP_CLIENT_ID, restaurants=restaurants)
	if compare(categories, category_all):
		return redirect('/')
	else:
		restaurants = Restaurant.objects(categories__in=categories).exclude('comments')
		return render_template('food-map.html', map_client_id=MAP_CLIENT_ID, restaurants=restaurants)


def compare(x, y):
	return collections.Counter(x) == collections.Counter(y)




@food_map.route('/hello')
def hello():
	return 'hello food-map'
