from . import food_restaurant
from .models import Restaurant, Comment

from flask import redirect


@food_restaurant.route('/restaurants/<restaurant_id>/feedback/good')
def give_good_feedback(restaurant_id):
	# TODO 구현
	return redirect('/')


@food_restaurant.route('/restaurant/<restaurant_id>/feedback/bac')
def give_bad_feedback(restaurant_id):
	# TODO 구현
	return redirect('/')










@food_restaurant.route('/test')
def test():
	Restaurant(name='hello', categories=['중식', '한식'], location=[37.5157873, 127.0991124], comments=[Comment(name='익명', content='테스트')]).save()
	return redirect('/')


@food_restaurant.route('/restaurants/remove-all')
def remove_all():
	Restaurant.objects().delete()
	return redirect('/')
