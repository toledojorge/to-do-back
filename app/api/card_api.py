from service.card_service import CardService
from repository.card_repository import CardRepository
from flask import jsonify
from flask import Blueprint

card_bp = Blueprint('card', __name__, url_prefix='/card')                                                                    
card_repository = CardRepository()
card_service =  CardService(card_repository=card_repository)

@card_bp.route('', methods=['GET'])
def listar():
    return card_service.getAll()