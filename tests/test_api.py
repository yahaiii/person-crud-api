import pytest
import requests
import json

# Set the base URL of your API
base_url = 'http://localhost:5000/api'  # Change the URL as needed

# Function to pretty-print JSON responses
def print_json(response):
    try:
        print(json.dumps(response.json(), indent=4))
    except ValueError:
        print(response.text)

# Test CREATE (POST)
def test_create_person():
    data = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }

    response = requests.post(base_url, json=data)
    assert response.status_code == 201
    assert response.json()["message"] == "Person created successfully"

# Test READ (GET)
def test_get_person():
    response = requests.get(f'{base_url}/1')  # Replace '1' with an existing person_id
    assert response.status_code == 200

# Test UPDATE (PUT)
def test_update_person():
    data = {
        "age": 31,
        "email": "john.doe.updated@example.com"
    }

    response = requests.put(f'{base_url}/1', json=data)  # Replace '1' with an existing person_id
    assert response.status_code == 200
    assert response.json()["message"] == "Person updated successfully"

# Test DELETE (DELETE)
def test_delete_person():
    response = requests.delete(f'{base_url}/1')  # Replace '1' with an existing person_id
    assert response.status_code == 200
    assert response.json()["message"] == "Person deleted successfully"

if __name__ == '__main__':
    # You can run individual tests or all tests using pytest

    # Example: Run all tests in this file
    pytest.main()
