from .. import db


class Comment(db.EmbeddedDocument):
	name = db.StringField(required=True)
	content = db.StringField(required=True)
	creation = db.DateTimeField()


class Restaurant(db.Document):
	name = db.StringField(required=True)
	type = db.ListField(required=True)
	address = db.StringField()
	url = db.StringField()
	location = db.GeoPointField(required=True)
	price = db.IntField()
	comments = db.EmbeddedDocumentListField(Comment)
	creation = db.DateTimeField()





