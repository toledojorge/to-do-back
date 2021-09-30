from app.util.validations import validate_required
from app import db

class Person(db.Model):
    MESSAGE_EMAIL_REQUIRED = "Email is required"
    MESSAGE_FIRST_NAME_REQUIRED = "First name is required"
    MESSAGE_LAST_NAME_REQUIRED = "Last name is required"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, id, email, first_name, last_name):
        validate_required(email, self.MESSAGE_EMAIL_REQUIRED)
        validate_required(first_name, self.MESSAGE_FIRST_NAME_REQUIRED)
        validate_required(last_name, self.MESSAGE_LAST_NAME_REQUIRED)

        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name