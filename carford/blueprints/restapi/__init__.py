from flask import Blueprint
from flask_restful import Api
from carford.blueprints.restapi.resources import PersonResource, PersonItemResource, CarResource, CarItemResource

bp = Blueprint("restapi", __name__, url_prefix='/api/v1')
api = Api(bp)

def init_app(app):
    api.add_resource(PersonResource, '/person/')
    api.add_resource(PersonItemResource, '/person/<person_id>')
    api.add_resource(CarResource, '/car/')
    api.add_resource(CarItemResource, '/car/<car_id>')

    app.register_blueprint(bp)
