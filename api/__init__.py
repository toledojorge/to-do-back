from flask import Blueprint
from flask import jsonify

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/test', methods=['GET'])
def listar():
    return jsonify("test")