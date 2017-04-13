from . import food_map
from .models import Restaurant, Comment
from .. import MAP_CLIENT_ID

from flask import render_template, redirect


@food_map.route('/')
def show_map():
	restaurants = Restaurant.objects()
	return render_template('food-map.html', map_client_id=MAP_CLIENT_ID, restaurants=restaurants)


@food_map.route('/test')
def test():
	Restaurant(name='hello', categories=['중식', '한식'], location=[37.5157873, 127.0991124], comments=[Comment(name='익명', content='테스트')]).save()
	return redirect('/')


@food_map.route('/restaurants/remove-all')
def remove_all():
	Restaurant.objects().delete()
	return redirect('/')
