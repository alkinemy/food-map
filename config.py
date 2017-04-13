#!/usr/bin/env python


class Config(object):
	DEBUG = False
	TESTING = False
	DATABASE_URL = ''
	MAP_CLIENT_KEY = ''

	@staticmethod
	def init_app(app):
		pass


class DevelopConfig(Config):
	DEBUG = True
	DATABASE_URL = '127.0.0.1'


class ProductionConfig(Config):
	DATABASE_URI = '127.0.0.1'


class TestingConfig(Config):
	TESTING = True


config = {
	'develop': DevelopConfig,
	'test': TestingConfig,
	'production': ProductionConfig,

	'default': DevelopConfig
}
