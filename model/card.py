from util.validations import validate_required
from app import db

class Card(db.Model):
    MESSAGE_NAME_REQUIRED = "Name is required"
    MESSAGE_DESCRIPTION_REQUIRED = "Description is required"
    MESSAGE_STATE_REQUIRED = "State is required"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    state = db.Column(db.Boolean(), nullable=False)


    def __init__(self, id, name, description, state):
        validate_required(name, self.MESSAGE_NAME_REQUIRED)
        validate_required(description, self.MESSAGE_DESCRIPTION_REQUIRED)
        validate_required(state, self.MESSAGE_STATE_REQUIRED)

        self.id = id
        self.name = name
        self.description = description
        self.state = state