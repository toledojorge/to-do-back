from flask import Blueprint
from .card_api import card_bp
from .person_api import person_bp

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(card_bp)
api_bp.register_blueprint(person_bp)