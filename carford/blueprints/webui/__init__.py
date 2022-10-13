from flask import Blueprint
from carford.blueprints.webui.views import index, person, car

blueprint = Blueprint("webui", __name__, template_folder="templates")

blueprint.add_url_rule("/", view_func=index)
blueprint.add_url_rule("/person/<person_id>", view_func=person, endpoint="personview")
blueprint.add_url_rule("/car/<car_id>", view_func=car, endpoint="carview")

def init_app(app):
    app.register_blueprint(blueprint)
