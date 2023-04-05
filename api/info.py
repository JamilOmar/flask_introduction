from .shared import api ,Resource

class Info(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(Info, '/')