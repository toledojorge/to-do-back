from flask import jsonify
from api import api_bp
from flask import Blueprint

card_bp = Blueprint('card', __name__, url_prefix='/burritos')                                                                    

@card_bp.route('/test', methods=['GET'])
def listar():
    return jsonify("test")