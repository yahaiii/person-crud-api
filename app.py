from flask import Flask, request
from flask_restful import Api, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Person

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MySQL01#@localhost/db_name'

db = SQLAlchemy(app)

person_fields = {
    'person_id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'email': fields.String,
}


class PersonResource(Resource):
    @marshal_with(person_fields)
    def get(self, person_id):
        # Implement logic to get a person based on person_id
        pass

    @marshal_with(person_fields)
    def put(self, person_id):
        # Implement logic to update a person based on person_id
        pass

    def delete(self, person_id):
        # Implement logic to delete a person based on person_id
        pass

# Create a resource for creating a new person
class PersonListResource(Resource):
    @marshal_with(person_fields)
    def post(self):
        # Implement logic to create a new person
        pass


api.add_resource(PersonResource, '/api/person/<int:person_id>')
api.add_resource(PersonListResource, '/api/person')
