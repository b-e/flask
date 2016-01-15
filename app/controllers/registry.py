from flask_restful import Resource
from app.models import Registry
from app.models import RegistrySchema

class RegistryCtrl(Resource):
	def get(self):
		registry = Registry.query.all()[0]
		rs = RegistrySchema()

		#result = registry_schema.dump(ret)
		return rs.dump(registry).data