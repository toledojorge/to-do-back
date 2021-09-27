from flask import jsonify
from api import api_bp

@api_bp.route('/test', methods=['GET'])
def listar():
    return jsonify("test")