from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def run(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    registrar_blueprint(app)
    
    app.run(host='0.0.0.0', port=5000, debug=True)

def registrar_blueprint(app):
    from .api import api_bp
    app.register_blueprint(api_bp)