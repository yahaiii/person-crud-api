# REST API Documentation

## Introduction

This document provides documentation for the REST API for managing a "person" resource. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on person records in a database.

## Base URL

The base URL for this API is `http://localhost:5000/api`. Replace `localhost` and `5000` with the appropriate values if your API is hosted elsewhere.

## Endpoints

### 1. Create (POST) a New Person

- **Endpoint:** `/api`
- **Description:** Add a new person to the database.
- **Request Format:**
  - Method: POST
  - URL: `http://localhost:5000/api`
  - Request Body: JSON object containing person details:
    ```json
    {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }
    ```
- **Response Format:**
  - Status Code: 201 (Created)
  - Response Body:
    ```json
    {
        "message": "Person created successfully"
    }
    ```

### 2. Read (GET) Person Details

- **Endpoint:** `/api/<int:person_id>`
- **Description:** Fetch details of a person by person_id.
- **Request Format:**
  - Method: GET
  - URL: `http://localhost:5000/api/<int:person_id>`
- **Response Format:**
  - Status Code: 200 (OK) if person is found, 404 (Not Found) otherwise.
  - Response Body (if found):
    ```json
    {
        "person_id": 1,
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }
    ```
  - Response Body (if not found):
    ```json
    {
        "error": "Person not found"
    }
    ```

### 3. Update (PUT) Person Details

- **Endpoint:** `/api/<int:person_id>`
- **Description:** Modify details of an existing person by person_id.
- **Request Format:**
  - Method: PUT
  - URL: `http://localhost:5000/api/<int:person_id>`
  - Request Body: JSON object containing updated person details (age and email):
    ```json
    {
        "age": 31,
        "email": "john.doe.updated@example.com"
    }
    ```
- **Response Format:**
  - Status Code: 200 (OK) if person is found and updated, 404 (Not Found) otherwise.
  - Response Body (if found and updated):
    ```json
    {
        "message": "Person updated successfully"
    }
    ```
  - Response Body (if not found):
    ```json
    {
        "error": "Person not found"
    }
    ```

### 4. Delete (DELETE) a Person

- **Endpoint:** `/api/<int:person_id>`
- **Description:** Remove a person by person_id.
- **Request Format:**
  - Method: DELETE
  - URL: `http://localhost:5000/api/<int:person_id>`
- **Response Format:**
  - Status Code: 200 (OK) if person is found and deleted, 404 (Not Found) otherwise.
  - Response Body (if found and deleted):
    ```json
    {
        "message": "Person deleted successfully"
    }
    ```
  - Response Body (if not found):
    ```json
    {
        "error": "Person not found"
    }
    ```

## Dynamic Parameter Handling

The API is flexible enough to handle dynamic input for both `person_id` and `person_name`. It processes operations based on these parameters and includes validation to allow only strings as input.

## Known Limitations

- Deployment instructions are not included.

## Setting Up and Deploying the API

Refer to the README.md in the project repository for instructions on setting up the API.

