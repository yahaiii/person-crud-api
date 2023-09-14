from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)

    # Configure the app here (database URI, CORS, etc.)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/persons'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database extension
    db.init_app(app)

    # Initialize API extension
    api.init_app(app)

    # Enable CORS
    CORS(app)

    # Import and register your routes here
    from resources import PersonResource, PersonListResource
    
    api.add_resource(PersonResource, '/api/person/<int:person_id>')
    api.add_resource(PersonListResource, '/api/person')

    # Create database table
    with app.app_context():
        db.create_all()

    # Error Handling: Define custom error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return {'message': 'Resource not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return {'message': 'Internal server error'}, 500

    return app
