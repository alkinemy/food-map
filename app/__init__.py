from flask import Flask
from flask_mongoengine import MongoEngine

# from app.map.models import Restaurant


db = MongoEngine()


def create_app():
	app = Flask(__name__)

	app.config['MONGODB_SETTINGS'] = {
		'db': 'food-map',
		'host': 'mongodb://localhost/database_name'
	}

	db.init_app(app)
	# db.register([Restaurant])

	from app.map import food_map
	app.register_blueprint(food_map)

	return app
