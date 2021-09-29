from app.model.card import Card
from app.service.card_service import CardService
from app.repository.card_repository import CardRepository
from flask import Blueprint, request, jsonify

card_bp = Blueprint('card', __name__, url_prefix='/card')                                                                    
card_repository = CardRepository()
card_service =  CardService(card_repository=card_repository)

@card_bp.route("", methods=['GET'])
def listar():
    return jsonify(card_service.get_all())

@card_bp.route("<id>", methods=["GET"])
def get(id: int):
    return jsonify(card_service.get(id))

@card_bp.route("", methods=["POST"])
def insert():
    body = request.get_json()
    card = Card(id = None, 
                name = body['name'], 
                description = body['description'], 
                state=None)
    return jsonify(card_service.insert(card))

@card_bp.route("<id>", methods=["PUT"])
def update(id: int):
    body = request.get_json()
    card = Card(id = None, 
            name = body['name'],
            description = body['description'], 
            state = body['state'])
    return jsonify(card_service.update(card,id))

@card_bp.route("<id>", methods=["DELETE"])
def delete(id: int):
    return jsonify(card_service.delete(id))
