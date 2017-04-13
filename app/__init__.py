from flask import Flask
from flask_mongoengine import MongoEngine

import os


db = MongoEngine()

MAP_CLIENT_ID = os.environ.get('MAP_CLIENT_ID')


def create_app():
	app = Flask(__name__)
	# app.config.from_object(config(config_name))

	app.config['MONGODB_SETTINGS'] = {
		'db': 'food-map',
		'host': '127.0.0.1'
	}

	# config[config_name].init_app(app)

	db.init_app(app)

	from app.map import food_map
	app.register_blueprint(food_map)

	return app
