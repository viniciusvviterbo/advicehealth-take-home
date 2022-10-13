from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required

from wtforms import PasswordField
from wtforms.validators import InputRequired

from carford.models import Persons, Cars, Users
from carford.ext.database import db
from hashlib import sha256

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)
admin = Admin()

class CustomPasswordField(PasswordField):
    def populate_obj(self, obj, name):
        password = self.data
        setattr(obj, name, sha256(password.encode('utf-8')).hexdigest())

class UserView(sqla.ModelView):
    form_extra_fields = {
        'password': CustomPasswordField('Password', validators=[InputRequired()])
    }

def init_app(app):
    admin.name = app.config.TITLE
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.add_view(sqla.ModelView(Persons, db.session))
    admin.add_view(sqla.ModelView(Cars, db.session))
    admin.add_view(UserView(Users, db.session))
