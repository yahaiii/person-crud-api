from flask import Flask, request
from flask_restful import Api, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Person

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MySQL01#@localhost/persons'


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
        
        db.session.commit()

        return person

    def delete(self, person_id):
        person = Person.query.get_or_404(person_id)
        db.session.delete(person)
        db.session.commit()
        return '', 204

# Create a resource for creating a new person
class PersonListResource(Resource):
    @marshal_with(person_fields)
    def post(self):
        data = request.get_json()
        person = Person(name=data['name'], age=data['age'], email=data['email'])
        db.session.add(person)
        db.session.commit()
        return person, 201


api.add_resource(PersonResource, '/api/person/<int:person_id>')
api.add_resource(PersonListResource, '/api/person')
