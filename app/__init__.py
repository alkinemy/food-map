import wtforms_json
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_wtf.csrf import CSRFProtect

from datetime import datetime

import os


db = MongoEngine()

csrf = CSRFProtect()

MAP_CLIENT_ID = os.environ.get('MAP_CLIENT_ID')

SECRET_KEY = str(datetime.now().timestamp())


def create_app():
	app = Flask(__name__)
	# app.config.from_object(config(config_name))

	app.config['MONGODB_SETTINGS'] = {
		'db': 'food-map',
		'host': '127.0.0.1'
	}
	app.secret_key = SECRET_KEY

	# config[config_name].init_app(app)

	db.init_app(app)

	csrf.init_app(app)

	wtforms_json.init()

	from app.map import food_map
	app.register_blueprint(food_map)
	from app.restaurant import food_restaurant
	app.register_blueprint(food_restaurant)

	app.config['TRAP_BAD_REQUEST_ERRORS'] = True

	return app
