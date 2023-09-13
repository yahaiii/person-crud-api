# Simple Person API

This project is a simple REST API that allows you to perform CRUD (Create, Read, Update, Delete) operations on a "person" resource. You can add, retrieve, modify, and remove person records using the API. The project uses Flask, SQLAlchemy, and MySQL for database interactions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Database Models](#database-models)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

This project aims to provide a simple RESTful API for managing "person" records in a database. It supports basic CRUD operations and allows dynamic parameter handling for operations based on a person's name. The project also includes UML diagrams to represent the system's design and database structure.

## Features

- Create a new person record.
- Retrieve details of a person by ID.
- Update details of an existing person by ID.
- Remove a person by ID.
- Dynamic parameter handling based on a person's name.
- Secure database interactions to prevent common vulnerabilities.

## Technologies Used

- **Flask:** A micro web framework for Python.
- **SQLAlchemy:** An Object-Relational Mapping (ORM) library for Python.
- **MySQL:** A popular relational database management system.
- **Flask-RESTful:** An extension for Flask to simplify API development.
- **Flask-CORS:** An extension for handling Cross-Origin Resource Sharing.
- **Marshmallow:** A library for object serialization/deserialization.
- **Flask-Marshmallow:** An extension for integrating Marshmallow with Flask.
- **pytest:** A testing framework for Python.
- **Postman:** A tool for testing APIs manually.
- **Git:** Version control system.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

Before you begin, ensure you have the following prerequisites:

- Python 3.x
- MySQL server
- Virtual environment (recommended)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yahaiii/person-crud-api.git
   ```

2.  Navigate to the project directory:

    ```bash
    cd person-crud-api
    ```

3.  Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

4.  Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

The project directory structure is organized as follows:

* `app.py`: The main Flask application.
* `models.py`: Contains the database models defined using SQLAlchemy.
* `schemas.py`: Defines Marshmallow schemas for data validation and serialization.
* `config.py`: Configuration settings for the application.
* `tests/`: Directory for test scripts and fixtures.
* `docs/`: Directory for documentation and UML diagrams.
* `requirements.txt`: List of project dependencies.

## Usage
To use the API, run the Flask application and make requests to the specified endpoints. You can use tools like Postman for manual testing or write automated tests using the provided test fixtures.

## API Endpoints
The API provides the following endpoints: