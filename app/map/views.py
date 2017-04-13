from . import food_map
from .models import Restaurant, Comment
from .. import MAP_CLIENT_ID

from flask import render_template, redirect


@food_map.route('/')
def show_map():
	return render_template('food-map.html', map_client_id=MAP_CLIENT_ID)


@food_map.route('/test')
def test():
	Restaurant(name='hello', type=['중식', '한식'], location=[37.5157873, 127.0991124], comments=[Comment(name='익명', content='테스트')]).save()
	return redirect('/')
