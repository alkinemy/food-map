from flask import Flask
from flask_mongoengine import MongoEngine


db = MongoEngine()


def create_app():
	app = Flask(__name__)

	app.config['MONGODB_SETTINGS'] = {
		'db': 'food-map',
		'host': '127.0.0.1'
	}

	db.init_app(app)

	from app.map import food_map
	app.register_blueprint(food_map)

	return app
