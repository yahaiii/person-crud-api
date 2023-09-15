import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, select, insert, update, delete

app = Flask(__name__)

# Get database credentials from environment variables
db_username = os.environ.get('DATABASE_USERNAME')
db_password = os.environ.get('DATABASE_PASSWORD')

# Create the DTABASE_URL
db_url = f'mysql+mysqlconnector://{db_username}:{db_password}@yahai.mysql.pythonanywhere-services.com/yahai$persons'

# Create a SQLAlchemy engine (you can change the database URL as needed)
engine = create_engine(db_url)

# Create a SQLAlchemy MetaData object
metadata = MetaData()

# Reflect the 'persons' table and bind it to the engine
metadata.reflect(bind=engine)

# Get the 'persons' table from the reflected metadata
persons_table = metadata.tables['persons']

@app.route('/api', methods=['POST'])
def create_person():
    data = request.json  # JSON request data containing person details

    try:
        # Create a new person in the database
        with engine.connect() as connection:
            query = insert(persons_table).values(**data)
            connection.execute(query)
            connection.commit()  # Explicitly commit the transaction

        return jsonify({"message": "Person created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error

@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    with engine.connect() as connection:
        query = select(persons_table).where(persons_table.c.person_id == person_id)
        result = connection.execute(query).fetchone()

    if result is None:
        return jsonify({"error": "Person not found"}), 404

    person_dict = {}
    for column, value in zip(persons_table.columns, result):
        person_dict[column.name] = value

    return jsonify(person_dict)

@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = request.json  # JSON request data containing updated person details

    with engine.connect() as connection:
        query = update(persons_table).where(persons_table.c.person_id == person_id).values(**data)
        result = connection.execute(query)
        connection.commit()  # Commit the changes to the database

    if result.rowcount == 0:
        return jsonify({"error": "Person not found"}), 404

    return jsonify({"message": "Person updated successfully"})

@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    with engine.connect() as connection:
        query = delete(persons_table).where(persons_table.c.person_id == person_id)
        result = connection.execute(query)
        connection.commit()  # Commit the changes to the database

    if result.rowcount == 0:
        return jsonify({"error": "Person not found"}), 404

    return jsonify({"message": "Person deleted successfully"})

@app.route('/api/<dynamic_param>', methods=['GET', 'PUT', 'DELETE'])
def process_person(dynamic_param):
    try:
        # Check if the dynamic parameter is a valid integer (person_id)
        if dynamic_param.isdigit():
            person_id = int(dynamic_param)
            if request.method == 'GET':
                # Retrieve a person by person_id
                with engine.connect() as connection:
                    query = select(persons_table).where(persons_table.c.person_id == person_id)
                    result = connection.execute(query).fetchone()

                if result is None:
                    return jsonify({"error": "Person not found by person_id"}), 404

                person_dict = {}
                for column, value in zip(persons_table.columns, result):
                    person_dict[column.name] = value

                return jsonify(person_dict)

            elif request.method == 'PUT':
                # Update a person by person_id
                data = request.json
                with engine.connect() as connection:
                    query = update(persons_table).where(persons_table.c.person_id == person_id).values(**data)
                    result = connection.execute(query)
                    connection.commit()

                if result.rowcount == 0:
                    return jsonify({"error": "Person not found by person_id"}), 404

                return jsonify({"message": "Person updated successfully"})

            elif request.method == 'DELETE':
                # Delete a person by person_id
                with engine.connect() as connection:
                    query = delete(persons_table).where(persons_table.c.person_id == person_id)
                    result = connection.execute(query)
                    connection.commit()

                if result.rowcount == 0:
                    return jsonify({"error": "Person not found by person_id"}), 404

                return jsonify({"message": "Person deleted successfully"})

        else:
            # Handle CRUD operations based on person_name (string)
            if request.method == 'GET':
                # Retrieve a person by person_name
                with engine.connect() as connection:
                    query = select(persons_table).where(persons_table.c.name == dynamic_param)
                    result = connection.execute(query).fetchone()

                if result is None:
                    return jsonify({"error": "Person not found by person_name"}), 404

                person_dict = {}
                for column, value in zip(persons_table.columns, result):
                    person_dict[column.name] = value

                return jsonify(person_dict)

            elif request.method == 'PUT':
                # Update a person by person_name
                data = request.json
                with engine.connect() as connection:
                    query = update(persons_table).where(persons_table.c.name == dynamic_param).values(**data)
                    result = connection.execute(query)
                    connection.commit()

                if result.rowcount == 0:
                    return jsonify({"error": "Person not found by person_name"}), 404

                return jsonify({"message": "Person updated successfully"})

            elif request.method == 'DELETE':
                # Delete a person by person_name
                with engine.connect() as connection:
                    query = delete(persons_table).where(persons_table.c.name == dynamic_param)
                    result = connection.execute(query)
                    connection.commit()

                if result.rowcount == 0:
                    return jsonify({"error": "Person not found by person_name"}), 404

                return jsonify({"message": "Person deleted successfully"})

        return jsonify({"error": "Invalid input"}), 400  # Bad Request
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error
    
if __name__ == '__main__':
    app.run(debug=True)
