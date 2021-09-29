from flask import jsonify
from flask import Blueprint

card_bp = Blueprint('card', __name__, url_prefix='/card')                                                                    

@card_bp.route('/test', methods=['GET'])
def listar():
    return jsonify("test")