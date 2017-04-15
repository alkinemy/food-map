from . import food_restaurant
from .models import Restaurant, Comment, CommentForm

from flask import render_template, redirect, request, jsonify, flash


@food_restaurant.route('/restaurants/<restaurant_id>/feedback/good', methods=['POST'])
def give_good_feedback(restaurant_id):
	print(request.remote_addr)
	restaurant = Restaurant.objects().get(id=restaurant_id)
	Restaurant.objects(id=restaurant.id).update_one(inc__good=1)
	restaurant.reload('good')
	return jsonify(good=restaurant.good)


@food_restaurant.route('/restaurants/<restaurant_id>/feedback/bad', methods=['POST'])
def give_bad_feedback(restaurant_id):
	print(request.remote_addr)
	restaurant = Restaurant.objects().get(id=restaurant_id)
	Restaurant.objects(id=restaurant.id).update_one(inc__bad=1)
	restaurant.reload('bad')
	return jsonify(bad=restaurant.bad)


@food_restaurant.route('/restaurants/<restaurant_id>')
def detail(restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	return render_template('restaurant-detail.html', restaurant=restaurant)


@food_restaurant.route('/restaurants/<restaurant_id>/comments', methods=['POST'])
def write_comments(restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	comment_request = request.get_json()
	comment_form = CommentForm.from_json(comment_request)

	if comment_form.validate_on_submit():
		comment = Comment(name='익명', password=comment_request['password'], content=comment_request['content'])
		restaurant.comments.append(comment)
		restaurant.save()
		restaurant.reload('comments')
		return render_template('comment-group.html', comments=restaurant.comments)
	else:
		print(comment_form.errors)
		return jsonify(message=comment_form.errors)

