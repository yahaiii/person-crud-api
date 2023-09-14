from app import db

class Person(db.Model):
    __tablename__ = 'persons'

    person_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email