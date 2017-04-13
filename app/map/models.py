from .. import db

from datetime import datetime


class Comment(db.EmbeddedDocument):
	name = db.StringField(required=True)
	password = db.PasswordField(required=True)
	content = db.StringField(required=True)
	creation = db.DateTimeField(default=datetime.now)


class Restaurant(db.Document):
	name = db.StringField(required=True)
	categories = db.ListField(required=True)
	address = db.StringField()
	site = db.StringField()
	url = db.StringField()
	location = db.GeoPointField(required=True)
	price = db.StringField()
	good = db.IntField(default=0)
	bad = db.IntField(default=0)
	comments = db.EmbeddedDocumentListField(Comment)
	creation = db.DateTimeField(default=datetime.now)
