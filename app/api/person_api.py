from app.model.person import Person
from app.schema.person_schema import PersonSchema
from app.service.person_service import PersonService
from app.repository.person_repository import PersonRepository
from flask import Blueprint, request, jsonify

person_bp = Blueprint('person', __name__, url_prefix='/person')                                                                    
person_repository = PersonRepository()
person_service = PersonService(person_repository=person_repository)

@person_bp.route("", methods=['GET'])
def listar():
    persons_schema = PersonSchema(many=True)
    persons = person_service.get_all()
    persons = persons_schema.dump(persons)
    return jsonify(persons)

@person_bp.route("<id>", methods=["GET"])
def get(id: int):
    person_schema = PersonSchema()
    person = person_service.get(id)
    person = person_schema.dump(person)
    return jsonify(person)

@person_bp.route("", methods=["POST"])
def insert():
    body = request.get_json()
    person = Person(id = None, 
                email = body['email'], 
                first_name = body['first_name'], 
                last_name = body['last_name'])
    return jsonify(person_service.insert(person))

@person_bp.route("<id>", methods=["PUT"])
def update(id: int):
    body = request.get_json()
    person = Person(id = None, 
                email = body['email'], 
                first_name = body['first_name'], 
                last_name = body['last_name'])
    return jsonify(person_service.update(person,id))

@person_bp.route("<id>", methods=["DELETE"])
def delete(id: int):
    return jsonify(person_service.delete(id))
