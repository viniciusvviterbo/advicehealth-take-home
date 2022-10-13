from flask import jsonify, abort, request
from flask_restful import Resource
from flask_validate_json import validate_json
from carford.blueprints.restapi.schemas import post_person, put_person, post_car, put_car
from carford.models import Persons, Cars
from carford.blueprints.restapi.controller import create_one, read_by_id, read_filter, read_all, update, delete
from operator import attrgetter
from carford.ext.auth import requires_auth

class PersonResource(Resource):
    method_decorators = {'post': [requires_auth]}

    def get(self):
        result = Persons.query.all() or abort(204)

        persons = []

        for person in result:
            id, firstName, lastName = attrgetter('id', 'firstName', 'lastName')(person)
            isSaleOportunity = read_filter(Cars, Cars.person_id, id).count() == 0
            persons.append({
                'id': id,
                'firstName': firstName,
                'lastName': lastName,
                'isSaleOportunity': isSaleOportunity
            })

        return jsonify(
            {
                'persons': persons
            }
        )
    
    @validate_json(post_person)
    def post(self):
        data = request.get_json()

        new_person = Persons(
            firstName = data['firstName'], 
            lastName = data['lastName']
        )

        result = create_one(new_person) or abort(204)

        return jsonify(
            result.to_dict()
        )

class PersonItemResource(Resource):
    method_decorators = {
        'put': [requires_auth],
        'delete': [requires_auth]
    }

    def get(self, person_id):
        person = Persons.query.filter_by(id = person_id).first() or abort(404)

        id, firstName, lastName = attrgetter('id', 'firstName', 'lastName')(person)
        isSaleOportunity = read_filter(Cars, Cars.person_id, id).count() == 0

        return jsonify(
            {
                'id': id,
                'firstName': firstName,
                'lastName': lastName,
                'isSaleOportunity': isSaleOportunity
            }
        )

    @validate_json(put_person)
    def put(self, person_id):
        data = request.get_json()

        updated_person = Persons(
            firstName = data['firstName'], 
            lastName = data['lastName']
        )

        result = update(Persons, updated_person) or abort(204)

        return jsonify(
            {
                'persons': [ result.to_dict() ]
            }
        )

    def delete(self, car_id):
        result = delete(Cars, car_id) or abort(204)

        return jsonify(
            {
                'deleted_id': result
            }
        )

class CarResource(Resource):
    method_decorators = {'post': [requires_auth]}

    def get(self):
        result = Cars.query.all() or abort(204)

        cars = []

        for car in result:
            id, color, model, person_id = attrgetter('id', 'color', 'model', 'person_id')(car)
            cars.append({
                'id': id,
                'color': color.name,
                'model': model.name,
                'person_id': person_id
            })

        return jsonify(
            {
                'cars': cars
            }
        )
    
    @validate_json(post_car)
    def post(self):
        data = request.get_json()

        existing_cars = read_filter(Cars, Cars.person_id, data['person'])

        if existing_cars.count() >= 3:
            return jsonify(
                {
                    'Message': 'This person already reached the maximum number of cars allowed'
                }
            )

        else:
            new_car = Cars(
                color = data['color'], 
                model = data['model'],
                person_id = data['person']
            )

            result = create_one(new_car) or abort(204)

            return jsonify(
                result.to_dict()
            )

class CarItemResource(Resource):
    method_decorators = {
        'put': [requires_auth],
        'delete': [requires_auth]
    }

    def get(self, car_id):
        car = Cars.query.filter_by(id = car_id).first() or abort(404)
        id, color, model, person_id = attrgetter('id', 'color', 'model', 'person_id')(car)
        return jsonify(
            {
                'id': car.id,
                'color': car.color.name,
                'model': car.model.name,
                'person_id': car.person_id
            }
        )

    @validate_json(put_car)
    def put(self, car_id):
        data = request.get_json()

        existing_cars = read_filter(Cars, Cars.person_id, data['person'])

        if existing_cars.count() >= 3:
            return jsonify(
                {
                    'Message': 'The new intended person already reached the maximum number of cars allowed'
                }
            )
        else:
            updated_car = Cars(
                id = data['id'],
                color = data['color'], 
                model = data['model'],
                person_id = data['person']
            )

            result = update(Cars, updated_car) or abort(204)

            return jsonify(
                {
                    'cars': result
                }
            )

    def delete(self, car_id):
        result = delete(Cars, car_id) or abort(204)

        return jsonify(
            {
                'deleted_id': result
            }
        )
