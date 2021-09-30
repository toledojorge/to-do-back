from app.util.validations import validate_required
from app import db
from app.model.person import Person

class Card(db.Model):
    __tablename__ = 'card'
    MESSAGE_NAME_REQUIRED = "Name is required"
    MESSAGE_DESCRIPTION_REQUIRED = "Description is required"
    MESSAGE_STATE_REQUIRED = "State is required"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    state = db.Column(db.Boolean(), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship(Person)

    def __init__(self, id, name, description, state, person_id):
        validate_required(name, self.MESSAGE_NAME_REQUIRED)
        validate_required(description, self.MESSAGE_DESCRIPTION_REQUIRED)
        #validate_required(state, self.MESSAGE_STATE_REQUIRED)

        self.id = id
        self.name = name
        self.description = description
        self.state = state
        self.person_id = person_id