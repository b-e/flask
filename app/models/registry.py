from sqlalchemy import Column, Integer, String
from app.index import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Registry(db.Model):
	__tablename__ = 'registry'

	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.String)
	endpoint = db.Column(db.String)
	phoneNumber = db.Column(db.Integer)
	channel = db.Column(db.String)
	pid = db.Column(db.Integer)

class RegistrySchema(ma.ModelSchema):
    class Meta:
        model = Registry