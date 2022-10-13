from flask import abort, render_template
from carford.models import Persons, Cars

def index():
    persons = Persons.query.all()
    return render_template("index.html", persons = persons)

def person(person_id):
    person = Persons.query.filter_by(id = person_id).first() or abort(404, "Pessoa não encontrada")
    cars = list(Cars.query.filter_by(person_id = person_id))
    return render_template(
        "person.html",
        person = person,
        cars = cars
    )

def car(car_id):
    car = Cars.query.filter_by(id = car_id).first() or abort(404, "Carro não encontrado")
    person = Persons().query.filter_by(id = car.person_id).first() or abort(404, "Dono não encontrado")
    return render_template(
        "car.html",
        car = car,
        person = person
    )
