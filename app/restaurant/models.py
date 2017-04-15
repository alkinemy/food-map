from app import db
from flask_mongoengine.wtf import model_form
from wtforms import PasswordField, validators

from datetime import datetime


class Comment(db.EmbeddedDocument):
	name = db.StringField(required=True)
	password = db.StringField(required=True)
	content = db.StringField(required=True, validators=[validators.InputRequired(message='missing comment content')])
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


# from flask_mongoengine.wtf import model_form
# from wtforms import PasswordField
#
# user = model_form(Comment)
# user.password = PasswordField('Password')

CommentForm = model_form(Comment, exclude=['name'])
CommentForm.password = PasswordField('Password')