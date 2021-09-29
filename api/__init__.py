from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')
from api.card_api import card_bp
api_bp.register_blueprint(card_bp)