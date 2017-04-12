from flask import Flask


def create_app():
	app = Flask(__name__)

	from app.map import food_map
	app.register_blueprint(food_map)

	return app

