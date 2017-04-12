from .. import db


class Restaurant(db.Document):
	name = db.StringField(required=True)
	type = db.ListField(required=True)
	address = db.StringField()
	url = db.StringField()
	location = db.EmbeddedDocumentField(GeoLocation)
	price = db.IntField()
	creation = db.DateTimeField()


class GeoLocation(db.EmbeddedDocument):
	latitude = db.DecimalField(required=True)
	longitude = db.DecimalField(required=True)
