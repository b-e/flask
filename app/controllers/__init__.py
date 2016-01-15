from flask_restful import Resource
from app.models import Registry
#from app.models import registry_schema
import json

class Read(Resource):
	def get(self):
		ret = Registry.query.all()[0]
		#result = registry_schema.dump(ret)
		return ret