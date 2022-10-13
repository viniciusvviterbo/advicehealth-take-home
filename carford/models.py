from carford.ext.database import db
import enum
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

class Persons(db.Model, SerializerMixin):
    __tablename__ = 'Persons'
    id = db.Column('id', db.Integer, primary_key = True, unique = True, nullable = False)
    firstName = db.Column('firstName', db.String(255), nullable = False)
    lastName = db.Column('lastName', db.String(255), nullable = False)

    def __str__(self):
        return '{} {}'.format(self.firstName, self.lastName)

class EnumColors(enum.Enum):
    Yellow = 1
    Blue = 2
    Gray = 3

class EnumModels(enum.Enum):
    Hatch = 1
    Sedan = 2
    Convertible = 3

class Cars(db.Model, SerializerMixin):
    __tablename__ = 'Cars'
    id = db.Column('id', db.Integer, primary_key = True, unique = True, nullable = False)
    color = db.Column('color', db.Enum(EnumColors), nullable = False)
    model = db.Column('model', db.Enum(EnumModels), nullable = False)
    person_id = db.Column('person_id', db.Integer, db.ForeignKey('Persons.id'), nullable = False)
    person = db.relationship("Persons", backref="cars")

class Users(db.Model, SerializerMixin):
    __tablename__ = 'Users'
    id = db.Column('id', db.Integer, primary_key = True, unique = True, nullable = False)
    username = db.Column('username', db.String(255), nullable = False)
    password = db.Column('password', db.String(255), nullable = False)
