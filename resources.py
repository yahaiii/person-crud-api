from flask_restful import Resource, fields, marshal_with, reqparse
from flask import request
from models import Person  # Import the Person model
from create_app import db

person_fields = {
    'person_id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'email': fields.String,
}

class PersonResource(Resource):
    @marshal_with(person_fields)
    def get(self, person_id):
        person = Person.query.get_or_404(person_id)
        return person

    @marshal_with(person_fields)
    def put(self, person_id):
        person = Person.query.get_or_404(person_id)

        # Update person attributes based on the request data
        data = request.get_json()
        if 'name' in data:
            person.name = data['name']
        if 'age' in data:
            person.age = data['age']
        if 'email' in data:
            person.email = data['email']
        
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error updating the person'}, 500

        return person

    def delete(self, person_id):
        person = Person.query.get_or_404(person_id)
        try:
            db.session.delete(person)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error deleting the person'}, 500
        return '', 204

class PersonListResource(Resource):
    @marshal_with(person_fields)
    def post(self):
        data = request.get_json()
        person = Person(name=data['name'], age=data['age'], email=data['email'])
        try:
            db.session.add(person)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error creating the person'}, 500
        return person, 201
